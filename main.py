# coding:utf-8
# See PyCharm help at https://www.jetbrains.com/help/pycharm/


from demo.server import app
import uvicorn

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    uvicorn.run(app=app,
                host="127.0.0.1",
                port=8000, debug=True,
                log_level="info")


