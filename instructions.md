
1) start
Hello, can you create a small sample project in Python language, with Dockerfiles for 2 docker images; 
one image should contain all data in a Postgres database, you can take a convenient docker base image from dockerhub. 
The second image with our small Python project should use the database of the first image, it should load and store data to it.
Please also create a docker compose file and a Readme about how to use the docker compose and dockerfiles. 
The python project should not contain more than 1200 lines of code, it could use public data accessible by an API or calculate 
data using advanced data science Python libraries like Numpy or Pandas. Please also provide suitable database entities for the Postgres database. 
The database should contain simple database entities, and not more than 4 total database entities.
________________

2) first extension user input:
Can you extend the previous example project with Python so that a user can enter additional user and 
order data and can also enter a command to list existing users and another command to list orders of a specific user?
_________________________

3) second extension persiting DB data and product types in orders:
can you please revise and extend the example by the following:
* the data stored to the Postgres container, should be persisted outside of the container on the host system:
  - show two alternative ways: one using bind mounts and another by copying the data of the database to the host
  - when starting a new DB container, it should check for preexisting data in the host system
* the orders DB entity does not contain any order items; please extend the DB entity of orders with a product type, and add another DB entity for the product types
* please initialize the data for each user, with two orders, each order containing one or more products, of different amount. Fill also the product DB entity accordingly.
