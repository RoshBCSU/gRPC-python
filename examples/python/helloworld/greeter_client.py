# Copyright 2015 gRPC authors.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
"""The Python implementation of the GRPC helloworld.Greeter client."""

from __future__ import print_function

import logging

import grpc
import helloworld_pb2
import helloworld_pb2_grpc

def call_both_methods():
    # Create a channel to connect to the server
    channel = grpc.insecure_channel("196.168.56.1:50051")
   
    # Create a gRPC stub using the channel
    stub = helloworld_pb2_grpc.GreeterStub(channel)

    # Call the SayHello method
    response_hello = stub.SayHello(helloworld_pb2.HelloRequest(name="you"))
    print("Greeter client received (SayHello): " + response_hello.message)

    # Call the SayHelloAgain method
    response_hello_again = stub.SayHelloAgain(helloworld_pb2.HelloRequest(name="you"))
    print("Greeter client received (SayHelloAgain): " + response_hello_again.message)

def run():
    # NOTE(gRPC Python Team): .close() is possible on a channel and should be
    # used in circumstances in which the with statement does not fit the needs
    # of the code.
    print("Will try to greet world ...")
    with grpc.insecure_channel("196.168.56.1:50051") as channel:
        stub = helloworld_pb2_grpc.GreeterStub(channel)
        response = stub.SayHello(helloworld_pb2.HelloRequest(name="you"))
    print("Greeter client received: " + response.message)
    response = stub.SayHelloAgain(helloworld_pb2.HelloRequest(name='you'))
    print("Greeter client received: " + response.message)
    call_both_method()

if __name__ == "__main__":
    logging.basicConfig()
    run()
