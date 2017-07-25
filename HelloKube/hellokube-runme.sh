#!/bin/bash

# this setup assumes:
# - you have no firewall/proxy need, and internet connection.
# - a OSX machine. totally doable under linux, installation commands vary depending on package manager.
# - brew cask installed. i totally avoid the curl | bash  blasphemy.

# install minikube. I use OSX and brew for simplicity, your mileage may vary.
# installation instructions:
brew cask install minikube

# you'll also need docker. For osx, easiest option would be Docker for Mac:
# https://docs.docker.com/engine/installation/mac/

# make sure we use the minikube context
# (in case of other preexisting k8s deployments)
kubectl config use-context minikube
# use minikube's docker env (again to avoid clashing with other docker settings)
eval $(minikube docker-env)
# build local Dockerfile. It will pull flask and a slim python docker image.
# the app listens on port 9000.
docker build -t hellokube:v1 .
# create a k8s deployment
kubectl run hellokube --image=hellokube:v1 --port=9000
# and service
kubectl expose deployment hellokube --type=NodePort
# finally, open browser to the exposed host for the listening app
minikube service hellokube
