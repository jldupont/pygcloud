"""
@author: jldupont
"""

# gcloud projects get-iam-policy $PROJECT_ID
#
PROJECT_BINDINGS = """
{
  "bindings": [
    {
      "members": [
        "serviceAccount:service-215695389495@gcp-sa-artifactregistry.iam.gserviceaccount.com"
      ],
      "role": "roles/artifactregistry.serviceAgent"
    },
    {
      "members": [
        "serviceAccount:215695389495@cloudbuild.gserviceaccount.com"
      ],
      "role": "roles/cloudbuild.builds.builder"
    },
    {
      "members": [
        "serviceAccount:service-215695389495@gcp-sa-cloudbuild.iam.gserviceaccount.com"
      ],
      "role": "roles/cloudbuild.serviceAgent"
    },
    {
      "members": [
        "serviceAccount:service-215695389495@compute-system.iam.gserviceaccount.com"
      ],
      "role": "roles/compute.serviceAgent"
    },
    {
      "members": [
        "serviceAccount:service-215695389495@containerregistry.iam.gserviceaccount.com"
      ],
      "role": "roles/containerregistry.ServiceAgent"
    },
    {
      "members": [
        "serviceAccount:280761648870@cloudbuild.gserviceaccount.com"
      ],
      "role": "roles/datastore.owner"
    },
    {
      "members": [
        "serviceAccount:215695389495-compute@developer.gserviceaccount.com",
        "serviceAccount:215695389495@cloudservices.gserviceaccount.com",
        "serviceAccount:280761648870@cloudbuild.gserviceaccount.com"
      ],
      "role": "roles/editor"
    },
    {
      "members": [
        "serviceAccount:service-215695389495@firebase-rules.iam.gserviceaccount.com"
      ],
      "role": "roles/firebaserules.system"
    },
    {
      "members": [
        "serviceAccount:service-215695389495@gcp-sa-firestore.iam.gserviceaccount.com"
      ],
      "role": "roles/firestore.serviceAgent"
    },
    {
      "members": [
        "serviceAccount:280761648870@cloudbuild.gserviceaccount.com"
      ],
      "role": "roles/iam.securityAdmin"
    },
    {
      "members": [
        "user:j@gmail.com",
        "user:x@y.com"
      ],
      "role": "roles/owner"
    },
    {
      "members": [
        "serviceAccount:service-215695389495@gcp-sa-pubsub.iam.gserviceaccount.com"
      ],
      "role": "roles/pubsub.serviceAgent"
    },
    {
      "members": [
        "serviceAccount:280761648870@cloudbuild.gserviceaccount.com"
      ],
      "role": "roles/run.admin"
    },
    {
      "members": [
        "serviceAccount:service-215695389495@gcp-sa-iap.iam.gserviceaccount.com"
      ],
      "role": "roles/run.invoker"
    },
    {
      "members": [
        "serviceAccount:service-215695389495@serverless-robot-prod.iam.gserviceaccount.com"
      ],
      "role": "roles/run.serviceAgent"
    }
  ],
  "etag": "BwYb_QmEX_U=",
  "version": 1
}
"""
