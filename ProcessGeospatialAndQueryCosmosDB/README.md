### Python code for running on Azure Batch

- process_geojson_batch.py : this script has one input parameter, namely the path to the geojson - but that will be parsed through Azure Data Factory pipeline. The script takes a geojson file, and adds an extra property (the state name) to each individual feature. It splits the original file into small geojson files of one feature each, and stores it back in blob.
- blob_manager.py : helper for dealing with blob storage
- constants.py : specifies a few details from your Azure resources

(- process_geojson.py : similar to process_geojson_batch.py but then a stand alone version, working away from Azure Batch)
