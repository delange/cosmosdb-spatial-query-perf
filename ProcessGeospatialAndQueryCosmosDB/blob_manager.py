from azure.core.exceptions import ResourceExistsError
from azure.storage.blob import BlobClient, BlobServiceClient, ContainerClient


class blob_manager:
    def __init__(self, connection_string):
        self.connection_string = connection_string

    def blob_already_exists(self, container, blob_name):
        """ Queries for the properties of a blob.
            Returns true if the blob exists, otherwise false."""

        blob_service_client = BlobServiceClient.from_connection_string(self.connection_string)

        try:
            blob_service_client.create_container(container)
        except ResourceExistsError:
            pass

        blob_client = blob_service_client.get_blob_client(container=container, blob=blob_name)
        
        try:
            blob_client.get_blob_properties()
            return True
        except:
            return False
    
    def upload_file(self, local_file_path, container, blob_name):
        """ Uploads a local file into a blob storage container """
        blob_service_client = BlobServiceClient.from_connection_string(self.connection_string)

        try:
            blob_service_client.create_container(container)
        except ResourceExistsError:
            pass

        blob_client = blob_service_client.get_blob_client(container=container, blob=blob_name)
        with open(local_file_path, "rb") as data:
            blob_client.upload_blob(data)

    def download_file(self, local_file_path, container, blob_name):
        """Downloads a file from a blob storage container.
            Returns the local file path of the downloaded file."""
        blob_service_client = BlobServiceClient.from_connection_string(self.connection_string)

        blob_client = blob_service_client.get_blob_client(container=container, blob=blob_name)

        with open(local_file_path, "wb") as blob_file:
                blob_file.writelines([blob_client.download_blob().readall()])
            
        return local_file_path
