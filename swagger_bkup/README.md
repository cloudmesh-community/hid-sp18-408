# Assignment: Cloud and Big Data Rest Service with Swagger

### Service Descprition

*Built a Network service that will provide following capabilities* 


The implementation gives the network details on the device
The swagger code-gen generate the server stub code for us by taking the 
network.yaml as input and gives us a nice foundation to develop the main logic.
I have implemented main logic in the file *network_stub.py*
at location - https://github.com/cloudmesh-community/hid-sp18-408/tree/master/swagger/network/flaskConnexion/swagger_server/controllers 
I have tried to uphold the best practices of API implementation by keeping 
the defination encapsulated using a stub code.

You can download the code from the repository and start playing around.

### Follow the below steps

* Clone the repository
* Navigate to "flaskConnexion" directory 
* start the service by executing the command "python -m swagger_server"

You will see something like this 
Running on http://0.0.0.0:8080/ (Press CTRL+C to quit)


### Running the service from browser

* Open any browser and request the url with fullyqualified file name

#### Example 1
	http://localhost:8080/api/network
#### Result - 

{
  "Network": {
    "Broadcast": "192.168.1.255",
    "Gateway": "192.168.1.254",
    "IP": "192.168.1.73",
    "MAC": "48:e2:44:d4:e7:cd",
    "MASK": "255.255.255.0",
    "MTU": "1500",
    "Name": "wlo1",
    "Type": "Ethernet"
  }
}
