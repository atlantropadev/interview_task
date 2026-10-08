# interview_task

Starter package for test automation interviews: pytest + Playwright tests against public targets.

- UI: [Sauce Demo](https://www.saucedemo.com)
- API: [Restful-Booker](https://restful-booker.herokuapp.com/apidoc/index.html)

## Setup

Requires Python 3.14+.

```bash
python3.14 -m venv .venv && source .venv/bin/activate
pip install -e ".[dev]"
playwright install chromium
```

## Run

```bash
pytest              # all tests
pytest -m ui        # frontend only
pytest -m api       # API only
pytest --headed     # watch the browser
ruff check . && ruff format --check .
```
