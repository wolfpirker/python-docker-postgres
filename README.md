# Sample Python and PostgreSQL Project with Docker

This project demonstrates a simple Python application that interacts with a PostgreSQL database. The application fetches data from a public API, processes it using Pandas, and stores the results in the database. Additionally, it provides a command-line interface (CLI) for adding new users and orders, and for listing existing users and orders.

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

2.1) use command "docker attach <container-id>"
  to connect to the Python App container shell; there are following menu options in the Python app:
   Choose an option:
	1. Add a new user
	2. Add a new order for an existing user
	3. List all users
	4. List all orders for a specific user
	5. Exit


3.) Access the database

The PostgreSQL database will be accessible on localhost:5432. You can connect to it using any PostgreSQL client with the following credentials:

    Username: user

    Password: password

    Database: sampledb
    
    
4.) Check the application logs

The Python application will fetch data from the API, process it, and insert it into the database. 
You can view the logs in the terminal where you ran docker-compose up.


5) Stopping the Containers

enter command
	$ docker-compose down
in another shell.



_________________

### Summary

This extended version of the project now includes a CLI that allows users to interact with the database by adding new users and orders, 
and by listing existing users and orders. The CLI is integrated into the main application and can be accessed when running the Docker containers. 
This makes it easy to manage and query the database directly from the command line.

