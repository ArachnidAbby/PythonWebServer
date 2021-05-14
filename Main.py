import socket
import Handlers, Handle_IO
HOST = "localhost"
PORT = 1300

Functions = {
    "GET" : Handlers.handle_GET
}

Redirects = {
    "/" : "/index.html"
}

def changeTo_Redirect(text):
    splitText = text.split(" ")
    return splitText[0]+" "+Redirects[splitText[1]]+" "+splitText[2]


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST,PORT))
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
            if firstLine[1] in Redirects.keys():
                Functions[firstLine[0]](changeTo_Redirect(dataSplit[0]),conn)
            else:
                Functions[firstLine[0]](dataSplit[0],conn)
        except:
            Handle_IO.send_404(conn)

s.close()