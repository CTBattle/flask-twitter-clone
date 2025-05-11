#!/bin/bash

# Ensure instance folder exists
mkdir -p flask_twitter_clone/instance

# Set environment variables
export PYTHONPATH=.
export FLASK_APP=flask_twitter_clone

# Reset and seed the database
python3 flask_twitter_clone/seed.py
