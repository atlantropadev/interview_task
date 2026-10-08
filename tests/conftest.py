from collections.abc import Iterator
from typing import Any

import pytest
from playwright.sync_api import APIRequestContext, Page, Playwright

from interview_task.api_client import BookingClient
from interview_task.config import API_BASE_URL, PASSWORD, STANDARD_USER
from interview_task.pages import InventoryPage, LoginPage


@pytest.fixture(scope="session")
def api_request(playwright: Playwright) -> Iterator[APIRequestContext]:
    context = playwright.request.new_context(
        base_url=API_BASE_URL,
        extra_http_headers={"Accept": "application/json"},
    )
    yield context
    context.dispose()


@pytest.fixture(scope="session")
def booking_client(api_request: APIRequestContext) -> BookingClient:
    return BookingClient(api_request)


@pytest.fixture(scope="session")
def token(booking_client: BookingClient) -> str:
    return booking_client.create_token()


@pytest.fixture
def booking_payload() -> dict[str, Any]:
    return {
        "firstname": "Jane",
        "lastname": "Tester",
        "totalprice": 150,
        "depositpaid": True,
        "bookingdates": {"checkin": "2026-01-01", "checkout": "2026-01-05"},
        "additionalneeds": "Breakfast",
    }


@pytest.fixture
def login_page(page: Page) -> LoginPage:
    login = LoginPage(page)
    login.open()
    return login


@pytest.fixture
def inventory_page(login_page: LoginPage) -> InventoryPage:
    login_page.login(STANDARD_USER, PASSWORD)
    return InventoryPage(login_page.page)
