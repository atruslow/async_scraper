import zmq
import time

ctx = zmq.Context()
pub_socket = ctx.socket(zmq.PUB)
pub_socket.bind("tcp://*:5570")

sub_socket = ctx.socket(zmq.SUB)
sub_socket.connect("tcp://scraper:5560")
sub_socket.setsockopt(zmq.SUBSCRIBE, b'')

time.sleep(1)
while True:
    time.sleep(1)
    print('Sending')
    pub_socket.send_json({
        'url': "https://roll20.net/compendium/dnd5e/"
    })

    print('publisher got:', sub_socket.recv_json())
