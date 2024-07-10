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

# Labels

* The parameter `--labels` is an alias for `--update-labels`.
* When `--clear-labels` is also specified along with `--labels`,
  clearing takes precedence

# References

* [Cloud Run](https://cloud.google.com/run/docs/deploying)
"""
from pygcloud.models import GCPServiceRevisionBased, Params
from pygcloud.gcp.labels import LabelGenerator


class CloudRun(GCPServiceRevisionBased, LabelGenerator):

    def __init__(self, name: str, *params: Params, region: str = None):
        super().__init__(name=name, ns="run")
        assert isinstance(region, str)
        self.params = list(params)
        self.region = region

    def params_describe(self):
        return [
            "run", "services", "describe", self.name,
            "--region", self.region,
            "--format", "json"
        ]

    def params_create(self):
        """
        The common parameters such as project_id would normally
        be injected through the Deployer.
        """
        return [
            "beta", "run", "deploy", self.name,
            "--clear-labels",
            "--region", self.region,
        ] + self.params + self.generate_use_labels()
