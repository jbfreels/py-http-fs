# py-http-fs

Python HTTP folder share with or without basic authentication.

Basic authentication borrowed from: https://gist.github.com/fxsjy/5465353

Makefile included for basic building of the docker image and running.

## Building

```script
docker build -t py-http .
```

## Example Usage

Start py-http with no basic auth sharing `/tmp` on port 8081:

```bash
docker run -d -p 8081:80 \
  -v /tmp:/data \
  py-http
```

Start py-http with basic auth sharing `/tmp` on port 8081:

```bash
docker run -d -p 8081:80 \
  -v /tmp:/data \
  -e USERNAME='share' \
  -e PASSWORD='password' \
  py-http
```

Browse to _http://localhost:8081_ to access the share in your web browser.
