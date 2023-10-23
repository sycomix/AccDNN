#!/usr/bin/env python

from settings import *
from caffe.proto import caffe_pb2
from google.protobuf import text_format

def readProtoFile(filepath, parser_object):
    with open(filepath, "r") as fd:
        if not fd:
            raise Exception(f"ERROR ({filepath})!")
        text_format.Merge(str(fd.read()), parser_object)
    return parser_object
