import requests

BASE_URL = "http://127.0.0.1:8000"

def test_generate_reply():
    """ test /generate_reply/ API """
    data = {"text": "What do you think about AI?"}
    response = requests.post(f"{BASE_URL}/generate_reply/", json=data)

    assert response.status_code == 200  # making sure the request was successful
    assert "reply" in response.json()  # makeing sure JSON contains 'reply' 

if __name__ == "__main__":
    test_generate_reply()
    print("✅ API test passed！")
