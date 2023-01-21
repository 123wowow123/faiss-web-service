# Faiss Web Service

### Getting started
```sh
docker run --rm -it -p 9001:5000 123wowow123/faiss-web-service:[FAISS_RELEASE]
```

Once the container is running, you should be able to ping the service:
```sh
# Healthcheck
curl '34.168.105.198/ping'

# Faiss search
curl '34.168.105.198/faiss/search?q=war&k=10'

# Faiss add
curl 'localhost:5000/faiss/add' -X POST -d '{"id": 9999, "sentence": "war in ukrain"}'

# Faiss remove
curl 'localhost:5000/faiss/remove'  -X DELETE -d '{"id": 9999}'


### Production
The application runs with Flask's build in server. Flask's documentation clearly states [it is not suitable for production](http://flask.pocoo.org/docs/1.1.x/deploying/).


#### Docker Commands
Build docker image
`make`

Upload docker image to repo
`make release`

#### Google Docker/Kubernetes Commands

https://cloud.google.com/sdk/docs/install
https://cloud.google.com/kubernetes-engine/docs/tutorials/hello-app#cloud-shell

Create cluster and go-live
`gcloud container clusters create-auto chronopin-cluster`

`gcloud container clusters get-credentials chronopin-cluster --region us-west1`

`kubectl create deployment faiss-web-service --image=us-west1-docker.pkg.dev/chronopin-209507/faiss/faiss-web-service:v1`

`kubectl scale deployment faiss-web-service --replicas=1`

`kubectl autoscale deployment faiss-web-service --cpu-percent=100 --min=1 --max=1`

checks
`kubectl get pods`

`kubectl expose deployment faiss-web-service --name=faiss-web-lb --type=LoadBalancer --port 80 --target-port 5000`

checks
`kubectl get service`

#### Rolling update

eg: or better use `make gbuild` & `make grelease`

`kubectl set image deployment/faiss-web-service faiss-web-service=us-west1-docker.pkg.dev/chronopin-209507/faiss/faiss-web-service:v1`

`watch kubectl get pods`

`curl '34.168.105.198/ping'`

For delete service read doc

#### pyenv

https://realpython.com/intro-to-pyenv/


Make sure you are in 3.x version
`python -V`

Check version installed on your system
`pyenv versions`

Intall pyenv
`brew install pyenv`

Install python 3
`pyenv install -v 3`

Use python 3
`pyenv global 3.<actual version>`

Check pip is at the same version
`pyenv which pip`

Setup virtualenv
`pip install virtualenv`
`virtualenv venv`
`source venv/bin/activate`
`deactivate venv `

Pip freeze requirments

`pip freeze > requirements.txt`