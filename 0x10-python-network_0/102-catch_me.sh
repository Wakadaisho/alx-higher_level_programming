#!/bin/bash
# Find the response 'You got me' from the URL below
curl -s -X PUT -H "user_id: 98" -b "user_id = 98" -L 0.0.0.0:5000/catch_me
