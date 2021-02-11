import os
import json
from django.db import models
from django.core import serializers
from aif import constants as aif
from xml.dom import minidom

export_type = "json"


def serialize_object(_file, path, data_object):
    try:
        filename = os.path.dirname(os.path.realpath(_file)) + path + "." + export_type
        print("serializing to", filename)
        serializer = serializers.get_serializer("json")()
        serializer.serialize(data_object.objects.all())
        with open(filename, "w") as out:
            if export_type == "json":
                out.write(json.dumps(json.loads(serializer.getvalue()), indent=4))
            else:  # export_type == "xml":
                out.write(minidom.parseString(serializer.getvalue()).toprettyxml(indent="   "))
    except FileNotFoundError:
        print("file not found")


def deserialize_object(_file, path, data_object):
    try:
        filename = os.path.dirname(os.path.realpath(_file)) + path + "." + export_type
        print("deserializing from", filename)
        with open(filename, "r") as file:
            data_object.objects.all().delete()
            for obj in serializers.deserialize(export_type, file.read()):
                obj.save()
    except FileNotFoundError:
        print("file not found")