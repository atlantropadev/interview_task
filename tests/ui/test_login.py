import re

import pytest
from playwright.sync_api import expect

from interview_task.config import LOCKED_OUT_USER, PASSWORD, STANDARD_USER
from interview_task.pages import LoginPage

pytestmark = pytest.mark.ui


def test_standard_user_can_log_in(login_page: LoginPage) -> None:
    login_page.login(STANDARD_USER, PASSWORD)
    expect(login_page.page).to_have_url(re.compile(r"/inventory\.html$"))


def test_locked_out_user_sees_error(login_page: LoginPage) -> None:
    login_page.login(LOCKED_OUT_USER, PASSWORD)
    expect(login_page.error).to_contain_text("locked out")
