# quick api tester
import requests

def test_endpoint(url, method='GET', data=None):
    try:
        if method == 'GET':
            r = requests.get(url)
        elif method == 'POST':
            r = requests.post(url, json=data)
        
        print(f"Status: {r.status_code}")
        print(f"Response: {r.json()}")
        return r
    except Exception as e:
        print(f"Error: {e}")

# testing
if __name__ == "__main__":
    # test_endpoint("https://api.github.com/users/octocat")
    # test_endpoint("https://jsonplaceholder.typicode.com/posts/1")
    pass
