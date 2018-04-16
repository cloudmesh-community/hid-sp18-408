# Swagger Network service on Docker


## Acknowlegement: 
The github repo of Pathan, Shagufta (hid-sp18-516) was refered while implementing this service on docker.
 

## Implementation :
* The specification of the REST service is defined in `network.yaml` file
* The logic to display the network details has been implemented in the file `network_stub.py`
* The server-side code has been generated using Swagger Codegen


## Execution steps
This is the directory for reproducable Reset Service with Swagger. 

* clone the repository

* navigate to the directory 

        cd /hid-sp18-408/swagger/swagger-docker

* Using Docker to run the network service:

	- make docker-all -- creates the docker image, start the container running the service

	- make docker-build -- creates the docker image 

	- make docker-start -- start the container which runs the REST service

	- make docker-stop -- stop the container 

	- make docker-remove -- remove the docker image

	- make docker-clean -- stop the container and remove the image

* Test the service:
	- make docker test -- curl for network details

* The yaml file is at 

        hid-sp18-405/swagger/swagger-docker/network.yaml
    
* The default_controller is at 

        hid-sp18-405/swagger/swagger-docker/default_controller.py
    
* To install these modules alone, please cd to the above directory and run:
		
		pip install -r requirements.txt
 		python setup.py install
  
## Service Descprition

The Rest service gives the network information of the system.
To display the name of the network interface, IP, Gateway, MAC address, Subnet Mask, 
Broadcast, MTU of the network interface, netifaces library is used.

