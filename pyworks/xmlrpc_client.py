# python3
# xmlrpc_client.py - XMLを交換形式としたRPCによる関数を呼び出し(client側)

from xmlrpc.client import ServerProxy

proxy = ServerProxy("http://localhost:6789/")
num = 7
result = proxy.double(num)
print(f"Double {num} is {result}")