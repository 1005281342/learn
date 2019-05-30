import asyncio

import redis
from sanic import Sanic
from sanic.response import json

app = Sanic()


connect = redis.Redis(
    host='127.0.0.1',
    password='',
    port=6379,
    decode_responses=True,
    db=1
)


async def sleep_100():

    from time import sleep
    connect.set('hello', '1')
    sleep(5)
    print(10086)


@app.route('/test', methods=["GET", "POST"])
async def test(req):
    name_list = req.json.get("name")
    if connect.get('hello') != '1':
        asyncio.ensure_future(sleep_100())
    return json({
        "name": name_list,
    })


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=6664)  # , workers=4
