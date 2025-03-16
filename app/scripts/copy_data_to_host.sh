#!/bin/sh

# Copy data from container to host
echo "Copying data to host..."
cp -r /var/lib/postgresql/data /host_data
echo "Data copied to /host_data."
