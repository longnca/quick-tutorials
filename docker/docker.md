# Introduction to Docker

## Table of Contents:
1. [References](#references)
1. [Step-by-step Installation](#step-by-step-installation)
1. [Using Docker on Windows](#using-docker-on-windows)
1. [Best practices for using Docker on Windows](#best-practices-for-using-docker-on-windows)
1. [How to run a container from a single image](#how-to-run-a-container-from-a-single-image)
1. [Multi-container applications](#multi-container-applications)


## References:

Some good resources to learn more about Docker:
- [Docker Official Documentation](https://docs.docker.com/guides/get-started/).
- [DE Zoomcamp by DataTalksClub - 24 minutes - FREE](https://youtu.be/EYNwNlOrpr0?si=sqlXisduRe3plhkM).
- [Docker Fundamentals course by Cantrill - FREE](https://learn.cantrill.io/p/docker-fundamentals).
- [Docker Fundamentals YouTube playlist by Cantrill - FREE](https://www.youtube.com/playlist?list=PLTk5ZYSbd9Mg51szw21_75Hs1xUpGObDm).

## Step-by-Step Installation

### Download Docker Desktop for Windows:

- Visit the Docker website and download Docker Desktop for Windows.
- You need to create a Docker account if you don’t have one already.

### Install Docker Desktop:

- Run the installer you downloaded.
- Follow the install wizard to accept the license, authorize the installer, and proceed with the install.
- You will be prompted to authorize Docker.app with your system password during the install process.
- Once it's complete, you will see the message as below.
![docker-install-success](images/docker-install-success.png)

### Configure WSL 2:

- During installation, you may be prompted to enable **Windows Subsystem for Linux version 2 (WSL 2)** and download a Linux kernel update package if WSL 2 is not already installed.
- If you are using VS Code editor, you will be prompted to install the **WSL extension** in VS Code.

### Configure Docker:

- Docker starts automatically once the installation is complete.
- Docker will ask you to log in with your Docker account. Use the Docker ID and password you created when you downloaded Docker.

### Verify installation:

- Open a command prompt or PowerShell window.
- Run the following command to check if Docker is installed and running:
```bash
docker --version
```

### Run your first container:

- You can test Docker by running a simple container to verify that Docker can pull and run *images*.
- Open a command prompt or PowerShell and run the following command:
```bash
docker run hello-world
```
- Docker will download and run a small test *image*. If successful, you'll see a message indicating that your installation appears to be working correctly.
![docker-run-hello-world](images/docker-run-hello-world.png)
- If you follow the walkthrough instructions on "Docker Desktop" to create the first container, you will select `8088:80`⁠ in the Port(s) column to see it running.
![docker-first-container-1](images/docker-first-container-1.png)
- You'll see the message at port `http://localhost:8088:80`on the browser as below.
![docker-first-container-2](images/docker-first-container-2.png)


**Congratulations!** Now you have Docker installed and running on your Windows machine. You can start using it to containerize applications, including databases, data processing tools, and more.

## Using Docker on Windows

- **Docker CLI**: Use Docker commands in your terminal to pull images, run containers, and manage Docker.
- **Docker Compose**: Docker Desktop includes Docker Compose for defining and running multi-container Docker applications.
- **Docker Desktop Dashboard**: Provides a simple interface to manage your containers, images, networks, and volumes.

## Basic Docker commands
- `docker pull [image]`: Pulls an image from Docker Hub.
- `docker run [image]`: Runs a container from an image.
- `docker ps`: Lists running containers.
- `docker images`: Lists images that are locally stored with the Docker engine.
- `docker stop [container-id]`: Stops a running container.

## Best practices for using Docker on Windows

- Regularly update Docker to the latest version to get new features, bug fixes, and security patches.
- Use **Docker Volumes** for persistent data storage.
- Be aware of the differences between Linux and Windows containers, especially if you are developing cross-platform applications.
- Utilize **Docker Compose** for managing multi-container applications.

## How to run a container from a single image

**Credit:** Everything in this section is pasted from Docker Desktop's walkthrough instruction. All the screenshots are mine.

In this guide, you create an image using a Dockerfile and a sample application.

### Get the sameple applicaiton:

- Clone the repository at https://github.com/docker/welcome-to-docker⁠.
```bash
git clone https://github.com/docker/welcome-to-docker
```
- Run the following command before moving on.
```bash
cd welcome-to-docker
```

### Verify your Dockerfile:

- Open the sample application in your IDE (e.g. VS Code). Note that it already has a Dockerfile. For your own projects you need to create this yourself.
![dockerfile](images/dockerfile.png)

### Build your first image:

- You can build an image using the following docker build command via a CLI in your project folder.

```bash
docker build -t welcome-to-docker .
```
Explain the command: The `-t` flag tags your image with a name. (welcome-to-docker in this case). And the `.` (dot) lets Docker know where it can find the Dockerfile.

### Run your container:

- Once the build is complete, an image will appear in the **Images** tab in Docker Desktop.
![dockerfile-in-images](images/dockerfile-in-images.png)

- Select the image name to see its details. Select **Run** to run it as a container. In the Optional settings remember to specify a port number (something like `8089`).
![run-optional-settings](images/run-optional-settings.png)

### View the frontend:

- You now have a running container. 
- If you don't have a name for your container, Docker provides one. View your container live by selecting the link below the container's name.
![run-front-end](images/run-front-end.png)
- You'll see the message at port `http://localhost:8089/`on the browser as below.
![docker-first-container-2](images/docker-first-container-2.png)

## Multi-container applications

**Credit:** Everything in this section is pasted from Docker Desktop's walkthrough instruction. All the screenshots are mine.

### Introducing Docker Compose:

- You already know how to start each container individually. 
- Imagine how great it would be if a tool could start multiple containers with a single command. That tool is Docker Compose.

### Get the sample app:

- Clone the repository at https://github.com/docker/multi-container-app⁠.
```bash
git clone https://github.com/docker/multi-container-app
```

### Understanding the sample:

- This is a simple todo application built using ExpressJS and Node. All todos are saved in a MongoDB database.
![multi-container-1](images/multi-container-1.png)

### `compose.yaml`:

- If you view the code of the sample application, you will notice that it has a `compose.yaml` file. 
- This file tells Docker how to run your application. Open the `compose.yaml` file in a text editor to explore the instructions.
![compose-yaml](images/compose-yaml.png)

### Running the application:

- We are going to run this application with the docker compose up command in your project directory. This command builds and runs all the services listed in the compose file.
```bash
docker compose up -d
```
- Explain the command: The `-d` flag tells docker compose to run in detached mode.
![docker-compose-up-d](images/docker-compose-up-d.png)

### View the frontend:

- In Docker Desktop, you should now have two containers running (the `todo-app`, and `todo-database`). To view the frontend, expand the app stack in Containers and select the link to `localhost:3000`⁠.
![multi-container-2](images/multi-container-2.png)
- Add some tasks in the frontend, and then open the app in a new tab. Notice that the tasks are still visible.
![multi-container-3](images/multi-container-3.png)

### Develop in your containers

- When developing with Docker, you may need to automatically update and preview your running services as you edit and save your code. We use docker compose watch for this.
- Run the following command to run your project with compose watch.
```bash
docker compose watch
```
- Now change the text in line 18 of the app `app/views/todos.ejs` to see your changes *in real time*.
- Read more about how to set this up in your own applications via the compose watch documentation⁠.
- Stop watch mode: You can stop watch with `Ctrl + C` shortcut.

### Delete everything and restart:

- Having your configuration stored in a Compose file has another advantage, you can easily delete everything and restart.
- Simply select the app stack, and then select `Delete` on Docker Desktop. 
![multi-container-delete](images/multi-container-delete.png)
- When you want to restart, run `docker compose up` in the project folder again. This will restart your application again. 
- Note that when the db container is deleted, any todos created are also lost.