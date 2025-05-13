#!/bin/bash

# Create the instance folder if it doesn't exist (for SQLite DB)
mkdir -p flask_twitter_clone/instance

# Set environment variables
export PYTHONPATH=.
export FLASK_APP=flask_twitter_clone

# Use Railway's injected port and bind to 0.0.0.0
flask run --host=0.0.0.0 --port=8080
