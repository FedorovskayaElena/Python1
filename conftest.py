import pytest
from fixture.application import Application
from fixture.db import DBFixture
import json
import jsonpickle
import os.path
import importlib

fixture = None
target = None


def load_config(file):
    global target
    if target is None:
        config_file = os.path.join(os.path.dirname(os.path.abspath(__file__)), file)
        with open(config_file) as cf:
            target = json.load(cf)
    return target


# Создание фикстуры
@pytest.fixture()
def app(request):
    global fixture
    browser = request.config.getoption("--browser")
    web_config = load_config(request.config.getoption("--target"))["web"]
    if fixture is None or not fixture.is_valid():
        fixture = Application(browser, web_config["baseURL"])
    fixture.session.ensure_login(web_config["login"], web_config["password"])
    return fixture


# Отдельная фикстура для базы данных
@pytest.fixture(scope="session")
def db(request):
    db_config = load_config(request.config.getoption("--target"))["db"]
    dbFixture = DBFixture(host=db_config["host"], database=db_config["database"],
                          user=db_config["user"], password=db_config["password"])
    def fin():
        dbFixture.destroy()
    request.addfinalizer(fin)
    return dbFixture


# Отдельная фикстура для финализации
@pytest.fixture(scope="session", autouse=True)
def stop(request):
    def fin():
        fixture.session.ensure_logout()
        fixture.destroy()
    request.addfinalizer(fin)
    return fixture


# Фикстура для получения параметра check_ui
@pytest.fixture(scope="session")
def check_ui(request):
    return request.config.getoption("--check_ui")


def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="Firefox")
    parser.addoption("--target", action="store", default="target.json")
    parser.addoption("--check_ui", action="store_true")


def pytest_generate_tests(metafunc):
    for fixture in metafunc.fixturenames:
        if fixture.startswith("data_"):
            testdata = load_from_module(fixture[5:])
            metafunc.parametrize(fixture, testdata, ids=[str(x) for x in testdata])
        elif fixture.startswith("json_"):
            testdata = load_from_json(fixture[5:])
            metafunc.parametrize(fixture, testdata, ids=[str(x) for x in testdata])


def load_from_module(module):
    return importlib.import_module("data.%s" % module).testdata


def load_from_json(module):
    testdata = []
    with open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "data/%s.json" % module)) as file:
        testdata = jsonpickle.decode(file.read())
    return testdata