#!/bin/bash

./run_migrations.sh

# Start Nginx in the background
nginx -g "daemon off;" &

python app.py
