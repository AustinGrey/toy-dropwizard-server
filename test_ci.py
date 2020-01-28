import requests
import pytest # have to install via command "pip3 install -U pytest"

def test_health_check():
    r = requests.get('http://localhost:8085')
    assert(r.status_code == 404)

# 1. Add two more tests here of your choice. I will explain the API.
#    Make sure to verify the necessary info, e.g., status code, response data.
# 2. Add "pytest" as integration testing script as part of Github Actions CI workflow (you've done this before!)

def test_hello_world():
    r = requests.get('http://localhost:8085/hello-world')
    assert(r.status_code == 200)
    assert(r.json()['content'] == 'Hello, Stranger!')

def test_id_counter():
    r1 = requests.get("http://localhost:8085/hello-world")
    r2 = requests.get("http://localhost:8085/hello-world")
    try:
        r1 = r1.json()
        r2 = r2.json()
    except:
        assert(False)

    # print(r1)
    # print(r2)
    assert(r1['id'] + 1 == r2['id'])