#!/bin/sh

# Run database migrations
alembic -c svc/api/v1/migrations/alembic.ini upgrade head
