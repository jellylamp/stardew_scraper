#!/usr/bin/env python3
from flask import Flask, jsonify
import os

app = Flask(__name__)

@app.route('/')
def index():
    return "Hello, World!"

@app.route('/api/v1/maru', methods=['GET'])
def get_maru():
    return jsonify({'maru': 'test'})

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=int(os.environ.get('PORT', 8080)))
