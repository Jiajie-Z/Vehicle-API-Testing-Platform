class VehicleApiClient:
    def __init__(self, session) -> None:
        self.session = session
        self.token: str | None = None

    def login(self, username: str, password: str):
        response = self.post(
            "/api/auth/login",
            json={"username": username, "password": password},
            auth_required=False,
        )

        if response.status_code == 200:
            self.token = response.json()["token"]

        return response

    def get(self, path: str, auth_required: bool = True):
        return self.session.get(
            path,
            headers=self._headers(auth_required),
        )

    def post(self, path: str, json: dict, auth_required: bool = True):
        return self.session.post(
            path,
            json=json,
            headers=self._headers(auth_required),
        )

    def _headers(self, auth_required: bool) -> dict[str, str]:
        headers = {"Content-Type": "application/json"}

        if auth_required and self.token:
            headers["Authorization"] = f"Bearer {self.token}"

        return headers
