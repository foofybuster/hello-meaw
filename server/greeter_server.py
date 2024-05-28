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
"""The Python implementation of the GRPC helloworld.Greeter server."""

from concurrent import futures
import logging

import grpc
import helloworld_pb2
import helloworld_pb2_grpc
import time
from ultralytics import YOLO
import functools


class Greeter(helloworld_pb2_grpc.GreeterServicer):
    global model
    def SayHello(self, request, context):
        return helloworld_pb2.HelloReply(message="Hello, %s!" % request.name)
    def Doopzeem(self, request_iterator, context):
        start_time = time.time()
        for frame in request_iterator:
          results = model.predict(frame.name)
          if any(results[0].boxes.cls):
            result = functools.reduce(lambda x, y : x.names[int(x.boxes.cls)] + y.names[int(y.boxes.cls)], results)
            result = "" if result == None else result
            try:
              result = result if type(result) == str else result.names[int(result.boxes.cls)]
            except:
              result = result if type(result) == str else result.names[int(result.boxes.cls[0])]
            yield helloworld_pb2.HelloRequest(name=result)
#        elapsed_time = time.time() - start_time
#        return helloworld_pb2.FrameSummary(
#          elapsed_time=int(elapsed_time),
#          result=1
#    )


def serve():
    global model
    model = YOLO("yolov8n.pt")
    model.fuse()
    port = "50051"
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    helloworld_pb2_grpc.add_GreeterServicer_to_server(Greeter(), server)
    server.add_insecure_port("[::]:" + port)
    server.start()
    print("Server started, listening on " + port)
    server.wait_for_termination()


if __name__ == "__main__":
    logging.basicConfig()
    serve()
