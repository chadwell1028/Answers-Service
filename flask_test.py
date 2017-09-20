from screenshotter import Screenshotter


from flask import Flask, request

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World!'


@app.route('/test')
def test():
    return "test"


@app.route('/post/<path:path_link>', methods=['GET','POST'])
def run_stuff(path_link):
    if request.method == 'POST':
        screenshotter = Screenshotter(path_link)
        return path_link
