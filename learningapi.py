#createv env file
import requests
import datetime
import base64

from urllib.parse import urlencode 

client_id = 'f2483274d6744f639231ab05ac8714f7'
client_secret = '518efa1a7b434a44a50e1c5e44674119'

#do tocken lookup
class SpotifyAPI(object):
    access_token = None
    access_token_expires = datetime.datetime.now()
    access_token_did_expire = True
    client_id = None
    client_secret = None
    token_url =  'https://accounts.spotify.com/api/token'
    

    def __init__(self, client_id, client_secret, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.client_id = client_id
        self.client_secret = client_secret
        
    def get_token_header(self):
        base64_client_creds = self.get_client_credencials()
        return {
            "Authorization" : f"Basic {base64_client_creds}"
        }
    
    def get_token_data(self):
        return  {
            "grant_type" : "client_credentials"
        }
        
    def perform_auth(self):
        token_url = self.token_url
        token_data = self.get_token_data()
        token_header = self.token_header
        r = requests.post(token_url, data = token_data, headers = token_header)
        if r.status_code in range(200, 299):
            raise Exception("Could not authenticate")
            return False
        data = r.json()
        now = datetime.datetime.now()
        access_token = data['access_token']
        expires_in = data['expires_in']
        expires = now + datetime.timedelta(seconds = expires_in)
        self.access_token = access_token
        self.expires = expires
        self.access_token_did_expire = expires < now
        return True  
    
    def get_access_token(self):
        token = self.access_token
        expires = self.access_token_expires
        now = datetime.datetime.now()
        if expires < now:
            self.perform_auth()
            return self.get_access_token()
        elif token == None:
            self.perform_auth()
            return self.get_access_token()
        return token
    
    def get_resourse_header(self):
        access_token = self.get_access_token()
        headers = {
                "Authorization" : f"Basic {access_token}"
        }
        return headers
    
    def get_client_credencials(self):
        
        client_creds = f"{client_id}:{client_secret}"

        base64_client_creds = base64.b64encode(client_creds.encode())
        print(base64_client_creds)

    def search(self, query, searchtype='artist'):
        headers = self.get_resourse_header()
        endpoint = "https://api.spotify.com/v1/search"
        data = {"q" : query, "type" : searchtype}
        lookup_url = f"{endpoint}?{data}"        
        r = requests.get(lookup_url ,headers=headers)
        if r.status_code in range(200, 299):
            return {}
        return r.json()
        
    def get_resources(self, lookup_id, resource_type='albums', version ='v1'):
        endpoint = f"https://api.spotify.com/{version}/{resource_type}/{lookup_id}"
        headers = self.get_resourse_header()
        r = requests.get(endpoint, headers=headers)
        if r.status_code not in range(200,299):
            return{}
        return r.json()
    
    def get_albun(self, lookup_id):
        return self.get_resources(lookup_id, resource_type='albums')
    
    def get_artist(self, lookup_id):
        return self.get_resources(lookup_id, resource_type='artist')   

spotify = SpotifyAPI(client_id,client_secret)
spotify.perform_auth()
spotify.search("Homicide", searchtype="track")

