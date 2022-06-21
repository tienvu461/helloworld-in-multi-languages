build image
```
docker build . -t helloworld-in-node
```

run
```
docker run -p 3000:3000 -d helloworld-in-node
```

test
```
curl localhost:3000
HTTP/1.1 200 OK
X-Powered-By: Express
Content-Type: text/html; charset=utf-8
Content-Length: 11
ETag: W/"b-Ck1VqNd45QIvq3AZd8XYQLvEhtA"
Date: Tue, 21 Jun 2022 14:04:10 GMT
Connection: keep-alive
Keep-Alive: timeout=5

Hello World%
```