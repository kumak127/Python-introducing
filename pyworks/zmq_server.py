# python3
# zmq_server.py - ZeroMQのソケットを使ったデータのやり取り(server側)

import zmq

host = "127.0.0.1"
port = 6789
context = zmq.Context()
server = context.socket(zmq.REP)
server.bind(f"tcp://{host}:{port}")
while True:
    # Wait for next request from client
    request_str = server.recv().decode("utf-8")
    print(f"That voice in my head says: {request_str}")
    reply_bytes = f"Stop saying: {request_str}".encode("utf-8")
    server.send(reply_bytes)