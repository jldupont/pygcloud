"""
@author: jldupont

gcloud beta run deploy ${_COMPONENT}  \
--source .  \
--no-allow-unauthenticated \
--region $_REGION     \
--project ${_PROJECT_ID}  \
--ingress internal-and-cloud-load-balancing \
--memory ${_MEMORY}   \
--execution-environment gen2 \
--add-volume name="blobs",type=cloud-storage,bucket="${_BLOBS_BUCKET}" \
--add-volume-mount volume="blobs",mount-path="${BLOB_MOUNT_PATH}" \
--set-env-vars "BLOB_MOUNT_PATH=${BLOB_MOUNT_PATH}" \
--command "/app/run.sh"
"""
from pygcloud.models import GCPServiceRevisionBased, Params


class CloudRun(GCPServiceRevisionBased):

    def __init__(self, name: str, *params: Params):
        self.name = name
        self.params = list(params)

    def params_create(self):
        """
        The common parameters such as project_id would normally
        be injected through the Deployer.
        """
        return [
            "beta", "run", "deploy", self.name
        ] + self.params
