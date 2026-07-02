import pytest
from utils.logger import logger

@pytest.fixture(scope="function")
def page(playwright):
    logger.info("========== TEST STARTED ==========")
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()

    yield page

    context.close()
    browser.close()
    logger.info("TEST FINISHED")

@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()

    if report.when == "call":
        if report.passed:
            logger.info("========== TEST PASSED ==========")

        elif report.failed:
            logger.error("========== TEST FAILED ==========")
            logger.error(report.longreprtext)