from flask import Flask
from socket import gethostbyname, gaierror

application = Flask(__name__)

@application.route("/")
def hello():
    try:
      abc = "Host '1234.lev.iot.ilab.cloud' has address "
      abc += gethostbyname('1234.lev.iot.ilab.cloud')
    except gaierror:
      abc = "Address not found"
    except e:
      abc = "General Error 1"

    return abc

if __name__ == "__main__":
    application.run()
