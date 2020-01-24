#!/bin/bash
docker stop stardew_scanner
docker build . -t stardew_scanner

# Stop and remove existing docker images if they exist
docker rm stardew_scanner

# run docker image detached
docker run -itd -p 8080:8080 --name stardew_scanner stardew_scanner
