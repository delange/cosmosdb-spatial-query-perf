

# Geospatial queries on CosmosDB and Azure Synapse Analytics

In this repository you will find the code and pipelines to run geospatial queries against an Azure Cosmos DB instance. While focussing here on the data ingestion and queries, we also made the connection to Azure Synapse Analytics, in order to perform large scale, big data processing on a Spark cluster with the data stored in Cosmos DB.

This repository is the technical back-bone from the .. blog post where the exeriments and the results are described.

As input data for the experiments we make use of the US building footprints, that have been created through a deeplearning approach on aerial photos resulting in more than 100 milion building footprints. The source data can be found at: https://github.com/microsoft/USBuildingFootprints 

![Image of Project](/img/footprints.jpg)


### General set-up

Here, two approaches are presented:
- the common usage pattern: direct data ingestion into CosmosDB and usage from Azure Synapse Analytics
- the experiment set-up: data preprocessing to accomadate the experiments before data ingestion into CosmosDB and queries from a VM with a C# application

![Set-up of Project](/img/Architecture.jpg)


### Common usage pattern



