from sqladmin.authentication import AuthenticationBackend
from starlette.requests import Request

from config.settings import NAME_ADMIN, PASSWORD
class AdminAuth(AuthenticationBackend):
    async def login(self, request: Request) -> bool:
        form = await request.form()
        username = form.get("username")
        password = form.get("password")

        # лучше взять из .env
        if username == NAME_ADMIN and password == PASSWORD:
            request.session.update({"token": "ok"})
            return True
        return False

    async def logout(self, request: Request) -> bool:
        request.session.clear()
        return True

    async def authenticate(self, request: Request) -> bool:
        return request.session.get("token") == "ok"
