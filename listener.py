import socket
import time

HOST = 'localhost'
PORT = 3000

s = socket.socket()
s.bind((HOST, PORT))
print(f"Aguardando conexão na porta: {PORT}")

s.listen(5)
conn, address = s.accept()

print(f"Recebendo solicitação de {address}")

messages = [
    'Mensagem A',
    'Mensagem B',
    'Mensagem C',
    'Mensagem D',
    'Mensagem E',
    'Mensagem F',
    'Mensagem G'
]

for message in messages:
    message = bytes(message, 'utf-8')
    conn.send(message)
    time.sleep(4)

conn.close()