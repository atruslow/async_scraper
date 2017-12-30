
import asyncio
import zmq
from zmq.asyncio import Context
from scraper.constants import constants

ctx = Context.instance()
pub_socket = ctx.socket(zmq.PUB)
pub_socket.bind(constants.URL_PUB_HOST)

sub_socket = ctx.socket(zmq.SUB)
sub_socket.connect(constants.URL_SUB_HOST)
sub_socket.setsockopt(zmq.SUBSCRIBE, b'')


async def recv():

    while True:
        msg = await sub_socket.recv_json()
        print('received', msg['url'])
        print('sending back')
        await publish(msg['url'])

    socket.close()


async def publish(url):

    await pub_socket.send_json({'scraper_url': url})


def main():
    loop = asyncio.get_event_loop()
    loop.run_until_complete(recv())
    loop.close()


if __name__ == "__main__":
    main()
