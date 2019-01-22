from sanic import Sanic
from sanic.response import json

app = Sanic()


@app.route('/test', methods=["GET", "POST"])
def test(req):

    name_list = req.json.get("name")
    data = req.raw_args.get("data")
    return json({
        "name": name_list,
        "data": data
    })


if __name__ == '__main__':

    app.run(host='0.0.0.0', port=6664)  # , workers=4
