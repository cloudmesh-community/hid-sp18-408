# Swagger Network service on Docker


## Acknowlegement: 
I referred to the git repo owned by Pathan, Shagufta (hid-sp18-516), modified
and created my own Make file for this assignment
 

## Implementation :
* The specification of the REST service is defined in `network.yaml` file
* The logic to display the network details has been implemented in the file `network_stub.py`
* The server-side code has been generated using Swagger Codegen


## Execution steps
This is the directory for reproducable Reset Service with Swagger. 

* The reproducibility can be achieved by using the Make file, one could either use it with docker container:

	- make docker-all -- creates the docker image, start the container running the service

	- make docker-build -- creates the docker image 

	- make docker-start -- start the container which runs the REST service

	- make docker-stop -- stop the container 

	- make docker-remove -- remove the docker image

	- make docker-clean -- stop the container and remove the image

  
