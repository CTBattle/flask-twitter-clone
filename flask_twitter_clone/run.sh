#!/bin/bash

# Create the instance folder if it doesn't exist (for SQLite DB)
mkdir -p flask_twitter_clone/instance

# Set environment variables
export PYTHONPATH=.
export FLASK_APP=flask_twitter_clone

# Run the Flask server
flask run