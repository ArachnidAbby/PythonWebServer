import socket
import Handlers, Handle_IO
import Configuration as config

Functions = {
    "GET" : Handlers.handle_GET,
    "TRACE" : Handlers.handle_TRACE,
    "HEAD"  : Handlers.handle_HEAD,
    "POST"  : Handlers.handle_POST #Not Implemented Yet
}

config.read_AllConfig()

def changeTo_Redirect(text):
    return text.replace(f" {text.split(' ')[1]} ",f" {config.Redirects[text.split(' ')[1]]} ")

def changeTo_FolderIndex(text):
    if not '.' in text.split(" ")[1]:
        return text.replace(f" {text.split(' ')[1]} ",f" {text.split(' ')[1]}/index.html ")
    return text

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((config.HOST,config.PORT))

while True:
    s.listen()
    conn, addr = s.accept()
    with conn:
        try:
            data = conn.recv(1024).decode()
            dataSplit = data.split("\r\n")
            firstLine = dataSplit[0].split(" ")
            if not firstLine[2]=="HTTP/1.1":
                continue
            if firstLine[0] in config.g_blockedMethods:
                Handle_IO.send_405(conn,firstLine[0])
                continue
            if firstLine[1] in config.Redirects.keys():
                Functions[firstLine[0]](changeTo_Redirect(dataSplit[0]),conn,data)
            else:
                dataSplit[0] = changeTo_FolderIndex(dataSplit[0])
                Functions[firstLine[0]](dataSplit[0],conn,data)
        except:
            Handle_IO.send_404(conn)

s.close()