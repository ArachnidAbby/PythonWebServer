import Configuration as config

ContentTypes = {
    "ico" : "image/webp",
    "png" : "image/webp",
    "jpg" : "image/webp",
    "html": "text/html;charset=utf-8",
    "txt" : "plain;charset=utf-8",
    "css" : "text/html;charset=utf-8"
}

def get_ContentType(pageName):
    '''
    get the content type based on the name of a page
    '''
    if not "." in pageName:
        return "text/html"
    return ContentTypes[pageName.split('.')[1]]

def send_Header(HTTPCode, ContentType, ContentLength, conn):
    try:
        conn.send(f'HTTP/1.1 {HTTPCode}\nServer: PythonWebServer/{config.VERSION}\nContent-Type: {ContentType}\nContent-Length: {ContentLength}\nConnection: Closed\n\n'.encode())
    except:
        print("Failed to send HTTP Header")

def send_Page(page, conn, ContentType="text/html", code="200 OK"):
    '''
    page = page content
    conn = socket connection
    '''
    try:
        send_Header(code, ContentType, len(page), conn)
        conn.send(page)
    except:
        print("Connection Aborted: Transaction could not be completed")

def send_RawHeader(header, conn):
    '''
    Send only an HTTP header
    '''
    try:
        conn.send(header.encode())
    except:
        print("Transaction failed")

def send_404(conn):
    '''
    sends a 404 message.
    if PageSrc/404Page.html exists -> show page
    else -> show generic message
    '''
    try:
        with open('PageSrc/404Page.html','rb') as f:
            src = f.read()
            send_Page(src,conn,code="404 Not Found")
    except:
        ERROR_MSG = '''
        <html>
            <head><title>404 PAGE NOT FOUND</title></head>
            <body><h1>404 PAGE NOT FOUND</h1></body>
        </html>
        '''
        send_Page(ERROR_MSG.encode(), conn, code="404 Not Found")

def send_405(conn, method):
    '''
    Sends a 405 Method Not Allowed Status Code
    '''
    try:
        page = f'''
        <html>
            <title405 ERROR</title>
            <h1>This Method is not allowed</h1>
            </h2>Method "{method}" is not allowed on this server!</h2>
        </html>
        '''
        send_Header("405 Method Not Allowed"
                    "text/html;charset=utf-8",
                    len(page), conn)
        conn.send(page.encode())
    except:
        print("Transaction failed")
