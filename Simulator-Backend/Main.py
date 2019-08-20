from CU import CU
from flask import Flask
from flask_cors import CORS
import json 

app = Flask(__name__)
CORS(app)

response = {
  "message": "Hello World"
}

# convert into JSON:
y = json.dumps(response)

@app.route("/")
def hello():
    return y

def main():
    ram = [1] * 16
    cu = CU("intel", "2019-08-16", "manage everything", ram, 1.2, True)

    code = open("../.code", "r")
    codelines = code.readlines()

    cu.startInstructions(codelines)
if __name__== "__main__":
  main()
  app.run(debug=True)