# HelloWorld with minikube

## exercise
**Mini Kube**
Write a simple hello world application in either of these languages: Python, Ruby, Go. Build the application within a Docker container and then load balance the application within a mini kube.

## assumptions
my solutions takes a couple of points for granted to avoid overcomplicating the solution too moch.
* you have no firewall/proxy need, and internet connection.
* a OSX machine. totally doable under linux, installation commands vary depending on package manager.
* brew cask installed. i totally avoid the curl | bash  blasphemy.

## scripted solution
simply run
```
cd helloKube
bash hellokube-runme.sh
```
