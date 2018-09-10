from tensorflow.contrib.keras.python.preprocessing import image
from tensorflow.contrib.keras.python.keras.applications.inception_v3 import *
import os
import sys
from flask import Flask, render_template, request
import json

app = Flask(__name__)

model = InceptionV3(weights='imagnent')

@app.route("/detect", methods=["GET", "POST"])
def detect():
    