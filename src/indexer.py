import csv
import socket
HOST = 'localhost'
PORT = 3000 

with open('data/ml-100k.csv', newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        if(row['rating'] > 3):
            payload = bytearray("HTTP GET /item/{1}/user/{2}".format(row['movieId'], row['userId']),'UTF-8') 
            # Simulate multiples connections 
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect((HOST, PORT))
            s.sendall(payload) 
            s.close()
