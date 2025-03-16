#!/bin/sh

# Check if data directory is empty (bind mount)
if [ -z "$(ls -A /var/lib/postgresql/data)" ]; then
  echo "No existing data found. Initializing database..."
  exec /usr/local/bin/docker-entrypoint.sh postgres
else
  echo "Existing data found. Skipping initialization."
  exec /usr/local/bin/docker-entrypoint.sh postgres
fi
