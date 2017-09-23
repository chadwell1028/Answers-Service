from PIL import Image

from screenshotter import Screenshotter
from tempfile import NamedTemporaryFile
from shutil import copyfileobj
from os import remove

from flask import Flask, request

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World!'


@app.route('/test')
def test():
    image = Image.open('File.jpg')
    image.show()
    return "test"


@app.route('/post/<path:path_link>', methods=['GET', 'POST'])
def run_stuff(path_link):
    if request.method == 'POST':
        screenshotter = Screenshotter()
        img = screenshotter.get_image(path_link)

        tempFileObj = NamedTemporaryFile(mode='w+b', suffix='jpg')
        pilImage = open('myfile.jpg', 'rb')
        copyfileobj(pilImage, tempFileObj)
        pilImage.close()
        remove('myfile.jpg')
        tempFileObj.seek(0, 0)

        image = Image.open(tempFileObj)
        image.show()
        # response = send_file(tempFileObj, as_attachment=True, attachment_filename='myfile.jpg')
        return 'response'
