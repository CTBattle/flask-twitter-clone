#!/bin/bash

# Ensure instance folder exists
mkdir -p flask_twitter_clone/instance

# Set env variables
export PYTHONPATH=.
export FLASK_APP=flask_twitter_clone

# Run the app on Railway-compatible port
flask run --host=0.0.0.0 --port=8080
