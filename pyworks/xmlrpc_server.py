# python3
# xmlrpc_server.py - XMLを交換形式としたRPCによる関数を呼び出し(server側)

from xmlrpc.server import SimpleXMLRPCServer

def double(num):
    return num * 2

server = SimpleXMLRPCServer(("localhost", 6789))
server.register_function(double, "double")
server.serve_forever()