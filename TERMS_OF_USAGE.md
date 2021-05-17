# Unmodifed Versions

This software can be used freely when unmodified.

## Things you are not allowed to do with my software:
  - distrubute this software with a price tag attached
  - claim you own this software


-----

# Modified Versions

When distrubuting modifications of this software you must follow a few rules.

## Things you are not allowed to do with my software:
  - distribute modification of this software without giving credit
  - distrubute modifications of this software with a price tag attached
  
## Before Distribution you must:
*Handle_IO.py->send_Header(\*args,\*kwargs)*

You need to change the header that you are sending to specify that you are working with a modified software

change:
```python
conn.send(f'HTTP/1.1 {HTTPCode}\nServer: PythonWebServer/{config.VERSION}\nContent-Type: {ContentType}\nContent-Length: {ContentLength}\nConnection: Closed\n\n'.encode())
```
to:
```python
conn.send(f'HTTP/1.1 {HTTPCode}\nServer: PythonWebServer/{config.VERSION}/MODIFIED\nContent-Type: {ContentType}\nContent-Length: {ContentLength}\nConnection: Closed\n\n'.encode())
```

or to:
```python
conn.send(f'HTTP/1.1 {HTTPCode}\nServer: MYSERVER/{config.VERSION}/PYWS-FORK\nContent-Type: {ContentType}\nContent-Length: {ContentLength}\nConnection: Closed\n\n'.encode())
```
*Replace `MYSERVER` with the name of your new server software*

---

Exceptions can be made easily if you contact me!
