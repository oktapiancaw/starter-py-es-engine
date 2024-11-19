#!/bin/zsh
# Build

docker buildx build -t <engine_name>  .
docker tag <engine_name> 192.168.107.22/oxt-experiments/<engine_name>:latest
docker push 192.168.107.22/oxt-experiments/<engine_name>:latest; notify-send -u critical "Build image done" "Image : <engine_name>"


