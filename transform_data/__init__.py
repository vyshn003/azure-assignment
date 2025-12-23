import azure.functions as func
from azure.storage.blob import BlobServiceClient

import os
import logging

def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info("Received req")
    try:
        conn_str = os.environ["AzureWebJobsStorage"]
        blob_service = BlobServiceClient.from_connection_string(conn_str)

        raw_container = blob_service.get_container_client("raw")
        processed_container = blob_service.get_container_client("processed")

        return func.HttpResponse("OK")
    except Exception as e:
        logging.error(f"Error: {str(e)}")
        return func.HttpResponse(f"Error: {str(e)}", status_code=501)
