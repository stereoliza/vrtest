import os, sys
from http.server import HTTPServer, CGIHTTPRequestHandler
webdir = r'C:\Users\drovv\AppData\Local\Programs\Python\Python38\vr' # место, где находятся файлы html и подкаталог cgi-bin
port = 80 # по умолчанию http://localhost/, иначе используйте
 # http://localhost:xxxx/
os.chdir(webdir) # перейти в корневой каталог HTML
srvraddr = ("", port) # имя хоста и номер порта
srvrobj = HTTPServer(srvraddr, CGIHTTPRequestHandler)
srvrobj.serve_forever() # запустить как бесконечный фоновый процесс 
