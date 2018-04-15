SWAGGERCODEGEN=java -jar swagger-codegen-cli-2.3.1.jar
YAMLFILE=network.yaml
DESTDIR=server/network/flaskConnexion
CREATED=server
NETWORKDIR=network

all: service start 
	@echo "DONE"

docker-all: docker-build docker-start
	@echo "DONE"

docker-build:
	@echo "building the image from docker file..."
	docker build -t manjoshi/cloudmesh-network .
	@echo "image DONE"

docker-pull:
	@echo "pulling the image from dockerhub..."
	docker pull manjoshi/cloudmesh-network
	@echo "image DONE"

docker-start:
	@echo "starting the service in container..."
	docker run -p 8080:8080 manjoshi/cloudmesh-network

docker-stop:
	@echo "stoping the service..."
	docker stop $$(docker ps -alq)
	@echo "service stopped"

docker-remove:
	@echo "removing the image..."
	docker rmi -f manjoshi/cloudmesh-network
	@echo "image removed"

docker-clean: docker-stop docker-remove
	@echo "DONE"

dest:
	mkdir -p $(DESTDIR)


service: dest
	@echo "creating the service..."
	wget http://central.maven.org/maven2/io/swagger/swagger-codegen-cli/2.3.1/swagger-codegen-cli-2.3.1.jar
	$(SWAGGERCODEGEN) generate \
	-i $(YAMLFILE) \
	-l python-flask \
	-o $(DESTDIR) 
	
	rm *.jar

	cp -r *.py $(DESTDIR)/swagger_server/controllers
	cd $(NETWORKDIR) && pip install -r requirements.txt && python setup.py install
	cd $(DESTDIR) && pip install -r requirements.txt 

start:  
	@echo "starting the service..."
	cd $(DESTDIR) && python -m swagger_server

test:
	curl http://localhost:8080/api/network

	#curl http://localhost:8080/cloudmesh/nlp/pos/Tim%20Cook%20is%20the%20CEO%20of%20Apple.
            
stop:
	@echo "stopping the service"
	ps -ef | grep swagger_server | grep -v "grep" | awk '{print $$2}' | xargs kill -9
	@echo "service stopped"

clean:
	@echo "removing service files created"
	rm -rf $(CREATED)

