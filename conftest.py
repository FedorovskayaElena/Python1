import pytest
from fixture.application import Application

fixture = None


# Создание фикстуры
@pytest.fixture()
def app(request):
    global fixture
    browser = request.config.getoption("--browser")
    baseURL = request.config.getoption("--URL")
    if fixture is None:
        fixture = Application(browser, baseURL)
    else:
        if not fixture.is_valid():
            fixture = Application(browser, baseURL)
    fixture.session.ensure_login("admin", "secret")
    return fixture


# Отдельная фикстура для финализации
@pytest.fixture(scope="session", autouse=True)
def stop(request):
    def fin():
        fixture.session.ensure_logout()
        fixture.destroy()
    request.addfinalizer(fin)
    return fixture


def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="Firefox")
    parser.addoption("--URL", action="store", default="http://localhost/addressbook/")
