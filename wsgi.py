from flask import Flask
from socket import gethostbyname, gaierror

application = Flask(__name__)

@application.route("/")
def hello():
    try:
      abc = socket.gethostbyname('12345678.lev.iot.ilab.cloud')
    except gaierror:
      abc = "Address not found"
    except:
      abc = "General Error 1"

    return abc

if __name__ == "__main__":
    application.run()
