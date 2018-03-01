[![Build Status](https://travis-ci.org/EXXETA/devops-demo.svg?branch=master)](https://travis-ci.org/EXXETA/devops-demo)

# Principles of DevOps Demo

In this project we demo a couple of techniques informed by the three pillars of DevOps:
flow, feedback, and continual experimentation.


## Setup

This demo was developed and tested on OSX - it should therefore run just as well
on Linux operating systems.
For how to install and work with Docker (a central component of this sample project)
on Windows please follow the instructions here:
[https://docs.docker.com/docker-for-windows/](https://docs.docker.com/docker-for-windows/).

Make certain you have Docker installed in a recent version:

    $ docker --version
    Docker version 17.12.0-ce, build c97c6d6

I recommend using Anaconda Python 3 which is straightfoward to use and maintain
virtual environment with: [https://www.anaconda.com/download/](https://www.anaconda.com/download/).

Create a virtual environment:

    $ conda create -n devops python=3.6 --yes

Activate the virtual environment:

    $ source activate devops

Install high-level DevOps-specific frameworks:

    $ pip install -r requirements.txt

## Run tests for `greetings` service

Install `greetings` requirements

    $ pip install pytest
    $ pip install -r greetings/requirements.txt

Run tests

    $ python -m pytest greetings -k tests

## Test services locally

To build all Docker images:

    $ docker-compose build

Now run the services locally:

    $ docker-compose up
