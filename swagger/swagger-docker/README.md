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


* The yaml file I used is in 

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

## Start The Service

* clone the repository
* navigate to the directory 

        cd /hid-sp18-408/swagger/swagger-docker
        
* creates the swagger service from the yaml file with correct controllers
        
        make service
        
* start the service by execute:

        make start

* The following will show

        Running on http://0.0.0.0:8080/ (Press CTRL+C to quit)
