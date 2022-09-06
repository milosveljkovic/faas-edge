# faas-edge
SmartHome app deployed in openwhisk as a set of actions

#### Useful commands

#### minikube 

start minikube:
```sh
minikube start --addons=ingress
```

port-forward owdev nginx:

```sh
kubectl port-forward svc/owdev-nginx -n openwhisk 8080:80
```

#### Openwhisk

configure wsk:
```sh
wsk property set --auth owdev-whisk.auth.system --apihost http://localhost:8080
```

deploy action with external packages (zip):
```sh
wsk action create processingv8 --kind python:3 --main main processing.zip
```

deploy action:
```sh
wsk action create helloJS hello.js
```

delete action:
```sh
wsk action delete helloJS
```

#### Curl

```sh
curl -u owdev-whisk.auth.system \
"http://localhost:8080/api/v1/namespaces/_/actions/ACTION_NAME?blocking=true&result=true" \
-X POST -H "Content-Type: application/json"
```

with body:
```sh
curl -u owdev-whisk.auth.system \
 "http://localhost:8080/api/v1/namespaces/_/actions/ACTION_NAME?blocking=true&result=true" \
 -X POST -H "Content-Type: application/json" \
 -d '{"data":"1451624400,0.932833333,0.003483333,0.932833333,3.33E-05,0.0207,0.061916667,0.442633333,0.12415,0.006983333,0.013083333,0.000416667,0.00015,0,0.03135,0.001016667,0.004066667,0.001516667,0.003483333,36.14,clear-night,0.62,10,Clear,29.26,1016.91,9.18,cloudCover,282,0,24.4,0"}'
```