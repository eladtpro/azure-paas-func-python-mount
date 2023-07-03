az webapp config storage-account update \            
--resource-group azure-openai \
--name func-python-mount \
--custom-id func-python-mount-id \
--storage-type AzureFiles \
--share-name media \
--account-name stfunctionsopenai \
--mount-path /media \
--access-key XXXXXXXXXXXXXXXXXXXXXXXXXX==
{
  "func-python-mount-id": {
    "accessKey": "XXXXXXXXXXXXXXXXXXXXXXXXXX==",
    "accountName": "stfunctionsopenai",
    "mountPath": "/media",
    "shareName": "media",
    "state": "Ok",
    "type": "AzureFiles"
  }
}