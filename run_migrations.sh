#!/bin/sh

# Run database migrations
alembic -c svc/api/v1/alembic.ini upgrade head
