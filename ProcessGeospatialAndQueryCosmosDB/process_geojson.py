import os
import glob
import logging
from geojsplit import geojsplit
import geojson

# current working directory
wd = os.getcwd()

# path to the input folder with all of the netcdf files
geojson_folder = os.path.join(wd, "data", "input_footprints", "Hawaii")
output_folder = os.path.join(wd, "data", "output_footprints", "Hawaii")

# create the output folder if it doesn't already exist
if not os.path.exists(output_folder):
	logging.info("Creating output folder: {}".format(output_folder))
	os.makedirs(output_folder)

# get a list of all the .geojson files in the input folder
all_geojson_files = glob.glob(os.path.join(geojson_folder, "*.geojson"))

# loop through each of the input geojson files and create an output
logging.info("Checking for new geojson files:")
for geojsonFile in all_geojson_files:
	# process the raw geojson file
    geojsonData = geojsplit.GeoJSONBatchStreamer(geojsonFile)
    i=1
    for feature_collection in geojsonData.stream(batch=1):
        outputFile = os.path.join(output_folder + "\Hawaii" + str(i) + ".geojson")
        # write to output file
        with open(outputFile, 'w') as f:
            geojson.dump(feature_collection, f) 
        i=i+1

logging.info("Done'")

