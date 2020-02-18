#!/usr/bin/env  bash

# Build image
docker build --tag=api .

# List images
docker image ls

# Run flask app
docker run -p 80:5001 api