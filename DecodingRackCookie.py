import requests
import base64
from urllib.parse import unquote
import marshal
import pprint as pp
import re

URL = "http://192.168.0.100/login"
creds = "test"

resp = requests.post(URL, "login=%(creds)s&password=%(creds)s" % {'creds': creds}, allow_redirects=False)
c = resp.headers.get('Set-Cookie')

#Выберем значение cookie, для этого возьмем ее между символами = и ;
c = c.split("=")[1].split("; ")[0]
cookie, signature = c.split("--")

decoded =  base64.b64decode(unquote(cookie))

str_with_bytes = str(decoded)
str_with_bytes = re.sub(r"\\x\d{,2}", "", str_with_bytes)
str_with_bytes = str_with_bytes.replace("b'", "")
str_with_bytes = str_with_bytes.replace(str_with_bytes[0], "")
decoded = str_with_bytes.encode('utf-8')

object = marshal.loads(decoded)
pp.pprint(object)