from xmlrpc.server import SimpleXMLRPCServer
from xmlrpc.server import SimpleXMLRPCRequestHandler

# Restrict to a particular path.
class RequestHandler(SimpleXMLRPCRequestHandler):
    rpc_paths = ('/RPC2',)

# Create server
server = SimpleXMLRPCServer(("192.168.43.49", 8000), requestHandler=RequestHandler,allow_none=True)
server.register_introspection_functions()

def adder_function(x,y):
    return (x + y)
server.register_function(adder_function, 'Add')

def Multiply_function(x,y):
    return (x * y)
server.register_function(Multiply_function, 'Mul')

def Divided_function(x,y):
    return (x / y)
server.register_function(Divided_function, 'Div')

def Substract_function(x,y):
    if x < y:
        a = y - x
    else:
        a = x - y
    return a
server.register_function(Substract_function, 'Sub')

server.serve_forever()