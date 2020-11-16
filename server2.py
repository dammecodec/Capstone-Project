from flask import Flask, request, Response, jsonify
import jsonpickle
import numpy as np
import cv2
from PIL import Image as im
host = '10.72.34.120'
port = 2402
tmp = True
app = Flask(__name__)
@app.route('/post', methods = ['POST'])
def receive():
    r = request
    nparr = np.frombuffer(r.data,np.uint8)
    img = cv2.imdecode(nparr, cv2.IMREAD_GRAYSCALE)
    im1 = im.fromarray(img)
    im1.save('tung1.jpg')
    response = {'message': 'image received. size={}x{}'.format(img.shape[1], img.shape[0])}
    response_pickled = jsonpickle.encode(response)
    return Response(response=response_pickled, status=200, mimetype="application/json")
@app.route('/command', methods = ['GET'])
def command():
    if tmp == True:
        return jsonify('ok')
    else:
        return 0
app.run(host,port)
