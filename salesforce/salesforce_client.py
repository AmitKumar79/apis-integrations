import os, requests
TOKEN_URL = 'https://login.salesforce.com/services/oauth2/token'

CLIENT_ID = os.getenv('SF_CLIENT_ID', 'ID')
CLIENT_SECRET = os.getenv('SF_CLIENT_SECRET', 'SECRET')
USERNAME = os.getenv('SF_USERNAME', 'USERNAME')
PASSWORD = os.getenv('SF_PASSWORD', 'PASSWORD')

def get_token():
    data = {
        'grant_type': 'password',
        'client_id': CLIENT_ID,
        'client_secret': CLIENT_SECRET,
        'username': USERNAME,
        'password': PASSWORD
    }
    r = requests.post(TOKEN_URL, data=data)
    return r.json()

if __name__ == '__main__':
    print(get_token())
