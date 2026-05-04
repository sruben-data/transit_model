# Built-In
import zipfile
import csv
from io import StringIO, BytesIO
import datetime
import os
import uuid

# External
import requests
import schedule
import config
from google.transit import gtfs_realtime_pb2 # gtfs-realtime-bindings

# 1. Download and cache static GTFS
params = {"api_key": config.api_token, "operator_id": config.operator_id}

if __name__ == "__main__":
    pass