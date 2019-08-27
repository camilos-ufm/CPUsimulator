<h1 align="center">
  <a href="https://github.com/denysdovhan/spaceship-prompt">
    <img alt="spaceship →~ prompt" src="https://www.google.com/url?sa=i&rct=j&q=&esrc=s&source=images&cd=&ved=2ahUKEwjBzcuxjKLkAhUSwlkKHahpCdwQjRx6BAgBEAQ&url=https%3A%2F%2Fpixabay.com%2Fvectors%2Fcpu-processor-intel-amd-chip-152656%2F&psig=AOvVaw27soldjBh8raIEdF04OI4C&ust=1566962485384718" width="400">
  </a>
  <br>🚀 CPU Simulator <br>
</h1>

<h4 align="center">
  <a href="http://zsh.org" target="_blank"><code>Zsh</code></a> prompt for Astronauts.
</h4>

<div align="center">
  <h4>
    <a href="#">Website</a> |
    <a href="#installing">Install</a> |
    <a href="#features">Features</a> |
    <a href="./docs/Options.md">Options</a> |
    <a href="./docs/API.md">API</a>
  </h4>
</div>

<div align="center">
  <sub>Built with ❤︎ by
  <a href="#">Katherine Mazariegos</a>,
  <a href="#">Daniel Hernández</a> and <a href="#">Andres Bolaños</a>
</div>
<br>

CPU simulator is an app that provides a set of instruction in order to recreate the functions of an actual CPU.

<sub>Vist <a href="#">Troubleshooting</a> for similar setup and find more..</sub>

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


pipenv install --ignore-pipfile

docker run -it --network="host" 

docker run -it --network="host" cpusimulator:0.0

docker run -it -p 5000:5000 andresry/cpusimulator:0.0
docker run --name web -d -p 5001:80 webcpu:0.0
docker run -it -d -p 5001:80 webcpu:0.0

docker-compose up -d
docker-compose down -v

docker ps

#To run it in debug mode / check the time
build the image from api.Dockerfile
docker run -it -p 5000:5000 cpusimulator:0.0

#To run it in production mode
docker-compose up --build