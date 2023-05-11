# File API for Transcode Demo

This is a basic Flask file server which forms part of a transcoder service Kubernetes demo.

## Building

Need to use the `--network=host` option to successfully get the package repositories on the watcher folder.

`docker build --no-cache --network=host . -t transcode-watcher`

## Hosting with Docker Compose

Bringing the `watcher` and `api` containers online is as simple as using `docker compose up`. As the frontend is static, there's no way to dynamically assign an endpoint to it, but you can easily tweak `script.js` to point to the appropriate IP address.