from flask import Flask
import socket

application = Flask(__name__)

@application.route("/")
def hello():
    try:
      abc = socket.gethostbyname('12345678.lev.iot.ilab.cloud')
    except:
      abc = "ERROR"
    return abc

if __name__ == "__main__":
    application.run()
