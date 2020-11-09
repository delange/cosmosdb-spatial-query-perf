# Azure Data Factory pipelines

Three pipelines are given:
- main-pipe (for both experiments and common usage)
- ingest to Cosmos DB from unzip (for common usage)
- ingest to Cosmos DB from split (for experiments)

## main-pipe


## ingest to Cosmos DB from unzip


## ingest to Cosmos DB from split




# ADF implementation for loading geojson

This folder contains an ADF-only implementation for loading featurs from a geojson file into CosmosDB. The geojson is split into individual features by a copy activity, and loaded as one feature per document. 

### Copy Activity

The activity adds two properties into each feature, to provide candidates for use as a partition key:
- filename of source geojson
- guid (generated, same value for all features in the file)

  <img src="./img/source-config.jpg" width=500px />

In the output, these are mapped to: 
- properties.state
- properties.partitionKey

  <img src="./img/mapping.jpg" width=500px />


The [pipeline](./pipeline) folder contains a simple pipeline that holds only the single copy activity. This assumes that the geojson has already been unzipped and stored in blobstore as a geojson file in a separate copy activity step. 

The [source dataset](./dataset/geojson.json) is a hardcoded pointer to a specfic file - this could be paramterised in the pipeline.

The [sink](./dataset/CosmosDbSqlApiCollection1.json) is a Cosmos DB with an existing database called `geojson` and a container called `features`. The partition key must be set to either `/properties/partitionKey` or `/properties/state`.

> **Note: This sample is not optimised or throttled for copy performance. Suggest scaling up RU's and turning off indexing in Cosmos DB for the initial import.**



