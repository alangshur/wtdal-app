import socket
import sys
import struct

PACKET_DIR_ACK_INT = 1
PACKET_DIR_NAK_INT = 2 

def build_adapter_sockets() -> tuple:
    try:

        # define engine controllers
        ingestion_engine_addr = ('localhost', 9000)
        match_engine_addr = ('localhost', 9001)
        control_engine_addr = ('localhost', 9002)

        # create TCP/IP sockets
        ingestion_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        match_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        control_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        # bind controller sockets
        ingestion_sock.connect(ingestion_engine_addr)
        match_sock.connect(match_engine_addr)
        control_sock.connect(control_engine_addr)
        return True, ingestion_sock, match_sock, control_sock

    except Exception as e:
        print("Error building adapter: {}".format(e))
        return False, None, None, None

class IngestionSocketFunctions:
    pass

class MatchSocketFunctions:
    pass

class ControlSocketFunctions:
    CONTROL_SOCKET_BYTES = 8

    SHUTDOWN_CODE_INT = 1
    OUTLIER_CODE_INT = 2
    ALIVE_CODE_INT = 3

    @staticmethod
    def send_shutdown_packet(control_socket) -> None:

        # send request
        request = struct.pack('ii', ControlSocketFunctions.SHUTDOWN_CODE_INT,
            PACKET_DIR_ACK_INT)  
        control_socket.sendall(request)

        # receive response
        response = control_socket.recv(ControlSocketFunctions.CONTROL_SOCKET_BYTES)
        if struct.unpack('ii', response)[0] != PACKET_DIR_ACK_INT: raise RuntimeError

    @staticmethod
    def send_outlier_packet(control_socket) -> tuple:

        # send request
        request = struct.pack('ii', ControlSocketFunctions.OUTLIER_CODE_INT,
            PACKET_DIR_ACK_INT)  
        control_socket.sendall(request)

        # receive response
        response = control_socket.recv(ControlSocketFunctions.CONTROL_SOCKET_BYTES)
        return struct.unpack('ii', response)

    @staticmethod
    def send_alive_packet(control_socket) -> None:

        # send request
        request = struct.pack('ii', ControlSocketFunctions.ALIVE_CODE_INT,
            PACKET_DIR_ACK_INT)  
        control_socket.sendall(request)

        # receive response
        response = control_socket.recv(ControlSocketFunctions.CONTROL_SOCKET_BYTES)
        if struct.unpack('ii', response)[0] != PACKET_DIR_ACK_INT: raise RuntimeError