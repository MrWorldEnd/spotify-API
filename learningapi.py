client_id = 'f2483274d6744f639231ab05ac8714f7'
client_secret = '518efa1a7b434a44a50e1c5e44674119'

#do tocken lookup

client_creds = f"{client_id}:{client_secret}"

tocken_url =  'https://accounts.spotify.com/api/token'
method = 'POST'
token_data = {
    "grant_type" : "client_credentials"
}

tocken_header = {
    "Authorization" : f"Basic {client_creds}"
}