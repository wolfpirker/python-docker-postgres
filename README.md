# Sample Python and PostgreSQL Project with Docker

This project demonstrates a simple Python application that interacts with a PostgreSQL database. 
The application fetches data from a public API, processes it using Pandas, and stores the results in the database. 
Additionally, it provides a command-line interface (CLI) for adding new users and orders, and for 
listing existing users, orders, and products.

## Prerequisites

- Docker
- Docker Compose

## Getting Started

1.) **Clone the repository**

   ```bash
   git clone https://github.com/yourusername/sample-docker-python-postgres.git
   cd sample-docker-python-postgres


2.) Build and run the Docker containers
$ docker-compose up --build

3.) Access the database

The PostgreSQL database will be accessible on localhost:5432. You can connect to it using any PostgreSQL client with the following credentials:

    Username: user

    Password: password

    Database: sampledb
    
4.) Use the CLI
use command "docker attach <container-id>"
to connect to the Python App container shell; 

The Python application provides a simple CLI for interacting with the database. When you run docker-compose up, the CLI will be available in the terminal. You can choose from the following options:

    Add a new user

    Add a new order for an existing user

    List all users

    List all orders for a specific user

    List all products

    Exit
    
================================
Data Persistence
Option 1: Bind Mounts

The database data is persisted on the host system using a bind mount. The data is stored in the ./db/data directory.
Option 2: Copy Data to Host

To copy the database data to the host system, run the following command:
bash
Copy

docker-compose exec db /scripts/copy_data_to_host.sh

The data will be copied to the /host_data directory on the host system.

================================
Stopping the Containers

To stop and remove the containers, run:
bash
Copy

docker-compose down


_________________

### Summary

This extended version of the project now includes:
- Data persistence using bind mounts and data copying.
- An extended database schema with `products` and `order_items` tables.
- Sample data initialization for users, orders, and products.
- A CLI for managing and querying the database.

You can now run the project, and the data will persist outside the container. 
The CLI allows you to interact with the database and manage users, orders, and products.
