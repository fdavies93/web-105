# File API for Transcode Demo

This is a basic Flask file server which forms part of a transcoder service Kubernetes demo.

## Building

Note that `watcher` uses a bespoke image including `python3` and `ffmpeg` packages in order to successfully trigger transcodes. Linux distro may be subject to change.

Need to use the `--network=host` option to successfully get the package repositories on the watcher folder.

`docker build --no-cache --network=host . -t transcode-watcher`

## Hosting with Docker Compose

Bringing the `watcher` and `api` containers online is as simple as using `docker compose up`. As the frontend is static, there's no way to dynamically assign an endpoint to it, but you can easily tweak `script.js` to point to the appropriate IP address.

## Todo / Improvements

* Watcher has no guards against trying to transcode the same file at the same time, leading to duplicated work for no reason.
    * Could probably be fixed by just adding a lock file and making different pod containers poll at offset times