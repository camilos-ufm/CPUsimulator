<h1 align="center">
  <!-- a href="https://github.com/denysdovhan/spaceship-prompt" -->
    <img alt="cpu" src="https://github.com/lisos-ufm/CPUsimulator/blob/andr/Simulator-Frontend/Unordered/cpu2.png" width="400">
  <br>🚀 CPU Simulator <br>
</h1>

<div align="center">
  <h4>
    <a href="#Features and Technologies">Features</a> |
    <a href="#Requirements">Requirements</a> |
    <a href="#Installing and running the app">Installing</a> |
    <a href="#Contributing">Contributing</a> |
    <a href="#License">License</a>
  </h4>
</div>

<div align="center">
  <sub>Built with ❤︎ by
  <a href="#">Katherine Mazariegos</a>,
  <a href="#">Daniel Hernández</a> and <a href="#">Andres Bolaños</a>
</div>
<br>

CPU simulator is an app that provides a set of instruction in order to recreate the functions of an actual CPU.

<sub>Vist <a href="#">Troubleshooting</a> to find more.</sub>

## Features and Technologies

- Let you upload a .code from website
- Debug mode implemented 
- See the CPU date in real time
- Mnemonic and Machine code
- You can edit the BIOS initial setup from a yml file
- Cross-platform, using Docker.
- Using Docker-Compose to run multiple containers.
- Pipenv
- TravisCI 
- NGINX for web page 
- Using OPP 
- Using functions as FCO
- Support for Linux, MacOS and Windows with Docker properly installed


**💡 Warning:** You cannot run production mode with clock set up as 0. That parameter is meant for debug mode only.

## Requirements

To work correctly, you will first need:

- [`Docker`](https://docs.docker.com/install/) must be installed.

## Installing and running the app

Now that the requirements are satisfied, you can install and run the CPU Simulator. First download or clone the repository and:

### [Production]

```
docker-compose up --build

```

Done. This command should run both containers (web and api). In order to see the app hit your computer host direction in the port [`5001`](http://localhost:5001/).

**💡 Warning:** Do not run this method if clock is set as 0 in bios.yml file.

### [Debug mode]

Make the required changes in bios.yml, you can either change the clock attribute to 0, program will wait for an Enter to continue. If not, you will be able to see the logs from the CPU simulator.

#### Procedure:

- Build the api image from api.Dockerfile
- Run the image you just build with the following flags: 

```
docker run -it -p 5000:5000 andresry/cpusimulator:0.0

```

- If you want to use the web app to interact with the debug mode of the cpu, please build the image for the NGINX container and run it as:

```
docker run --name web -d -p 5001:80 andresry/webcpu:0.0

```
- Open your browser and go to your port [`5001`](http://localhost:5001/).

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License
[MIT](https://choosealicense.com/licenses/mit/)
