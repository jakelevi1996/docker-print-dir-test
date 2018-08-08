
# docker-print-dir-test

Simple test for printing the contents of the Docker container's filesytem

Simultaneously build the image, name it as "print-dir" and run in a container using the following command:

docker build -t print-dir . && docker run -it print-dir