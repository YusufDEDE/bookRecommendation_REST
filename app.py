import os
import re
import json
import nltk
from flask_cors import CORS
from nltk.corpus import stopwords
from werkzeug.utils import secure_filename
from flask import Flask, jsonify, request, url_for

app = Flask(__name__)
CORS(app)

@app.route('/')
def word_test():
    w = request.args['word']
    return jsonify("Hello flask _> ", w)  
   
if __name__ == '__main__':
    app.run(debug=True)