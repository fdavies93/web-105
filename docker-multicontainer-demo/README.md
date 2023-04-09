# Multi-Container Demo

This project demonstrates concepts for working with multiple containers in Docker using simple Python apps.

## Building and Running

You can build by simply entering into the subfolders reader and writer and running `docker build . -t reader`.

**Creating a shared volume**
```sudo docker volume create demo```

**Creating a shared network**
```sudo docker network create reader-writer```

**Running writer (exposed)**
```sudo docker run -dit -p 5000:5000 -v demo:/data -e DATA_PATH="data/log.txt" --network=reader-writer writer```

**Running writer (unexposed)**
```sudo docker run -dit -v demo:/data -e DATA_PATH="data/log.txt" --network=reader-writer writer```

**Running reader**

Non-detached (preferable). Note that WRITER_ENDPOINT should be the IP within the network.
```sudo docker run -it -v demo:/data -e WRITER_ENDPOINT="http://172.18.0.2:5000" --network=reader-writer reader```

***Full process**
```
sudo docker volume create demo
sudo docker network create reader-writer
(in reader & writer folder)
sudo docker build . -t reader
sudo docker build . -t writer
sudo docker run -dit -v demo:/data -e DATA_PATH="data/log.txt" --network=reader-writer writer
sudo docker network inspect reader-writer
(this lets you find the local endpoint)
sudo docker run -it -v demo:/data -e WRITER_ENDPOINT="http://172.18.0.2:5000" --network=reader-writer reader
```