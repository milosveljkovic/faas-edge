# faas-edge
SmartHome app deployed in openwhisk as a set of actions

### Getting started

1. run minikube
2. port forward owdev-nginx
3. config wks

## Actions & FaasEdge Architecture

This section will describe all the actions briefly.
At the bottom of section the `faas` diagtam will be posted.

#### Processing Action (PA)

Simple action which should provide pre-processing of sensor data.

- remove NaN values
- remove missing values

After data preprocessing, PA sends PURE data to SA.

#### Storing Action (SA)

SA provides a store mechanism to PostgreSQL.
SA is in the chain with Processing Action.

As DB has been deployed in K8S, the following connection string shoud be set:

```py
conn=psycopg2.connect("host=pg-minikube-postgresql.default port=5432 dbname=postgres user=postgres password=postgres")
```

## Development

#### Useful commands

#### minikube 

Start minikube:
```sh
minikube start --addons=ingress
```

Port-forward owdev nginx:

```sh
kubectl port-forward svc/owdev-nginx -n openwhisk 8080:80
```

#### Postgres DB in minikube

```sh
helm repo add bitnami https://charts.bitnami.com/bitnami
helm install pg-minikube --set auth.postgresPassword=postgres bitnami/postgresql
# For locac development port-forward
kubectl port-forward svc/pg-minikube-postgresql -n default 5432:5432
```

#### Openwhisk

Configure wsk:
```sh
wsk property set --auth owdev-whisk.auth.system --apihost http://localhost:8080
```

Deploy action with external packages (zip):
```sh
wsk action create processingv8 --kind python:3 --main main processing.zip
```

Deploy action:
```sh
wsk action create helloJS hello.js
```

Delete action:
```sh
wsk action delete helloJS
```

Pack external python libraries within action:
```sh
docker run --rm -v "$PWD:/tmp" openwhisk/python3action bash   -c "cd tmp && virtualenv virtualenv && source virtualenv/bin/activate && pip install -r requirements.txt"
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