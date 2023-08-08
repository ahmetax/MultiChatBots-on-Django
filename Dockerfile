FROM python:3.10

# Do not use buffering
ENV PYTHONUNBUFFERED 1

# project root directory in the container
RUN mkdir /multibots

# Set the working directory
WORKDIR /multibots

# Copy the current directory contents into the container at /multibots
ADD . /multibots/

# upgrade pip
RUN pip install --upgrade pip

# Install modules in requirements.txt
RUN pip install -r requirements.txt
