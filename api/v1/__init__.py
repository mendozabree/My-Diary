from flask import Flask

app = Flask(__name__)


from api.v1.endpoints import entries
from api.v1.endpoints import users
