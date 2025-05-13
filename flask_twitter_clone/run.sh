#!/bin/bash

# Ensure instance folder exists (for SQLite DB)
mkdir -p flask_twitter_clone/instance

# Set environment variables
export PYTHONPATH=.
export FLASK_APP=flask_twitter_clone:create_app

# Apply DB migrations before starting
flask db upgrade

# Start server on Railway's assigned port
flask run --host=0.0.0.0 --port=${PORT:-5000}
