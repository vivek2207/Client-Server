Hi,

This is readme file for this code. This folder consist three files aapart from readme files. 

Please go through the file and its details below: 

1. Client.py: Python file to send request to server and receive response from it. It is using config.json as input file to send the request. 
2. config.json: This file consist list of all commands in json format and it consist total 16 commands ranging from directory creation to pinging over an active website. 
3. Server.py: This file is processing all the requests that are coming to the server. This uses libraris such as subprocess and json to handle and process the requests.

How to execute: 

  1. Download the folder and unzip it using correct tool. 
  2. You need to have certain libraries such as subporcess, json, time, threading etc. 
  3. Make sure that the mentioned port number is also open on your system, otherwise you mayvget error while code execution. 
  4. Run server.py first so that it can start listening to the client requests. 
  5. Run client.py and all the requests will be processed by the server.py and success response will be forwarded back to the client.
  6. Once the execution is done you can close the server.py as well. 

Note: I have windows system and I can not use linux, however, I have created invironment on AWS EC2 machine and executed my code over there. 
