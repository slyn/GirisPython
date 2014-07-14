#!/usr/bin/python3.4

from xmlrpc.server import SimpleXMLRPCServer
from xmlrpc.server import SimpleXMLRPCRequestHandler

class RequestHandler(SimpleXMLRPCRequestHandler):
    rpc_paths = ('/RPC2',)

server = SimpleXMLRPCServer(("localhost", 8000),
                            requestHandler=RequestHandler)
server.register_introspection_functions()

server.register_function(pow, 'us')

def toplama_fonksiyonu(x,y):
    return x + y
server.register_function(toplama_fonksiyonu, 'topla')

def cikarma_fonksiyonu(x,y):
	return x-y
server.register_function(cikarma_fonksiyonu, 'cikar') 

def carpma_fonksiyonu(x,y):
	return x*y
server.register_function(carpma_fonksiyonu,'carp')

def bolme_fonsiyonu(x,y):
	return x/y
server.register_function(bolme_fonsiyonu,'bol')

class MyFuncs:
    def mod(self, x, y):
        return x % y

server.register_instance(MyFuncs())

server.serve_forever()
