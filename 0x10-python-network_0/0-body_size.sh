#!/bin/bash
# Display the size of the body response of a URL
curl -sI "$1" | grep -oP 'Content-Length: \K\d+'
