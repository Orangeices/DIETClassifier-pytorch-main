# -*- coding:utf-8 -*-
from sanic import Sanic, response, request
from sanic.response import text

app = Sanic("My Hello, world app")


@app.get("/")
async def hello_world(request):
    return text("Hello, world.")


@app.route('/test', methods=['GET', 'POST'])
async def justTest(request):
    return text("Hello, world.")


if __name__ == '__main__':
    app.config["password"] = '123'
    app.run(host="0.0.0.0", port=8888)

