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
    INGESTION_SOCKET_BYTES = 16

    CONTRIBUTION_CODE_INT = 1
    UPDATE_CODE_INT = 2
    REMOVE_CODE_INT = 3

    @staticmethod
    def send_contribution_packet(ingestion_socket, contribution_id) -> None:
        
        # send request
        request = struct.pack('iifi', IngestionSocketFunctions.CONTRIBUTION_CODE_INT, 
            contribution_id, 0, 0)
        ingestion_socket.sendall(request)

        # receive response
        response = ingestion_socket.recv(IngestionSocketFunctions.INGESTION_SOCKET_BYTES)
        if struct.unpack('')

    @staticmethod
    def send_update_packet(ingestion_socket) -> None:
        pass

    @staticmethod
    def send_remove_packet(ingestion_socket) -> None:
        pass

class MatchSocketFunctions:
    MATCH_SOCKET_BYTES = 12

    @staticmethod
    def send_match_packet(match_socket) -> tuple:

        # send request
        request = struct.pack('iii', PACKET_DIR_ACK_INT, 0, 0)
        match_socket.sendall(request)

        # receive response
        response = match_socket.recv(MatchSocketFunctions.MATCH_SOCKET_BYTES)
        struct_resp = struct.unpack('iII', response)
        if struct_resp[0] == 2: return None
        else: return (struct_resp[1], struct_resp[2])

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
        struct_resp = struct.unpack('ii', response)
        if not struct_resp[0]: return None
        elif struct_resp[0] == 1: return ('below', struct_resp[1])
        elif struct_resp[0] == 2: return ('above', struct_resp[1])

    @staticmethod
    def send_alive_packet(control_socket) -> None:

        # send request
        request = struct.pack('ii', ControlSocketFunctions.ALIVE_CODE_INT,
            PACKET_DIR_ACK_INT)  
        control_socket.sendall(request)

        # receive response
        response = control_socket.recv(ControlSocketFunctions.CONTROL_SOCKET_BYTES)
        if struct.unpack('ii', response)[0] != PACKET_DIR_ACK_INT: raise RuntimeError