#createv env file
import requests
import datetime
import base64

client_id = 'f2483274d6744f639231ab05ac8714f7'
client_secret = '518efa1a7b434a44a50e1c5e44674119'

#do tocken lookup

client_creds = f"{client_id}:{client_secret}"

base64_client_creds = base64.b64encode(client_creds.encode())
print(base64_client_creds)

token_url =  'https://accounts.spotify.com/api/token'
method = 'POST'
token_data = {
    "grant_type" : "client_credentials"
}

tocken_header = {
    "Authorization" : f"Basic {base64_client_creds.decode()}"
}

r = requests.post(token_url, data = token_data, headers = token_header)
print(r.json())
tocken_response_data = r.json()

now = datetime.datetime.now()
access_tocken = tocken_response_data['access_token']
expires_in = tocken_response_data['expires_in']
expires = now + datetime.timedelta(seconds = expires_in)
did_expire = expires < now