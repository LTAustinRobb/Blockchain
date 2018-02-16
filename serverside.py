import socket


def main():
    host = '127.0.0.1'
    port = 5000

    s = socket.socket()
    s.bind((host, port))

    s.listen(1)
    c, addr = s.accept()
    blockchain = []

    print "connection from: " + str(addr)

    while True:
        data = c.recv()
        if len(data) < len(blockchain):
            c.send(blockchain)
        else:
            blockchain = data
            c.send(blockchain)

    c.close()


if __name__ == '__main__':
    main()





