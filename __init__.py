from flask import Flask


app = Flask(__name__)

from protetto import routes
