import os
import io
import numpy as np
from PIL import Image
import base64

import tensorflow as tf

from flask import Flask, request, redirect, jsonify, render_template

app = Flask(__name__)


#get element id
@app.route('/', methods=['post'])
def signup():
    email = request.form['text']

    return redirect('/')



@app.route('/')
def run():
    return render_template('index.html')


if __name__ == "__main__":

    app.run(debug=True)


