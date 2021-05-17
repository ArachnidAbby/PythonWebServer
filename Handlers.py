import Handle_IO

def handle_GET(request, conn, fullRequest):
    '''
    handles GET method request
    '''
    splitRequest = request.split(" ")
    with open("PageSrc"+splitRequest[1],"rb") as f:
        Handle_IO.send_Page(f.read(),conn, ContentType = Handle_IO.get_ContentType(splitRequest[1]))

def handle_POST(request, conn, fullRequest):
    pass

def handle_HEAD(request, conn, fullRequest):
    '''
    Handles HEAD request
    '''
    splitRequest = request.split(" ")
    with open("PageSrc"+splitRequest[1],"rb") as f:
        Handle_IO.send_Header("200 OK",Handle_IO.get_ContentType(splitRequest[1]),len(f.read()),conn)

def handle_PUT(request, con, fullRequest):
    pass

def handle_DELETE(request, conn, fullRequest):
    pass

def handle_TRACE(request, conn, fullRequest):
    '''
    send back original packet
    '''
    Handle_IO.send_Page(fullRequest.encode(),conn, ContentType="message/http")