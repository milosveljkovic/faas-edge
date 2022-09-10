import requests

def main(dict):
  url = "http://host.minikube.internal:8083/savemode"
  headers = {"accept": "application/json"}
  response = requests.post(url=url,headers=headers)
  print(response)
  return {"msg":"Save mode successfully activated!"}