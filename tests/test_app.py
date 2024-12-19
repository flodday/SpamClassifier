import requests

def test_check_message_spam():
    url = "http://127.0.0.1:5000/check?message=SIX chances to win CASH!"
    response = requests.get(url)
    assert response.status_code == 200
    assert response.json() == {"resp": True}

def test_check_message_ham():
    url = "http://127.0.0.1:5000/check?message=Hello, how are you?"
    response = requests.get(url)
    assert response.status_code == 200
    assert response.json() == {"resp": False}

def test_check_no_message():
    url = "http://127.0.0.1:5000/check"
    response = requests.get(url)
    assert response.status_code == 400
    assert response.json() == {"error": "No message provided"}
