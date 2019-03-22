import requests

URL = "http://192.168.0.100/login"
creds = "admin"

resp = requests.post(URL, "login=%(creds)s&password=%(creds)s" % {'creds': creds}, allow_redirects=False)
print(resp.headers.get('Location'))
