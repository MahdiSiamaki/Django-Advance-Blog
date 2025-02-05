from locust import HttpUser, task, between

class BlogUser(HttpUser):
    wait_time = between(1, 2)  # Wait 1-2 seconds between tasks

    def on_start(self):
        response= self.client.post("/accounts/api/v2/jwt/create/", json={"email": "admin@domain.com", "password": "asdfg123zxv"}).json()
        self.client.headers= {"Authorization": f'Bearer {response.get("access", None)}'}
    
    @task
    def post_list(self):
        self.client.get("/blog/api/v1/posts/")

    @task
    def category(self):
        self.client.get("/blog/api/v1/categories/")