import os
import sys
import tempfile
import uuid
from pathlib import Path
from geojsplit import geojsplit
import geojson
from azure.core.exceptions import ResourceExistsError
from azure.storage.blob import BlobClient, BlobServiceClient, ContainerClient

sys.path.insert(1, './ProcessGeospatialAndQueryCosmosDB') # in vscode, the other .py files were not seen, normaly, this line should be omitted 

import constants
from blob_manager import blob_manager


def split_geojson(in_geojson, out_path, n_features):
    """
    Split geojson file in smaller geojson files, each exist of x features (x to be set).
    :param in_geojson: Input geojson
    :param out_path: Local path to the created smaller geojson files
    :param n_features: Number of features to store per geojson
    """

    geojsonData = geojsplit.GeoJSONBatchStreamer(in_geojson)

    i=1
    for feature_collection in geojsonData.stream(batch=n_features):
        outputFile = os.path.join(out_path, Path(in_geojson).stem + str(i) + ".geojson")
        # write to output file to local destination
        with open(outputFile, 'w') as f:
            geojson.dump(feature_collection, f) 
        # upload output file to blob
        bm.upload_file(outputFile, 'footprints', os.path.join("statesgeojson_example/split", Path(in_geojson).stem, os.path.basename(outputFile)))
        i=i+1
    return None

# create blob connection
bm = blob_manager(constants.blob_connection_str)

in_geojson = sys.argv[1]
#in_geojson = "Alaska.geojson"

temp_path = os.path.join(tempfile.gettempdir(), str(uuid.uuid4()))
local_file_path = os.path.join(temp_path, Path(in_geojson).stem)
os.makedirs(local_file_path)
local_file_path_out = os.path.join(local_file_path, "split")
os.makedirs(local_file_path_out)
local_geojson_path = os.path.join(local_file_path, in_geojson)

local_geojson_file = bm.download_file(local_geojson_path, 'footprints', os.path.join("statesunzip_example", in_geojson))
split_geojson(local_geojson_file,local_file_path_out,10000)