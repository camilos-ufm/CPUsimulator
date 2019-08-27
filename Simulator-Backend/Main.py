from CU import CU
from Response import Response
from Bios import Bios
from flask import Flask,request
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
    responses = Response()
    bios = Bios()
    yml = open("../bios.yml", "r")
    ymlines = yml.readlines()
    bios.setValues(ymlines)
    print(bios.clock)
    print(bios.visualization)
    print(bios.ram)
    #ram = [1] * 16
    cu = CU("intel", "2019-08-16", "manage everything", bios.ram, bios.clock, True)

    code = open("../Programs/Program4.code", "r")
    codelines = code.readlines()
    print(codelines)
    cu.run(codelines)

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
    responses.setResponse(y)

    @app.route('/')
    def hello():
        return responses.getResponse()

    @app.route('/post', methods=['POST'])
    def hello1():
        if 'file' not in request.files:
            print("no file")

        file = request.files['file']
        print(file)
        codelines = []
        filestream = file.stream.readlines()
        print(filestream)
        for i in filestream:
          string = str(i).replace("b'","",1)
          string = string.replace("\\n'", "\n", 1)
          string = string.replace("'", "", 1)
          #string = string.strip("\\n")
          codelines.append(str(string))
          #i.strip("\n'")
        print(codelines)
        cu.run(codelines)

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
        responses.setResponse(y)
        return y

if __name__== "__main__":
  main()
  app.run(host= '0.0.0.0')