#!/bin/bash

# TODO: replace sleep with efficient indication check
# wait for DB init to finish
sleep 5

./run_migrations.sh

# Start Nginx in the background
nginx -g "daemon off;" &

python app.py
