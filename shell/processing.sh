curl -u "789c46b1-71f6-4ed5-8c54-816aa4f8c502:abczO3xZCLrMN6v2BKK1dXYFpXlPkccOFqm12CdAsMgRU4VrNZ9lyGVCGuMDGIwP" \
 "http://localhost:8080/api/v1/namespaces/_/actions/processingv001?blocking=true&result=true" \
 -X POST -H "Content-Type: application/json" \
 -d '{"data":"1451624400,0.932833333,0.003483333,0.932833333,3.33E-05,0.0207,0.061916667,0.442633333,0.12415,0.006983333,0.013083333,0.000416667,0.00015,0,0.03135,0.001016667,0.004066667,0.001516667,0.003483333,36.14,clear-night,0.62,10,Clear,29.26,1016.91,9.18,cloudCover,282,0,24.4,0"}'

curl -u "789c46b1-71f6-4ed5-8c54-816aa4f8c502:abczO3xZCLrMN6v2BKK1dXYFpXlPkccOFqm12CdAsMgRU4VrNZ9lyGVCGuMDGIwP" \
 "http://localhost:8080/api/v1/namespaces/_/actions/storingv003?blocking=true&result=true" \
 -X POST -H "Content-Type: application/json" \
 -d '{"dw":6.0,"fridge":0.0,"fu":2.0,"fu2":4.0,"gen":5.0,"ho":4.0,"time":"1970-01-01 00:00:02","use":4.0,"wc":0.0}'

curl -u "789c46b1-71f6-4ed5-8c54-816aa4f8c502:abczO3xZCLrMN6v2BKK1dXYFpXlPkccOFqm12CdAsMgRU4VrNZ9lyGVCGuMDGIwP" \
 http://owdev-nginx.openwhisk:80/api/v1/namespaces/_/triggers/testbe \
-X PUT -H "Content-Type: application/json" \
-d '{"name":"events"}'