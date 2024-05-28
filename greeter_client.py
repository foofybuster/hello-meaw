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
import os

def entry_request_iterator():
  #for frame in os.listdir("/Users/pornprom/Downloads/exam"):#["https://www.youtube.com/watch?v=L3tsYC5OYhQ", "/Users/pornprom/Downloads/kitten.png", "/Users/pornprom/Downloads/S__5120023.jpg"]:
  for frame in ["/Users/pornprom/Downloads/nunu/kitten.png", "/Users/pornprom/Downloads/nunu/S__5120023.jpg"]:
    entry_request = helloworld_pb2.HelloRequest(name = frame)
    #entry_request = helloworld_pb2.HelloRequest(name = "{}{}".format("/Users/pornprom/Downloads/exam/", frame))
    yield entry_request

def run():
    # NOTE(gRPC Python Team): .close() is possible on a channel and should be
    # used in circumstances in which the with statement does not fit the needs
    # of the code.
    #print("Will try to greet world ...")
    #with grpc.insecure_channel("localhost:50051") as channel:
    #  stub = helloworld_pb2_grpc.GreeterStub(channel)
    #  response = stub.SayHello(helloworld_pb2.HelloRequest(name="you0"))
    #print("Greeter client received: " + response.message)
    #channel = grpc.insecure_channel(target="localhost:50051")
    channel = grpc.insecure_channel(target="localhost:9999")
    stub = helloworld_pb2_grpc.GreeterStub(channel=channel)
    for yoooo in stub.Doopzeem(entry_request_iterator()):
      print(yoooo)


if __name__ == "__main__":
    logging.basicConfig()
    run()
