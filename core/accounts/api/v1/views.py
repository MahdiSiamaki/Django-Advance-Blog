from rest_framework import generics
from rest_framework.authtoken.models import Token
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.generics import (
    RetrieveUpdateDestroyAPIView,
    RetrieveUpdateAPIView,
)
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from rest_framework_simplejwt.backends import TokenBackend
from rest_framework_simplejwt.views import TokenObtainPairView
from django.shortcuts import get_object_or_404
from mail_templated import send_mail
from rest_framework_simplejwt.tokens import RefreshToken, AccessToken
from jwt.exceptions import InvalidTokenError, ExpiredSignatureError
from .serializers import (
    RegisterSerializer,
    CustomAuthTokenSerializer,
    CustomTokenObtainPairSerializer,
    ChangePasswordSerializer,
    ProfileSerializer,
    EmailVerificationSerializer,
)
from ...models import Profile, User
from ..utils import EmailThread


class RegisterApiView(generics.GenericAPIView):
    serializer_class = RegisterSerializer

    def get_tokens_for_user(self, user):
        refresh = RefreshToken.for_user(user)
        return {
            "refresh": str(refresh),
            "access": str(refresh.access_token),
        }

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()

        # Generate token for verification
        tokens = self.get_tokens_for_user(user)

        # Prepare email context
        context = {
            "name": user.full_name,
            "email": user.email,
            "verification_token": tokens["access"],
            "site_url": request.build_absolute_uri("/accounts/api/v1"),
        }

        # Send verification email
        email_thread = EmailThread(
            subject="Verify Your Email",
            template_name="email/verification.tpl",
            context=context,
        )
        email_thread.start()

        return Response(
            {
                "email": user.email,
                "message": "User Created Successfully. Please check your email to verify your account.",
            },
            status=status.HTTP_201_CREATED,
        )


class CustomObtainAuthToken(ObtainAuthToken):
    serializer_class = CustomAuthTokenSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(
            data=request.data, context={"request": request}
        )
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data["user"]
        token, created = Token.objects.get_or_create(user=user)
        return Response(
            {"token": token.key, "user_id": user.pk, "email": user.email}
        )


class Logout(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        request.user.auth_token.delete()
        return Response(status=status.HTTP_200_OK)


class CustomTokenObtainPairView(TokenObtainPairView):
    serializer_class = CustomTokenObtainPairSerializer


class ChangePasswordView(generics.GenericAPIView):
    serializer_class = ChangePasswordSerializer
    permission_classes = [IsAuthenticated]

    def get_object(self):
        return self.request.user

    def put(self, request, *args, **kwargs):
        self.object = self.get_object()
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        if not self.object.check_password(
            serializer.data.get("old_password")
        ):
            return Response(
                {"old_password": ["Wrong password."]},
                status=status.HTTP_400_BAD_REQUEST,
            )
        self.object.set_password(serializer.data.get("new_password"))
        self.object.save()
        return Response(
            "Password changed successfully", status=status.HTTP_200_OK
        )


class ProfileView(RetrieveUpdateAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = ProfileSerializer

    def get_object(self):
        return get_object_or_404(Profile, user=self.request.user)


class SendEmailView(generics.GenericAPIView):
    serializer_class = EmailVerificationSerializer

    def get_tokens_for_user(self, user):
        refresh = RefreshToken.for_user(user)
        return {
            "refresh": str(refresh),
            "access": str(refresh.access_token),
        }

    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        email = serializer.validated_data["email"]

        try:
            user = User.objects.get(email=email)
            if user.is_verified:
                return Response(
                    {"status": "error", "message": "Email already verified"},
                    status=status.HTTP_400_BAD_REQUEST,
                )

            tokens = self.get_tokens_for_user(user)

            context = {
                "name": user.full_name,
                "email": user.email,
                "verification_token": tokens["access"],
                "site_url": request.build_absolute_uri("/accounts/api/v1"),
            }

            email_thread = EmailThread(
                subject="Verify Your Email",
                template_name="email/verification.tpl",
                context=context,
            )
            email_thread.start()

            return Response(
                {
                    "status": "success",
                    "message": "Verification email sent successfully",
                },
                status=status.HTTP_200_OK,
            )

        except User.DoesNotExist:
            return Response(
                {"status": "error", "message": "User not found"},
                status=status.HTTP_404_NOT_FOUND,
            )


class VerifyEmail(generics.GenericAPIView):
    def get(self, request, token):
        try:
            # Decode token using AccessToken instead of TokenBackend
            token_obj = AccessToken(token)
            user_id = token_obj["user_id"]

            # Get and verify user
            user = User.objects.get(id=user_id)
            if not user.is_verified:
                user.is_verified = True
                user.save()
                return Response(
                    {
                        "status": "success",
                        "message": "Email verified successfully",
                    },
                    status=status.HTTP_200_OK,
                )

            return Response(
                {"status": "error", "message": "Email already verified"},
                status=status.HTTP_400_BAD_REQUEST,
            )

        except (InvalidTokenError, ExpiredSignatureError):
            return Response(
                {"status": "error", "message": "Invalid or expired token"},
                status=status.HTTP_400_BAD_REQUEST,
            )

        except User.DoesNotExist:
            return Response(
                {"status": "error", "message": "User not found"},
                status=status.HTTP_404_NOT_FOUND,
            )

        except Exception as e:
            return Response(
                {"status": "error", "message": str(e)},
                status=status.HTTP_400_BAD_REQUEST,
            )


class ResendVerificationEmail(generics.GenericAPIView):
    serializer_class = EmailVerificationSerializer

    def get_tokens_for_user(self, user):
        refresh = RefreshToken.for_user(user)
        return {
            "refresh": str(refresh),
            "access": str(refresh.access_token),
        }

    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        email = serializer.validated_data["email"]

        try:
            user = User.objects.get(email=email)
            if user.is_verified:
                return Response(
                    {"status": "error", "message": "Email already verified"},
                    status=status.HTTP_400_BAD_REQUEST,
                )

            tokens = self.get_tokens_for_user(user)

            context = {
                "name": user.full_name,
                "email": user.email,
                "verification_token": tokens["access"],
                "site_url": request.build_absolute_uri("/accounts/api/v1"),
            }

            email_thread = EmailThread(
                subject="Verify Your Email",
                template_name="email/verification.tpl",
                context=context,
            )
            email_thread.start()

            return Response(
                {
                    "status": "success",
                    "message": "Verification email sent successfully",
                },
                status=status.HTTP_200_OK,
            )

        except User.DoesNotExist:
            return Response(
                {"status": "error", "message": "User not found"},
                status=status.HTTP_404_NOT_FOUND,
            )
