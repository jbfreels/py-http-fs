# py-http-fs
Python HTTP folder share with or without basic authentication. 

Basic authentication borrowed from: https://gist.github.com/fxsjy/5465353

Makefile included for basic building of the docker image and running.

## Building
```
docker build -t py-http .
```

## Example Usage
Start py-http with no basic auth sharing  `/tmp` on port 8081:

```
docker run -d -p 8081:80 \
  -v /tmp:/data \
  py-http
```

Start py-http with basic auth sharing `/tmp` on port 8081:

```
docker run -d -p 8081:80 \
  -v /tmp:/data \
  -e USERNAME='share' \
  -e PASSWORD='password' \
  py-http
```

Browse to *http://localhost:8081* to access the share in your web browser.
