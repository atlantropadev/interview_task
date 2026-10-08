from typing import Any

import pytest

from interview_task.api_client import BookingClient

pytestmark = pytest.mark.api


def test_list_bookings(booking_client: BookingClient) -> None:
    response = booking_client.list_bookings()
    assert response.ok
    assert all("bookingid" in item for item in response.json())


def test_create_and_get_booking(
    booking_client: BookingClient, booking_payload: dict[str, Any]
) -> None:
    created = booking_client.create_booking(booking_payload)
    assert created.ok
    booking_id = created.json()["bookingid"]

    fetched = booking_client.get_booking(booking_id)
    assert fetched.ok
    assert fetched.json() == booking_payload


def test_update_booking(
    booking_client: BookingClient, booking_payload: dict[str, Any], token: str
) -> None:
    booking_id = booking_client.create_booking(booking_payload).json()["bookingid"]
    updated_payload = booking_payload | {"firstname": "John"}

    response = booking_client.update_booking(booking_id, updated_payload, token)
    assert response.ok
    assert response.json()["firstname"] == "John"


def test_delete_booking(
    booking_client: BookingClient, booking_payload: dict[str, Any], token: str
) -> None:
    booking_id = booking_client.create_booking(booking_payload).json()["bookingid"]

    assert booking_client.delete_booking(booking_id, token).status == 201
    assert booking_client.get_booking(booking_id).status == 404


def test_auth_with_invalid_credentials_returns_no_token(booking_client: BookingClient) -> None:
    assert booking_client.create_token("admin", "wrong") == ""
