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

def main():
    
    ram = [1] * 16
    cu = CU("intel", "2019-08-16", "manage everything", ram, 2.4, True)

    code = open("../Programs/Program0.code", "r")
    codelines = code.readlines()

    cu.startInstructions(codelines)

    response = {
      "registers":{
        "A": cu.a.getData(),
        "B": cu.b.getData(),
        "C": cu.c.getData(),
        "D": cu.d.getData()
        },
      "RAM": cu.ram.getRAM(),
      "CLOCK":cu.clock.freq,
      "ALU":cu.alu.getFlags()
    }

    y = json.dumps(response)

    @app.route("/")
    def hello():
        return y

if __name__== "__main__":
  main()
  app.run(host= '0.0.0.0')