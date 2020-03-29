import unittest
import requests
import json

def create_test_data(email): # emails must be unique!
    headers = {
        "Content-Type": 'application/json'
        }

    data ={"first_name": "Jane",
    "last_name":"Doe",
    "contacted":"Yes they were but they're in quarantine",
    "notes":"test",
    "email": email}

    data = json.dumps(data)
    response = requests.post("http://127.0.0.1:8000/api/v1/leads/", headers=headers, data=data)
    return response

class Tests(unittest.TestCase):
    ''' Make sure to use create_test_data to create test data befoer running the tests'''
    def test_get_all(self):
        # http://127.0.0.1:8000/api/v1/leads/

        headers = {
            "Content-Type": 'application/json'
        }

        response = requests.get("http://127.0.0.1:8000/api/v1/leads/", headers=headers)
        self.assertEqual(response.status_code, 200)

    def test_post_lead(self):
        headers = {
        "Content-Type": 'application/json'
        }

        data ={"first_name": "Jane",
        "last_name":"Doe",
        "contacted":"Yes they were but they're in quarantine",
        "notes":"test",
        "email": "testemail11@gmail.com"}

        data = json.dumps(data)
        response = requests.post("http://127.0.0.1:8000/api/v1/leads/", headers=headers, data=data)
        self.assertEqual(response.status_code, 201)

    def test_update_lead(self):
        headers = {
        "Content-Type": 'application/json'
        }

        data ={"first_name": "Jane",
        "last_name":"Doe",
        "contacted":"Yes they were but they're in quarantine",
        "notes":"test"
        }

        data = json.dumps(data)
        response = requests.put("http://127.0.0.1:8000/api/v1/leads/charlesdsmith2777@gmail.com/", headers=headers, data=data)
        self.assertEqual(response.status_code, 200)

    def test_delete_lead(self):
        headers = {
        "Content-Type": 'application/json'
        }

        response = requests.delete("http://127.0.0.1:8000/api/v1/leads/testemail7@gmail.com/", headers=headers)
        self.assertEqual(response.status_code, 200)

if __name__ == '__main__':
    unittest.main()
    # print(create_test_data("testme@gmail.com"))