import socketserver, sys
from subprocess import Popen, PIPE, STDOUT
# from Popen(command, shell=True, stdin=PIPE, stdout=PIPE, stderr=STDOUT)
# p = Popen(command, shell=True, stdin=PIPE, stdout=PIPE, stderr=STDOUT)
# output = temp.stdout.read()

# print output
from threading import Thread
from pprint import pprint
import json
import time

HOST = 'localhost'
PORT = 9527

# f1=open("ouput.json", "w")

class SingleTCPHandler(socketserver.BaseRequestHandler):
    "One instance per connection. Override handle(self) to customize action."
    def handle(self):
        # self.request is the client connection
        data = self.request.recv(1024)  # clip input at 1Kb
        text = data.decode('utf-8')
        record = json.loads(data)
        responsedata = []
        response = {}
        for command in record['commands']:
            message={}
            #list_cmd = command['method'].split(maxsplit=2)
            try:
                temp = Popen(command['method'], shell=True, stdin=PIPE, stdout=PIPE, stderr=STDOUT)
                message['output'] = str(temp.stdout.read())
                message['id']=command['id']
                message['stdout']=temp.stdout
                message['error']=temp.stderr
                print(message)
                time.sleep(1)

                # store the output in the list
                responsedata.append(message)
            except:
                print("Error")
        #print(responsedata)
        #print(type(responsedata))
        response["All response"] = responsedata
        response["records"]= "All commands"
        #print(response)
        #data_string = json.dumps(responsedata)
        #with open("output.json", "w") as outfile:
            #outfile.write(json.dumps(responsedata))
        self.request.send(bytes(json.dumps({"Status":"Success"}), 'UTF-8'))
        self.request.close()

class SimpleServer(socketserver.ThreadingMixIn, socketserver.TCPServer):
    # Ctrl-C will cleanly kill all spawned threads
    daemon_threads = True
    # much faster rebinding
    allow_reuse_address = True

    def __init__(self, server_address, RequestHandlerClass):
        socketserver.TCPServer.__init__(self, server_address, RequestHandlerClass)

if __name__ == "__main__":
    server = SimpleServer((HOST, PORT), SingleTCPHandler)
    # terminate with Ctrl-C
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        sys.exit(0)
