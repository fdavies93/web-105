# File API for Transcode Demo

This is a basic Flask file server which forms part of a transcoder service Kubernetes demo.

## Building

Need to use the `--network=host` option to successfully get the package repositories on the watcher folder.

`docker build --no-cache --network=host . -t transcode-watcher`