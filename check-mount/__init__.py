import logging
import azure.functions as func
import json
from os import listdir
import psutil

def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')
    mounts = psutil.disk_partitions()
    path = req.params.get('path')
    logging.info(f"Argument path: {path}. This HTTP triggered function executed successfully.")
    if path:
        items = [f for f in listdir(path)]
        finalObj = { 'items': items, 'mounts': mounts }
        jsonString = json.dumps(finalObj)
        logging.info(f"Argument jsonString: {jsonString}. This HTTP triggered function executed successfully.")
        return func.HttpResponse(
            jsonString,
            mimetype="application/json")
    else:
        return func.HttpResponse(
             "This HTTP triggered function executed successfully. Pass a path in the query string for a personalized response.",
             status_code=200
        )
