import Handle_IO
def handle_GET(request, conn):
    splitRequest = request.split(" ")
    with open("PageSrc"+splitRequest[1],"rb") as f:
        Handle_IO.send_Page(f.read(),conn, ContentType = Handle_IO.get_ContentType(splitRequest[1]))