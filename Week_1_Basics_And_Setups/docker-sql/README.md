# Docker and PostgreSQL

## Introduction to Docker

__Docker__ is a platform as a serivce products that use OS-level virtualization to deliver software in packages called *containers* similar to virtual machines but lighter in resource consumption. Each of these containers bundle the software, libraries, and configuration files so that they are isolated from one another.

A __Docker image__ is a *snapshot* of a container that we can define to run our software, or in this case our data pipelines. By exporting our Docker images to Cloud providers such as Amazon Web Services or Google Cloud Platform we can run our containers there.

In our use case, lets say we have a data pipeline, we want to run this data pipeline in a docker container so that this data pipeline is isolated from the rest.

[Images here showing basic flow of data pipeline]

To run this pipeline on our host computer (windows) and to achieve isolation, we can use docker. A simple architecture to illustrate:

[Images here showing the architecture]

Each of those blocks (containers) are self contained, and they will have everything that the particular service needs such as the software, configurations, and library dependencies in it.

<br>

### Why docker?

* Reproducibility
    * Docker containers are __stateless__. Any changes done inside a container will __NOT__ be saved when the container is killed and started again. This is an advantage because it allows us to restore any container to its initial state in a *reproducible* manner, but you will have to store data elsewhere if you need to do so; a common way to do so is with volumes.
* Local experiments
* Integration tests (CI/CD)
* Running pipelines on the cloud (AWS Batch, Kubernetes jobs)
* Spark (Analytics enginer for large-scale data processing)
* Serverless (AWS Lambda)

<br>

### Creating a simple data pipeline in Docker

To get started we can try to run the following command to verify docker is working:

```
docker run hello-world
```

this command will first look for a Docker image called `hello-world` from the local repository. If it doesn't exist, then it will try to pull (download) it from the Docker Hub, which is a cloud-based repository for container images.

Once the command container is started it will print a Hello World message on the CLI.

We can also add parameters to the command for example:

```
docker run -it ubuntu bash
```

the flag `-it` means that we want to run the container *interactively*, and we want to execute/run `bash` on the `ubuntu` docker image.

Once the container starts it will give us access to a bash prompt inside the container.

Now lets create a simple `Dockerfile` which is used to build our Docker image.

```dockerfile
# base image that we will build on
FROM python:3.8

# run commands to install dependencies for our pipelines
RUN pip install pandas

# set bash as the entrypoint to give us a bash prompt instead of python prompt
ENTRYPOINT [ "bash" ]
```

Now lets build the image

```
docker build -t test:pandas .
```

Check if the image was built

```
docker image ls
```

We should see that the image is successfully built on the repository `test` tagged `pandas`

![docker-images](images/docker-images.png)

Now lets run the container

```
docker run -it test:pandas
```

Verify that pandas is installed by running the command `python` on the bash prompt to open up a python prompt and then run

```python
import pandas
pandas.__version__
```

Now lets create the baseline for our pipeline script. `pipeline.py`

```python
import pandas as pd

# do stuff with pandas

print ('job finished successfully')
```

Next modify the Dockerfile

```dockerfile
FROM python:3.8

RUN pip install pandas

# set the working directory inside the container
WORKDIR /app

# copy the script to the container, 1st is source file, 2nd is destination
COPY pipeline.py pipeline.py

ENTRYPOINT [ "bash" ]
```

Now rebuild the image with the same command above and rerun the container. Finally, test the container.

![docker-test](images/docker-test.png)

For a data pipeline our container need to be self sufficient, instead of opening python prompt everytime we want to test our pipeline. Some modifications are in order to the `pipeline.py` script and `Dockerfile`

```python
import sys
import pandas # not actually used yet but keep it atm

# print arguments
print(sys.argv)

# argument 0 is the name of the file
# argumment 1 contains the actual first argument we care about
day = sys.argv[1]

# cool pandas stuff goes here

# print a sentence with the argument
print(f'job finished successfully for day = {day}')
```

Running this script with `python pipeline.py <some_number>` will print out:

* `['pipeline.py', '<some_number>']`
* `job finished succesfully for day = <some_number>`

Next is to modify the `Dockerfile` to containerize the script:

```dockerfile
FROM python:3.8

RUN pip install pandas

WORKDIR /app
COPY pipeline.py pipeline.py

# instead of starting the container with bash prompt,
# we straight up just run the script.
ENTRYPOINT [ "python", "pipeline.py" ]
```

Next lets rebuild the image and run the container with additional argument `<some_number>`, lets say `2022-02-05`

```
docker run -it test:pandas 2022-02-05
```

![docker-self-suf](images/docker-self-suf.png)