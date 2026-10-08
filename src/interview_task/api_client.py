from typing import Any

from playwright.sync_api import APIRequestContext, APIResponse

from interview_task.config import API_PASSWORD, API_USERNAME


class BookingClient:
    def __init__(self, request: APIRequestContext) -> None:
        self.request = request

    def create_token(self, username: str = API_USERNAME, password: str = API_PASSWORD) -> str:
        response = self.request.post("/auth", data={"username": username, "password": password})
        return response.json().get("token", "")

    def list_bookings(self, **filters: str) -> APIResponse:
        return self.request.get("/booking", params=filters)

    def get_booking(self, booking_id: int) -> APIResponse:
        return self.request.get(f"/booking/{booking_id}")

    def create_booking(self, payload: dict[str, Any]) -> APIResponse:
        return self.request.post("/booking", data=payload)

    def update_booking(self, booking_id: int, payload: dict[str, Any], token: str) -> APIResponse:
        return self.request.put(
            f"/booking/{booking_id}", data=payload, headers={"Cookie": f"token={token}"}
        )

    def delete_booking(self, booking_id: int, token: str) -> APIResponse:
        return self.request.delete(f"/booking/{booking_id}", headers={"Cookie": f"token={token}"})
