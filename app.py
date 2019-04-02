"""
Flask entry point
"""

from flask import Flask

app = Flask(__name__)

@app.route('/listing', methods=['POST'])
def listing():
    return 'OK'

@app.route('/health', methods=['GET'])
def health():
    return 'OK'
