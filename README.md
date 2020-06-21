# userdataapi

This Git Repo is the solution to the given assignment by Fullthrottlelabs.
I have used SQLite3 as DB and used DJANGO REST FRAMEWORK to generate REST API and the JSON output.
It is deployed on AWS with IPv4 Public IP
: 54.161.174.136 or as Public DNS (IPv4): ec2-54-161-174-136.compute-1.amazonaws.com
You can access JSON data using the cmd: 
curl -v "http://54.161.174.136/users/"
or 
curl -v "http://ec2-54-161-174-136.compute-1.amazonaws.com/users/"
You can download JSON data using the cmd:
curl -o data.json "http://54.161.174.136/users/"
or 
curl -o data.json "http://ec2-54-161-174-136.compute-1.amazonaws.com/users/"
Or Using POSTMAN
