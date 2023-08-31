#!/bin/bash
# Displays the status code of a response using only curl
curl -sI -o /dev/null -w "%{response_code}" "$1"
