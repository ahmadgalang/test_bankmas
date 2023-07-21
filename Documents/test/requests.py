import requests

base_url = "https://reqres.in/api/users"

def create_user():
    endpoint = base_url
    headers = {'Content-Type': 'application/json'}
    payload = {
        "name": "John Doe",
        "job": "Software Engineer"
    }

    response = requests.post(endpoint, json=payload, headers=headers)
    assert response.status_code == 201, f"Create User Test Failed. Expected: 201, Actual: {response.status_code}"
    print("Create User Test Passed and Response Code:", response.status_code)
    user_id = response.json()["id"]
    return user_id

def update_user():
    user_id = create_user()
    endpoint = f"{base_url}/{user_id}"
    headers = {'Content-Type': 'application/json'}
    payload = {
        "name": "John Doe Jr.",
        "job": "Senior Software Engineer"
    }

    response = requests.put(endpoint, json=payload, headers=headers)
    assert response.status_code == 200, f"Update User Test Failed. Expected: 200, Actual: {response.status_code}"
    print("Update User Test Passed and Response Code:", response.status_code)

def delete_user():
    user_id = create_user()
    endpoint = f"{base_url}/{user_id}"

    response = requests.delete(endpoint)
    assert response.status_code == 204, f"Delete User Test Failed. Expected: 204, Actual: {response.status_code}"
    print("Delete User Test Passed and Response Code:", response.status_code)

if __name__ == "__main__":
    print("Running API Tests...")
    create_user()
    update_user()
    delete_user()