# python3 
# zmq_client.py - ZeroMQのソケットを使ったデータのやり取り(client側)

import zmq

host = "127.0.0.1"
port = 6789
context = zmq.Context()
client = context.socket(zmq.REQ)
client.connect(f"tcp://{host}:{port}")
for num in range(1,6):
    request_str = f"message {num}"
    request_bytes = request_str.encode("utf-8")
    client.send(request_bytes)
    reply_str = client.recv().decode("utf-8")
    print(f"Send {request_str}, received {reply_str}")