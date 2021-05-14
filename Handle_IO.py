ContentTypes = {
    "ico" : "image/webp",
    "png" : "image/webp",
    "jpg" : "image/webp",
    "html": "text/html;charset=utf-8",
    "txt" : "plain;charset=utf-8"
}

def get_ContentType(pageName):
    '''
    get the content type based on the name of a page
    '''
    if not "." in pageName:
        return "text/html"
    return ContentTypes[pageName.split('.')[1]]

def send_Page(page,conn,ContentType="text/html"):
    '''
    page = page content
    conn = socket connection
    '''
    try:
        conn.send(f'HTTP/1.1 200 OK\nContent-Type: {ContentType}\nContent-Length: {len(page)}\nConnection: Closed\n\n'.encode())
        conn.send(page)
    except:
        print("Connection Aborted: Transaction could not be completed")

def send_404(conn):
    '''
    sends a 404 message.
    if PageSrc/404Page.html exists -> show page
    else -> show generic message
    '''
    try:
        with open('PageSrc/404Page.html','rb') as f:
            src = f.read()
            conn.send(f'HTTP/1.1 404 Not Found\nContent-Type: text/html;charset=utf-8\nContent-Length: {len(src)}\nConnection: Closed\n\n'.encode())
            conn.send(src)
    except:
        ERROR_MSG = '''
        <html>
            <head><title>404 PAGE NOT FOUND</title></head>
            <body><h1>404 PAGE NOT FOUND</h1></body>
        </html>
        '''
        conn.send(f'HTTP/1.1 404 Not Found\nContent-Type: text/html;charset=utf-8\nContent-Length: {len(ERROR_MSG)}\nConnection: Closed\n\n'.encode())
        conn.send(ERROR_MSG.encode())