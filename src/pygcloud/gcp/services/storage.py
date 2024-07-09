"""
Google Cloud Storage

# Labels

* Cannot be added when creating a bucket
* `--clear-labels` cannot be used on the same command as `--update-labels`
* Updates should be put in one `--update-labels` or
  else inconsistent behavior is to be expected
* Thus, the current state of labels needs to be collected before updating
* `--remove-labels` must be used

**Note** there is no support for labels currently for buckets in pygcloud.

# References

* [Bucket Labels](https://cloud.google.com/storage/docs/using-bucket-labels)

@author: jldupont
"""
from pygcloud.models import Params, GCPServiceUpdatable


class StorageBucket(GCPServiceUpdatable):

    REQUIRES_UPDATE_AFTER_CREATE = False

    def __init__(self, name: str, *params: Params):
        super().__init__(name=name, ns="gcs")
        if params is not None:
            self.params = list(params)

    def params_describe(self):
        return [
            "storage", "buckets", "describe", f"gs://{self.name}",
            "--format", "json"
        ] + self.params

    def params_create(self):
        return [
            "storage", "buckets", "create", f"gs://{self.name}"
        ] + self.params

    def params_update(self):
        return [
            "storage", "buckets", "update", f"gs://{self.name}"
        ] + self.params
