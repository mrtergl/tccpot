import logging
import threading
from socket import socket

BIND_IP = "0.0.0.0"


class TcpPot:

    def __init__(self, ports, log_filepath):
        self.ports = ports
        self.log_filepath = log_filepath
        self.listener_threads = {}

        if len(self.ports) < 1:
            raise Exception("No ports provided")

        logging.basicConfig(filename=log_filepath,
                            encoding='utf-8',
                            level=logging.DEBUG,
                            filemode="w",
                            format="%(asctime)s %(levelname)-8s %(message)s",
                            datefmt="%d-%m-%Y %H:%M")
        self.logger = logging.getLogger(__name__)
        self.logger.info("TCPPOT initializing")
        self.logger.info("[*] Ports: %s" % self.ports)
        self.logger.info("[*] Logfile: %s" % self.log_filepath)

    def handle_connection(self,client_socket,port, ip, remote_port):
        data = client_socket.recv(64)
        self.logger.info("{{*}} Accepted Connection from {0}:{1} - {2}".format(ip, remote_port, data))
        client_socket.send("Access denied.\n".encode('utf-8'))
        client_socket.close()

    def start_new_listener_thread(self,port):
        listener = socket()
        listener.bind((BIND_IP, int(port)))
        listener.listen(5)
        # 5 stands for it is acceptable 5 different connections are requested at the same time
        # and added to que to listen. MAX 5 MIN 1
        while True:
            client, addr = listener.accept()
            client_handler = threading.Thread(target=self.handle_connection, args=(client, addr[0], addr[1]))
            client_handler.start()

    def start_listening(self):
        for port in self.ports:
            """Create a new listener for each port"""
            self.listener_threads[port] = threading.Thread(target=self.start_new_listener_thread,args=(port,))
            self.listener_threads[port].start()

    def run(self):
        self.start_listening()




