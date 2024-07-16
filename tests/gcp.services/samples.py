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

IP_ADDRESS = """
{
  "address": "34.144.203.24",
  "addressType": "EXTERNAL",
  "creationTimestamp": "2024-05-08T08:41:32.180-07:00",
  "description": "",
  "id": "7020168853507679171",
  "ipVersion": "IPV4",
  "kind": "compute#address",
  "labelFingerprint": "42WmSpB8rSM=",
  "name": "ingress-proxy-ip",
  "networkTier": "PREMIUM",
  "selfLink": "https://www.googleapis.com/compute/v1/projects/PROJECT/global/addresses/ingress-proxy-ip",
  "status": "IN_USE",
  "users": [
    "https://www.googleapis.com/compute/v1/projects/PROJECT/global/forwardingRules/fwd-proxy-service"
  ]
}
"""   # NOQA

CLOUD_RUN_REVISION_SPEC = """
{
  "apiVersion": "serving.knative.dev/v1",
  "kind": "Service",
  "metadata": {
    "annotations": {
      "run.googleapis.com/client-name": "gcloud",
      "run.googleapis.com/client-version": "483.0.0",
      "run.googleapis.com/ingress": "internal-and-cloud-load-balancing",
      "run.googleapis.com/ingress-status": "internal-and-cloud-load-balancing",
      "run.googleapis.com/launch-stage": "BETA",
      "run.googleapis.com/operation-id": "6e52862c-84a1-4805-a5ee-57bf3473555a",
      "serving.knative.dev/creator": "280761648870@cloudbuild.gserviceaccount.com",
      "serving.knative.dev/lastModifier": "280761648870@cloudbuild.gserviceaccount.com"
    },
    "creationTimestamp": "2024-05-08T13:19:53.805059Z",
    "generation": 71,
    "labels": {
      "cloud.googleapis.com/location": "northamerica-northeast1"
    },
    "name": "SERVICE",
    "namespace": "215695389495",
    "resourceVersion": "AAYc54GvVGU",
    "selfLink": "/apis/serving.knative.dev/v1/namespaces/215695389495/services/SERVICE",
    "uid": "165ad2e2-0c5d-475d-af49-6b45b4a5a007"
  },
  "spec": {
    "template": {
      "metadata": {
        "annotations": {
          "autoscaling.knative.dev/maxScale": "100",
          "run.googleapis.com/client-name": "gcloud",
          "run.googleapis.com/client-version": "483.0.0",
          "run.googleapis.com/execution-environment": "gen2",
          "run.googleapis.com/startup-cpu-boost": "true"
        },
        "labels": {
          "client.knative.dev/nonce": "cotyygbwzm",
          "run.googleapis.com/startupProbeType": "Default"
        }
      },
      "spec": {
        "containerConcurrency": 80,
        "containers": [
          {
            "command": [
              "/app/run.sh"
            ],
            "env": [
              {
                "name": "BLOB_MOUNT_PATH",
                "value": "/tmp/_blobs"
              }
            ],
            "image": "northamerica-northeast1-docker.pkg.dev/SERVICE/cloud-run-source-deploy/SERVICE@sha256:10236cf86a0cdae06a147e72056ef5a0940edf53ebf5026d23bd840d016685c8",
            "ports": [
              {
                "containerPort": 8080,
                "name": "http1"
              }
            ],
            "resources": {
              "limits": {
                "cpu": "1000m",
                "memory": "512Mi"
              }
            },
            "startupProbe": {
              "failureThreshold": 1,
              "periodSeconds": 240,
              "tcpSocket": {
                "port": 8080
              },
              "timeoutSeconds": 240
            },
            "volumeMounts": [
              {
                "mountPath": "/tmp/_blobs",
                "name": "blobs"
              }
            ]
          }
        ],
        "serviceAccountName": "215695389495-compute@developer.gserviceaccount.com",
        "timeoutSeconds": 300,
        "volumes": [
          {
            "csi": {
              "driver": "gcsfuse.run.googleapis.com",
              "volumeAttributes": {
                "bucketName": "XYZ-SERVICE-files-dev"
              }
            },
            "name": "blobs"
          }
        ]
      }
    },
    "traffic": [
      {
        "latestRevision": true,
        "percent": 100
      }
    ]
  },
  "status": {
    "address": {
      "url": "https://SERVICE-4ro7a33l3a-nn.a.run.app"
    },
    "conditions": [
      {
        "lastTransitionTime": "2024-07-10T16:54:59.038309Z",
        "status": "True",
        "type": "Ready"
      },
      {
        "lastTransitionTime": "2024-05-08T13:19:54.492116Z",
        "status": "True",
        "type": "ConfigurationsReady"
      },
      {
        "lastTransitionTime": "2024-07-10T16:54:59.014028Z",
        "status": "True",
        "type": "RoutesReady"
      }
    ],
    "latestCreatedRevisionName": "SERVICE-00071-q56",
    "latestReadyRevisionName": "SERVICE-00071-q56",
    "observedGeneration": 71,
    "traffic": [
      {
        "latestRevision": true,
        "percent": 100,
        "revisionName": "SERVICE-00071-q56"
      }
    ],
    "url": "https://SERVICE-4ro7a33l3a-nn.a.run.app"
  }
}
"""  # NOQA

BACKEND_SERVICE = """
{
  "affinityCookieTtlSec": 0,
  "backends": [
    {
      "balancingMode": "UTILIZATION",
      "capacityScaler": 1.0,
      "group": "https://www.googleapis.com/compute/v1/projects/SERVICE/regions/northamerica-northeast1/networkEndpointGroups/backend-neg"
    }
  ],
  "connectionDraining": {
    "drainingTimeoutSec": 0
  },
  "creationTimestamp": "2024-05-08T17:28:46.445-07:00",
  "description": "",
  "enableCDN": false,
  "fingerprint": "HDHonjhFZmg=",
  "iap": {
    "enabled": true,
    "oauth2ClientId": "215695389495-kv6g4u53mdkmc5s9olhr3r9nusahnvbl.apps.googleusercontent.com",
    "oauth2ClientSecretSha256": "3a949ba4ab5c8124e553d89853ea38441d33e92830b64a88637e1bef8aef2974"
  },
  "id": "6598618698168247889",
  "kind": "compute#backendService",
  "loadBalancingScheme": "EXTERNAL",
  "logConfig": {
    "enable": true,
    "optionalMode": "EXCLUDE_ALL_OPTIONAL",
    "sampleRate": 1.0
  },
  "name": "backend-service",
  "port": 80,
  "portName": "http",
  "protocol": "HTTPS",
  "selfLink": "https://www.googleapis.com/compute/v1/projects/SERVICE/global/backendServices/backend-service",
  "sessionAffinity": "NONE",
  "timeoutSec": 30,
  "usedBy": [
    {
      "reference": "https://www.googleapis.com/compute/v1/projects/SERVICE/global/urlMaps/urlmap-backend-service"
    }
  ]
}
"""  # NOQA

SSL_CERTIFICATE = """
{
  "certificate": "-----BEGIN CERTIFICATE----------END CERTIFICATE-----",
  "creationTimestamp": "2024-05-08T17:29:37.626-07:00",
  "expireTime": "2024-10-02T14:06:37.000-07:00",
  "id": "626735018341934622",
  "kind": "compute#sslCertificate",
  "managed": {
    "domainStatus": {
      "DOMAIN": "ACTIVE"
    },
    "domains": [
      "DOMAIN"
    ],
    "status": "ACTIVE"
  },
  "name": "proxy-certificate",
  "selfLink": "https://www.googleapis.com/compute/v1/projects/PROJECT/global/sslCertificates/proxy-certificate",
  "subjectAlternativeNames": [
    "DOMAIN"
  ],
  "type": "MANAGED"
}"""  # NOQA

FWD_RULE = """
{
  "IPAddress": "34.144.203.24",
  "IPProtocol": "TCP",
  "creationTimestamp": "2024-05-08T17:29:46.798-07:00",
  "description": "",
  "fingerprint": "ltpTu3jOepo=",
  "id": "432872022940427797",
  "kind": "compute#forwardingRule",
  "labelFingerprint": "42WmSpB8rSM=",
  "loadBalancingScheme": "EXTERNAL",
  "name": "fwd-proxy-service",
  "networkTier": "PREMIUM",
  "portRange": "443-443",
  "selfLink": "https://www.googleapis.com/compute/v1/projects/PROJECT/global/forwardingRules/fwd-proxy-service",
  "target": "https://www.googleapis.com/compute/v1/projects/PROJECT/global/targetHttpsProxies/proxy-service"
}
"""  # NOQA

STORAGE_BUCKET = """
{
  "acl": [
    {
      "entity": "project-owners-215695389495",
      "projectTeam": {
        "projectNumber": "215695389495",
        "team": "owners"
      },
      "role": "OWNER"
    },
    {
      "entity": "project-editors-215695389495",
      "projectTeam": {
        "projectNumber": "215695389495",
        "team": "editors"
      },
      "role": "OWNER"
    },
    {
      "entity": "project-viewers-215695389495",
      "projectTeam": {
        "projectNumber": "215695389495",
        "team": "viewers"
      },
      "role": "READER"
    }
  ],
  "creation_time": "2024-06-04T00:58:08+0000",
  "default_acl": [
    {
      "entity": "project-owners-215695389495",
      "projectTeam": {
        "projectNumber": "215695389495",
        "team": "owners"
      },
      "role": "OWNER"
    },
    {
      "entity": "project-editors-215695389495",
      "projectTeam": {
        "projectNumber": "215695389495",
        "team": "editors"
      },
      "role": "OWNER"
    },
    {
      "entity": "project-viewers-215695389495",
      "projectTeam": {
        "projectNumber": "215695389495",
        "team": "viewers"
      },
      "role": "READER"
    }
  ],
  "default_storage_class": "STANDARD",
  "location": "US",
  "location_type": "multi-region",
  "metageneration": 14,
  "name": "bucket",
  "public_access_prevention": "enforced",
  "rpo": "DEFAULT",
  "soft_delete_policy": {
    "effectiveTime": "2024-06-04T00:58:08.161000+00:00",
    "retentionDurationSeconds": "604800"
  },
  "storage_url": "gs://bucket/",
  "uniform_bucket_level_access": false,
  "update_time": "2024-07-10T17:01:30+0000"
}
"""  # NOQA

HTTPS_PROXY = """
{
  "creationTimestamp": "2024-05-08T17:29:42.215-07:00",
  "fingerprint": "0dY8ZxQRKOk=",
  "id": "1964828312724416025",
  "kind": "compute#targetHttpsProxy",
  "name": "proxy-service",
  "quicOverride": "NONE",
  "selfLink": "https://www.googleapis.com/compute/v1/projects/PROJECT/global/targetHttpsProxies/proxy-service",
  "sslCertificates": [
    "https://www.googleapis.com/compute/v1/projects/PROJECT/global/sslCertificates/proxy-certificate"
  ],
  "tlsEarlyData": "DISABLED",
  "urlMap": "https://www.googleapis.com/compute/v1/projects/PROJECT/global/urlMaps/urlmap-backend-service"
}
"""  # NOQA

SCHEDULER_JOB = """
{
  "name": "projects/PROJECT/locations/northamerica-northeast1/jobs/test-job",
  "pubsubTarget": {
    "data": "dGVzdA==",
    "topicName": "projects/PROJECT/topics/test"
  },
  "retryConfig": {
    "maxBackoffDuration": "3600s",
    "maxDoublings": 16,
    "maxRetryDuration": "0s",
    "minBackoffDuration": "5s"
  },
  "schedule": "0 */3 * * *",
  "state": "ENABLED",
  "timeZone": "Etc/UTC",
  "userUpdateTime": "2024-07-15T11:41:07Z"
}
"""  # NOQA

PUBSUB_TOPIC = """
{
  "name": "projects/PROJECT/topics/test"
}
"""  # NOQA


SERVICES_LIST = r'''
[
  {
    "config": {
      "authentication": {},
      "documentation": {
        "summary": "Train high-quality custom machine learning models with minimal machine learning expertise and effort."
      },
      "monitoredResources": [
        {
          "description": "A Vertex AI Deployment Resource Pool.",
          "displayName": "Vertex AI Deployment Resource Pool",
          "labels": [
            {
              "description": "The identifier of the GCP Project owning the Deployment Resource Pool.",
              "key": "resource_container"
            },
            {
              "description": "The region in which the service is running.",
              "key": "location"
            },
            {
              "description": "The ID of the Deployment Resource Pool.",
              "key": "deployment_resource_pool_id"
            }
          ],
          "launchStage": "BETA",
          "type": "aiplatform.googleapis.com/DeploymentResourcePool"
        },
        {
          "description": "A Vertex AI API Endpoint where Models are deployed into it.",
          "displayName": "Vertex AI Endpoint",
          "labels": [
            {
              "description": "The identifier of the GCP Project owning the Endpoint.",
              "key": "resource_container"
            },
            {
              "description": "The region in which the service is running.",
              "key": "location"
            },
            {
              "description": "The ID of the Endpoint.",
              "key": "endpoint_id"
            }
          ],
          "launchStage": "BETA",
          "type": "aiplatform.googleapis.com/Endpoint"
        },
        {
          "description": "A Vertex AI Serving Cluster.",
          "displayName": "Vertex AI Serving Cluster",
          "labels": [
            {
              "description": "The identifier of the GCP User Project owning the cluster.",
              "key": "resource_container"
            },
            {
              "description": "The region in which the service is running.",
              "key": "location"
            },
            {
              "description": "The GKE name of the cluster.",
              "key": "cluster"
            }
          ],
          "launchStage": "PRELAUNCH",
          "type": "aiplatform.googleapis.com/ServingCluster"
        },
        {
          "description": "A Vertex AI Feature Store.",
          "displayName": "Vertex AI Feature Store",
          "labels": [
            {
              "description": "The identifier of the GCP Project owning the Featurestore.",
              "key": "resource_container"
            },
            {
              "description": "The region in which the service is running.",
              "key": "location"
            },
            {
              "description": "The ID of the Featurestore.",
              "key": "featurestore_id"
            }
          ],
          "launchStage": "BETA",
          "type": "aiplatform.googleapis.com/Featurestore"
        },
        {
          "description": "A Vertex AI Feature Online Store.",
          "displayName": "Vertex AI Feature Online Store",
          "labels": [
            {
              "description": "The identifier of the GCP Project owning the FeatureOnlineStore.",
              "key": "resource_container"
            },
            {
              "description": "The region in which the service is running.",
              "key": "location"
            },
            {
              "description": "The ID of the Feature Online Store.",
              "key": "feature_online_store_id"
            }
          ],
          "launchStage": "BETA",
          "type": "aiplatform.googleapis.com/FeatureOnlineStore"
        },
        {
          "description": "An Index built through the cloud Matching Engine service.",
          "displayName": "Matching Engine Index",
          "labels": [
            {
              "description": "The identifier of the GCP Project owning the Index.",
              "key": "resource_container"
            },
            {
              "description": "The region in which the service is running.",
              "key": "location"
            },
            {
              "description": "The ID of the Index.",
              "key": "index_id"
            }
          ],
          "launchStage": "BETA",
          "type": "aiplatform.googleapis.com/Index"
        },
        {
          "description": "An Endpoint to which Matching Engine Indexes are deployed.",
          "displayName": "Matching Engine Index Endpoint",
          "labels": [
            {
              "description": "The identifier of the GCP Project owning the Index.",
              "key": "resource_container"
            },
            {
              "description": "The region in which the service is running.",
              "key": "location"
            },
            {
              "description": "The ID of the index endpoint.",
              "key": "index_endpoint_id"
            }
          ],
          "launchStage": "BETA",
          "type": "aiplatform.googleapis.com/IndexEndpoint"
        },
        {
          "description": "A Vertex Pipelines Job.",
          "displayName": "Vertex Pipelines Job",
          "labels": [
            {
              "description": "The identifier of the GCP project associated with this resource, such as \"my-project\".",
              "key": "resource_container"
            },
            {
              "description": "The region in which the service is running.",
              "key": "location"
            },
            {
              "description": "The ID of the PipelineJob.",
              "key": "pipeline_job_id"
            }
          ],
          "launchStage": "BETA",
          "type": "aiplatform.googleapis.com/PipelineJob"
        },
        {
          "description": "A Google Cloud Project and region where a job is running.",
          "displayName": "Location",
          "labels": [
            {
              "description": "The identifier of the GCP project associated with this resource, such as \"my-project\".",
              "key": "resource_container"
            },
            {
              "description": "The region in which the service is running.",
              "key": "location"
            }
          ],
          "launchStage": "BETA",
          "type": "aiplatform.googleapis.com/Location"
        },
        {
          "description": "A Vertex AI Model.",
          "displayName": "Vertex AI Model",
          "labels": [
            {
              "description": "The identifier of the GCP Project owning the Model.",
              "key": "resource_container"
            },
            {
              "description": "The region in which the service is running.",
              "key": "location"
            },
            {
              "description": "The identifier of the Model.",
              "key": "model"
            }
          ],
          "launchStage": "BETA",
          "type": "aiplatform.googleapis.com/Model"
        },
        {
          "description": "A Vertex AI Notebook Runtime.",
          "displayName": "Vertex AI Notebook Runtime",
          "labels": [
            {
              "description": "The identifier of the GCP Project owning the Notebook Runtime.",
              "key": "resource_container"
            },
            {
              "description": "The region in which the notebook exists.",
              "key": "location"
            },
            {
              "description": "The identifier of the Notebook Runtime.",
              "key": "notebook_runtime_id"
            }
          ],
          "launchStage": "ALPHA",
          "type": "aiplatform.googleapis.com/NotebookRuntime"
        },
        {
          "description": "A Vertex AI Model Garden Publisher Model.",
          "displayName": "Vertex AI Model Garden Publisher Model",
          "labels": [
            {
              "description": "The identifier of the GCP Project owning the Endpoint.",
              "key": "resource_container"
            },
            {
              "description": "The region in which the service is running.",
              "key": "location"
            },
            {
              "description": "The publisher of the model.",
              "key": "publisher"
            },
            {
              "description": "The resource ID of the PublisherModel.",
              "key": "model_user_id"
            },
            {
              "description": "The version ID of the PublisherModel.",
              "key": "model_version_id"
            }
          ],
          "launchStage": "BETA",
          "type": "aiplatform.googleapis.com/PublisherModel"
        }
      ],
      "monitoring": {
        "consumerDestinations": [
          {
            "metrics": [
              "aiplatform.googleapis.com/prediction/internal/online/cmle_backend_latencies",
              "aiplatform.googleapis.com/prediction/internal/online/component_latencies",
              "aiplatform.googleapis.com/prediction/internal/online/core_infra_latencies",
              "aiplatform.googleapis.com/prediction/internal/online/custom/istio_request_duration_milliseconds",
              "aiplatform.googleapis.com/prediction/internal/online/custom/istio_requests_total",
              "aiplatform.googleapis.com/prediction/internal/online/custom/tfe_ie/tf_exit_total",
              "aiplatform.googleapis.com/prediction/internal/online/custom/tfe_ie/tf_launch_total",
              "aiplatform.googleapis.com/prediction/internal/online/custom/dynamic_loading/model_load_latencies",
              "aiplatform.googleapis.com/prediction/internal/online/custom/dynamic_loading/model_load_count",
              "aiplatform.googleapis.com/prediction/internal/online/custom/dynamic_loading/model_cache_lookup_count",
              "aiplatform.googleapis.com/prediction/internal/online/custom/dynamic_loading/model_states",
              "aiplatform.googleapis.com/prediction/internal/online/directpath_backend_latencies",
              "aiplatform.googleapis.com/prediction/internal/online/harpoon_backend_latencies",
              "aiplatform.googleapis.com/prediction/internal/online/llm_backend_latencies",
              "aiplatform.googleapis.com/prediction/internal/online/internal_error_count",
              "aiplatform.googleapis.com/prediction/internal/online/prediction_latencies",
              "aiplatform.googleapis.com/prediction/internal/online/request_byte_count",
              "aiplatform.googleapis.com/prediction/internal/online/response_count",
              "aiplatform.googleapis.com/prediction/internal/online/concurrent_requests",
              "aiplatform.googleapis.com/prediction/internal/online/throttled_request_count",
              "aiplatform.googleapis.com/prediction/internal/online/resource_usage_error_count",
              "aiplatform.googleapis.com/prediction/internal/online/lm_response_count",
              "aiplatform.googleapis.com/prediction/internal/online/lm_internal_error_count",
              "aiplatform.googleapis.com/prediction/internal/online/lm_internal_input_token_count",
              "aiplatform.googleapis.com/prediction/internal/online/lm_internal_input_character_count",
              "aiplatform.googleapis.com/prediction/internal/online/lm_internal_output_token_count",
              "aiplatform.googleapis.com/prediction/internal/online/lm_internal_output_character_count",
              "aiplatform.googleapis.com/prediction/internal/online/lm_prediction_latencies",
              "aiplatform.googleapis.com/prediction/internal/online/lvm_request_count",
              "aiplatform.googleapis.com/prediction/online/streaming_message_overhead_latencies",
              "aiplatform.googleapis.com/prediction/online/streaming_message_count",
              "aiplatform.googleapis.com/prediction/online/streaming_message_bytes_count",
              "aiplatform.googleapis.com/prediction/online/open_streams",
              "aiplatform.googleapis.com/prediction/online/error_count",
              "aiplatform.googleapis.com/prediction/online/prediction_count",
              "aiplatform.googleapis.com/prediction/online/prediction_latencies",
              "aiplatform.googleapis.com/prediction/online/response_count",
              "aiplatform.googleapis.com/prediction/online/replicas",
              "aiplatform.googleapis.com/prediction/online/target_replicas",
              "aiplatform.googleapis.com/prediction/internal/online/cpu/utilization",
              "aiplatform.googleapis.com/prediction/internal/online/memory/bytes_used",
              "aiplatform.googleapis.com/prediction/internal/online/accelerator/duty_cycle",
              "aiplatform.googleapis.com/prediction/internal/online/accelerator/memory/bytes_used",
              "aiplatform.googleapis.com/prediction/internal/online/network/received_bytes_count",
              "aiplatform.googleapis.com/prediction/internal/online/network/sent_bytes_count",
              "aiplatform.googleapis.com/prediction/internal/online/l2_operator_reconcile_latencies",
              "aiplatform.googleapis.com/prediction/internal/online/lm_internal_weighted_input_output_token_count"
            ],
            "monitoredResource": "aiplatform.googleapis.com/Endpoint"
          },
          {
            "metrics": [
              "aiplatform.googleapis.com/prediction/online/deployment_resource_pool/replicas",
              "aiplatform.googleapis.com/prediction/online/deployment_resource_pool/target_replicas",
              "aiplatform.googleapis.com/prediction/online/deployment_resource_pool/cpu/utilization",
              "aiplatform.googleapis.com/prediction/online/deployment_resource_pool/memory/bytes_used",
              "aiplatform.googleapis.com/prediction/online/deployment_resource_pool/accelerator/duty_cycle",
              "aiplatform.googleapis.com/prediction/online/deployment_resource_pool/accelerator/memory/bytes_used",
              "aiplatform.googleapis.com/prediction/online/deployment_resource_pool/network/received_bytes_count",
              "aiplatform.googleapis.com/prediction/online/deployment_resource_pool/network/sent_bytes_count"
            ],
            "monitoredResource": "aiplatform.googleapis.com/DeploymentResourcePool"
          },
          {
            "metrics": [
              "aiplatform.googleapis.com/scann/query/request_count",
              "aiplatform.googleapis.com/scann/query/latencies",
              "aiplatform.googleapis.com/scann/internal/query/latency_bucketized",
              "aiplatform.googleapis.com/matching_engine/query/request_count",
              "aiplatform.googleapis.com/matching_engine/query/query_count",
              "aiplatform.googleapis.com/matching_engine/query/request_count_v2",
              "aiplatform.googleapis.com/matching_engine/internal/query/request_count",
              "aiplatform.googleapis.com/matching_engine/query/latencies",
              "aiplatform.googleapis.com/matching_engine/query/query_latencies",
              "aiplatform.googleapis.com/matching_engine/internal/query/latency_bucketized",
              "aiplatform.googleapis.com/matching_engine/internal/query/match_server_request_count",
              "aiplatform.googleapis.com/matching_engine/internal/query/match_server_latencies"
            ],
            "monitoredResource": "aiplatform.googleapis.com/IndexEndpoint"
          },
          {
            "metrics": [
              "aiplatform.googleapis.com/scann/current_shards",
              "aiplatform.googleapis.com/scann/current_replicas",
              "aiplatform.googleapis.com/matching_engine/current_shards",
              "aiplatform.googleapis.com/matching_engine/current_replicas",
              "aiplatform.googleapis.com/matching_engine/internal/current_replicas",
              "aiplatform.googleapis.com/matching_engine/cpu/request_cores",
              "aiplatform.googleapis.com/matching_engine/cpu/request_utilization",
              "aiplatform.googleapis.com/matching_engine/memory/used_bytes",
              "aiplatform.googleapis.com/matching_engine/memory/request_bytes"
            ],
            "monitoredResource": "aiplatform.googleapis.com/IndexEndpoint"
          },
          {
            "metrics": [
              "aiplatform.googleapis.com/matching_engine/stream_update/datapoint_count",
              "aiplatform.googleapis.com/matching_engine/stream_update/latency",
              "aiplatform.googleapis.com/matching_engine/stream_update/latencies",
              "aiplatform.googleapis.com/matching_engine/internal/stream_update/catchup_latency",
              "aiplatform.googleapis.com/matching_engine/stream_update/request_count",
              "aiplatform.googleapis.com/matching_engine/index/size",
              "aiplatform.googleapis.com/matching_engine/index/embeddings",
              "aiplatform.googleapis.com/matching_engine/index/last_batch_update_time",
              "aiplatform.googleapis.com/matching_engine/index/last_compaction_time",
              "aiplatform.googleapis.com/matching_engine/report_index_shard_stats_to_gcs/request_count",
              "aiplatform.googleapis.com/matching_engine/empty_index/request_count"
            ],
            "monitoredResource": "aiplatform.googleapis.com/Index"
          },
          {
            "metrics": [
              "aiplatform.googleapis.com/featurestore/online_entities_updated",
              "aiplatform.googleapis.com/featurestore/online_serving/request_count",
              "aiplatform.googleapis.com/featurestore/online_serving/latencies",
              "aiplatform.googleapis.com/featurestore/online_serving/response_size",
              "aiplatform.googleapis.com/featurestore/online_serving/request_bytes_count",
              "aiplatform.googleapis.com/featurestore/streaming_write/offline_processed_count",
              "aiplatform.googleapis.com/featurestore/streaming_write/offline_write_delays"
            ],
            "monitoredResource": "aiplatform.googleapis.com/Featurestore"
          },
          {
            "metrics": [
              "aiplatform.googleapis.com/featurestore/storage/stored_bytes",
              "aiplatform.googleapis.com/featurestore/storage/billable_processed_bytes",
              "aiplatform.googleapis.com/featurestore/node_count",
              "aiplatform.googleapis.com/featurestore/cpu_load",
              "aiplatform.googleapis.com/featurestore/cpu_load_hottest_node"
            ],
            "monitoredResource": "aiplatform.googleapis.com/Featurestore"
          },
          {
            "metrics": [
              "aiplatform.googleapis.com/featureonlinestore/online_serving/request_count",
              "aiplatform.googleapis.com/featureonlinestore/online_serving/serving_bytes_count",
              "aiplatform.googleapis.com/featureonlinestore/online_serving/serving_latencies",
              "aiplatform.googleapis.com/featureonlinestore/serving_data_ages",
              "aiplatform.googleapis.com/featureonlinestore/serving_data_by_sync_time",
              "aiplatform.googleapis.com/feature_online_store/online_serving/internal/router/serving_latencies",
              "aiplatform.googleapis.com/feature_online_store/online_serving/internal/leaf/request_count",
              "aiplatform.googleapis.com/feature_online_store/online_serving/internal/leaf/serving_bytes_count",
              "aiplatform.googleapis.com/feature_online_store/online_serving/internal/leaf/latencies"
            ],
            "monitoredResource": "aiplatform.googleapis.com/FeatureOnlineStore"
          },
          {
            "metrics": [
              "aiplatform.googleapis.com/featureonlinestore/storage/stored_bytes",
              "aiplatform.googleapis.com/featureonlinestore/storage/bigtable_cpu_load",
              "aiplatform.googleapis.com/featureonlinestore/storage/bigtable_cpu_load_hottest_node",
              "aiplatform.googleapis.com/featureonlinestore/storage/bigtable_nodes",
              "aiplatform.googleapis.com/featureonlinestore/storage/optimized_nodes",
              "aiplatform.googleapis.com/featureonlinestore/running_sync",
              "aiplatform.googleapis.com/feature_online_store/online_serving/internal/router/memory/request_bytes",
              "aiplatform.googleapis.com/feature_online_store/online_serving/internal/router/memory/used_bytes",
              "aiplatform.googleapis.com/feature_online_store/online_serving/internal/router/cpu/request_utilization",
              "aiplatform.googleapis.com/feature_online_store/online_serving/internal/router/cpu/request_cores"
            ],
            "monitoredResource": "aiplatform.googleapis.com/FeatureOnlineStore"
          },
          {
            "metrics": [
              "aiplatform.googleapis.com/generate_content_input_tokens_per_minute_per_base_model",
              "aiplatform.googleapis.com/generate_content_requests_per_minute_per_project_per_base_model",
              "aiplatform.googleapis.com/online_prediction_requests_per_base_model",
              "aiplatform.googleapis.com/quota/generate_content_input_tokens_per_minute_per_base_model/exceeded",
              "aiplatform.googleapis.com/quota/generate_content_input_tokens_per_minute_per_base_model/usage",
              "aiplatform.googleapis.com/quota/generate_content_requests_per_day_per_project_per_base_model/exceeded",
              "aiplatform.googleapis.com/quota/generate_content_requests_per_day_per_project_per_base_model/usage",
              "aiplatform.googleapis.com/quota/generate_content_requests_per_minute_per_project_per_base_model/exceeded",
              "aiplatform.googleapis.com/quota/generate_content_requests_per_minute_per_project_per_base_model/usage",
              "aiplatform.googleapis.com/quota/long_running_online_prediction_requests_per_base_model/exceeded",
              "aiplatform.googleapis.com/quota/long_running_online_prediction_requests_per_base_model/usage",
              "aiplatform.googleapis.com/quota/online_prediction_dedicated_requests_per_base_model_version/exceeded",
              "aiplatform.googleapis.com/quota/online_prediction_dedicated_requests_per_base_model_version/usage",
              "aiplatform.googleapis.com/quota/online_prediction_dedicated_tokens_per_base_model_version/exceeded",
              "aiplatform.googleapis.com/quota/online_prediction_dedicated_tokens_per_base_model_version/usage",
              "aiplatform.googleapis.com/quota/online_prediction_output_tokens_per_minute_per_base_model/exceeded",
              "aiplatform.googleapis.com/quota/online_prediction_output_tokens_per_minute_per_base_model/usage",
              "aiplatform.googleapis.com/quota/online_prediction_requests_per_base_model/exceeded",
              "aiplatform.googleapis.com/quota/online_prediction_requests_per_base_model/usage",
              "aiplatform.googleapis.com/quota/online_prediction_requests_per_user_per_base_model/exceeded",
              "aiplatform.googleapis.com/quota/online_prediction_requests_per_user_per_base_model/usage",
              "aiplatform.googleapis.com/quota/shared_generate_content_requests_per_day_per_base_model/exceeded",
              "aiplatform.googleapis.com/quota/shared_generate_content_requests_per_day_per_base_model/usage",
              "aiplatform.googleapis.com/quota/shared_generate_content_requests_per_minute_per_base_model/exceeded",
              "aiplatform.googleapis.com/quota/shared_generate_content_requests_per_minute_per_base_model/usage",
              "aiplatform.googleapis.com/quota/shared_online_prediction_requests_per_base_model/exceeded",
              "aiplatform.googleapis.com/quota/shared_online_prediction_requests_per_base_model/usage"
            ],
            "monitoredResource": "aiplatform.googleapis.com/Location"
          },
          {
            "metrics": [
              "aiplatform.googleapis.com/executing_vertexai_pipeline_jobs",
              "aiplatform.googleapis.com/executing_vertexai_pipeline_tasks"
            ],
            "monitoredResource": "aiplatform.googleapis.com/Location"
          },
          {
            "metrics": [
              "aiplatform.googleapis.com/model_monitoring/feature_drift_deviation",
              "aiplatform.googleapis.com/model_monitoring/prediction_output_drift_deviation",
              "aiplatform.googleapis.com/model_monitoring/feature_attribution_deviation",
              "aiplatform.googleapis.com/model_monitoring/model_performance",
              "aiplatform.googleapis.com/model_monitoring/gen_ai_evaluation",
              "aiplatform.googleapis.com/model_monitoring/gen_ai_safety",
              "aiplatform.googleapis.com/model_monitoring/gen_ai_input_output",
              "aiplatform.googleapis.com/model_monitoring/gen_ai_grounding",
              "aiplatform.googleapis.com/model_monitoring/gen_ai_recitation"
            ],
            "monitoredResource": "aiplatform.googleapis.com/Model"
          },
          {
            "metrics": [
              "aiplatform.googleapis.com/pipelinejob/duration",
              "aiplatform.googleapis.com/pipelinejob/task_completed_count"
            ],
            "monitoredResource": "aiplatform.googleapis.com/PipelineJob"
          },
          {
            "metrics": [
              "aiplatform.googleapis.com/publisher/online_serving/model_invocation_count",
              "aiplatform.googleapis.com/publisher/online_serving/model_invocation_latencies",
              "aiplatform.googleapis.com/publisher/online_serving/first_token_latencies",
              "aiplatform.googleapis.com/publisher/online_serving/tokens",
              "aiplatform.googleapis.com/publisher/online_serving/token_count",
              "aiplatform.googleapis.com/publisher/online_serving/characters",
              "aiplatform.googleapis.com/publisher/online_serving/character_count",
              "aiplatform.googleapis.com/publisher/online_serving/consumed_throughput"
            ],
            "monitoredResource": "aiplatform.googleapis.com/PublisherModel"
          },
          {
            "metrics": [
              "aiplatform.googleapis.com/serving/controlplane/operator_reconcile_latency_seconds",
              "aiplatform.googleapis.com/serving/controlplane/operator_workqueue_unfinished_work_seconds",
              "aiplatform.googleapis.com/serving/controlplane/operator_workqueue_depth",
              "aiplatform.googleapis.com/serving/controlplane/operator_version",
              "aiplatform.googleapis.com/serving/controlplane/release_stage"
            ],
            "monitoredResource": "aiplatform.googleapis.com/ServingCluster"
          },
          {
            "metrics": [
              "aiplatform.googleapis.com/colab/internal/runtime/startup_duration",
              "aiplatform.googleapis.com/colab/internal/runtime/health",
              "aiplatform.googleapis.com/colab/internal/runtime/image_version",
              "aiplatform.googleapis.com/colab/internal/runtime/uptime",
              "aiplatform.googleapis.com/colab/internal/runtime/cpu/usage_time",
              "aiplatform.googleapis.com/colab/internal/runtime/memory/limit",
              "aiplatform.googleapis.com/colab/internal/runtime/memory/usage",
              "aiplatform.googleapis.com/colab/internal/runtime/container/memory/usage",
              "aiplatform.googleapis.com/colab/internal/runtime/disk/used_bytes",
              "aiplatform.googleapis.com/colab/internal/runtime/disk/reserved_bytes",
              "aiplatform.googleapis.com/colab/internal/runtime/disk/free_bytes",
              "aiplatform.googleapis.com/colab/internal/runtime/network/received_bytes_count",
              "aiplatform.googleapis.com/colab/internal/runtime/network/sent_bytes_count",
              "aiplatform.googleapis.com/colab/internal/runtime/container/restart_count"
            ],
            "monitoredResource": "aiplatform.googleapis.com/NotebookRuntime"
          },
          {
            "metrics": [
              "aiplatform.googleapis.com/quota/generate_content_input_tokens_per_minute_per_base_model/limit",
              "aiplatform.googleapis.com/quota/generate_content_requests_per_day_per_project_per_base_model/limit",
              "aiplatform.googleapis.com/quota/generate_content_requests_per_minute_per_project_per_base_model/limit",
              "aiplatform.googleapis.com/quota/long_running_online_prediction_requests_per_base_model/limit",
              "aiplatform.googleapis.com/quota/online_prediction_dedicated_requests_per_base_model_version/limit",
              "aiplatform.googleapis.com/quota/online_prediction_dedicated_tokens_per_base_model_version/limit",
              "aiplatform.googleapis.com/quota/online_prediction_output_tokens_per_minute_per_base_model/limit",
              "aiplatform.googleapis.com/quota/online_prediction_requests_per_base_model/limit",
              "aiplatform.googleapis.com/quota/online_prediction_requests_per_user_per_base_model/limit",
              "aiplatform.googleapis.com/quota/shared_generate_content_requests_per_day_per_base_model/limit",
              "aiplatform.googleapis.com/quota/shared_generate_content_requests_per_minute_per_base_model/limit",
              "aiplatform.googleapis.com/quota/shared_online_prediction_requests_per_base_model/limit"
            ],
            "monitoredResource": "aiplatform.googleapis.com/Location"
          }
        ]
      },
      "name": "aiplatform.googleapis.com",
      "quota": {},
      "title": "Vertex AI API",
      "usage": {
        "requirements": [
          "serviceusage.googleapis.com/tos/cloud",
          "serviceusage.googleapis.com/billing-enabled"
        ]
      }
    },
    "name": "projects/215695389495/services/aiplatform.googleapis.com",
    "parent": "projects/215695389495",
    "state": "ENABLED"
  },
  {
    "config": {
      "authentication": {},
      "documentation": {
        "summary": "Exchange data and analytics assets securely and efficiently."
      },
      "monitoring": {},
      "name": "analyticshub.googleapis.com",
      "quota": {},
      "title": "Analytics Hub API",
      "usage": {
        "requirements": [
          "serviceusage.googleapis.com/tos/cloud"
        ]
      }
    },
    "name": "projects/215695389495/services/analyticshub.googleapis.com",
    "parent": "projects/215695389495",
    "state": "ENABLED"
  },
  {
    "config": {
      "authentication": {},
      "documentation": {
        "summary": "Store and manage build artifacts in a scalable and integrated service built on Google infrastructure."
      },
      "monitoredResources": [
        {
          "description": "A location in Artifact Registry.",
          "displayName": "Artifact Registry Location",
          "labels": [
            {
              "description": "The identifier of the GCP resource container associated with this resource, such as \"my_project\" or \"organizations/5678\".",
              "key": "resource_container"
            },
            {
              "description": "Location of resource.",
              "key": "location"
            }
          ],
          "launchStage": "GA",
          "type": "artifactregistry.googleapis.com/Location"
        },
        {
          "description": "A Cloud project in Artifact Registry.",
          "displayName": "Artifact Registry Project",
          "labels": [
            {
              "description": "The identifier of the GCP resource container associated with this resource, such as \"my_project\" or \"organizations/5678\".",
              "key": "resource_container"
            },
            {
              "description": "Location of resource.",
              "key": "location"
            }
          ],
          "launchStage": "BETA",
          "type": "artifactregistry.googleapis.com/Project"
        },
        {
          "description": "A repository in Artifact Registry.",
          "displayName": "Artifact Registry Repository",
          "labels": [
            {
              "description": "The identifier of the GCP resource container associated with this resource, such as \"my_project\" or \"organizations/5678\".",
              "key": "resource_container"
            },
            {
              "description": "Location of resource.",
              "key": "location"
            },
            {
              "description": "The identifier of the Artifact Registry repository, such as \"my_repository\".",
              "key": "repository_id"
            }
          ],
          "launchStage": "BETA",
          "type": "artifactregistry.googleapis.com/Repository"
        }
      ],
      "monitoring": {
        "consumerDestinations": [
          {
            "metrics": [
              "artifactregistry.googleapis.com/asia_multi_region_upstream_host_reads",
              "artifactregistry.googleapis.com/europe_multi_region_upstream_host_reads",
              "artifactregistry.googleapis.com/project_asia_multi_region_upstream_host_reads",
              "artifactregistry.googleapis.com/project_europe_multi_region_upstream_host_reads",
              "artifactregistry.googleapis.com/project_region_upstream_host_reads",
              "artifactregistry.googleapis.com/project_us_multi_region_upstream_host_reads",
              "artifactregistry.googleapis.com/quota/asia_multi_region_upstream_host_reads/exceeded",
              "artifactregistry.googleapis.com/quota/asia_multi_region_upstream_host_reads/usage",
              "artifactregistry.googleapis.com/quota/europe_multi_region_upstream_host_reads/exceeded",
              "artifactregistry.googleapis.com/quota/europe_multi_region_upstream_host_reads/usage",
              "artifactregistry.googleapis.com/quota/project_asia_multi_region_upstream_host_reads/exceeded",
              "artifactregistry.googleapis.com/quota/project_asia_multi_region_upstream_host_reads/usage",
              "artifactregistry.googleapis.com/quota/project_europe_multi_region_upstream_host_reads/exceeded",
              "artifactregistry.googleapis.com/quota/project_europe_multi_region_upstream_host_reads/usage",
              "artifactregistry.googleapis.com/quota/project_region_upstream_host_reads/exceeded",
              "artifactregistry.googleapis.com/quota/project_region_upstream_host_reads/usage",
              "artifactregistry.googleapis.com/quota/project_us_multi_region_upstream_host_reads/exceeded",
              "artifactregistry.googleapis.com/quota/project_us_multi_region_upstream_host_reads/usage",
              "artifactregistry.googleapis.com/quota/region_upstream_host_reads/exceeded",
              "artifactregistry.googleapis.com/quota/region_upstream_host_reads/usage",
              "artifactregistry.googleapis.com/quota/us_multi_region_upstream_host_reads/exceeded",
              "artifactregistry.googleapis.com/quota/us_multi_region_upstream_host_reads/usage",
              "artifactregistry.googleapis.com/region_upstream_host_reads",
              "artifactregistry.googleapis.com/us_multi_region_upstream_host_reads"
            ],
            "monitoredResource": "artifactregistry.googleapis.com/Location"
          },
          {
            "metrics": [
              "artifactregistry.googleapis.com/project/api/request_count",
              "artifactregistry.googleapis.com/project/api/request_latencies",
              "artifactregistry.googleapis.com/project/request_count",
              "artifactregistry.googleapis.com/project/request_latencies"
            ],
            "monitoredResource": "artifactregistry.googleapis.com/Project"
          },
          {
            "metrics": [
              "artifactregistry.googleapis.com/repository/api/request_count",
              "artifactregistry.googleapis.com/repository/api/request_latencies",
              "artifactregistry.googleapis.com/repository/request_count",
              "artifactregistry.googleapis.com/repository/request_latencies",
              "artifactregistry.googleapis.com/repository/size"
            ],
            "monitoredResource": "artifactregistry.googleapis.com/Repository"
          },
          {
            "metrics": [
              "artifactregistry.googleapis.com/quota/asia_multi_region_upstream_host_reads/limit",
              "artifactregistry.googleapis.com/quota/europe_multi_region_upstream_host_reads/limit",
              "artifactregistry.googleapis.com/quota/project_asia_multi_region_upstream_host_reads/limit",
              "artifactregistry.googleapis.com/quota/project_europe_multi_region_upstream_host_reads/limit",
              "artifactregistry.googleapis.com/quota/project_region_upstream_host_reads/limit",
              "artifactregistry.googleapis.com/quota/project_us_multi_region_upstream_host_reads/limit",
              "artifactregistry.googleapis.com/quota/region_upstream_host_reads/limit",
              "artifactregistry.googleapis.com/quota/us_multi_region_upstream_host_reads/limit"
            ],
            "monitoredResource": "artifactregistry.googleapis.com/Location"
          }
        ]
      },
      "name": "artifactregistry.googleapis.com",
      "quota": {},
      "title": "Artifact Registry API",
      "usage": {
        "requirements": [
          "serviceusage.googleapis.com/tos/cloud",
          "serviceusage.googleapis.com/billing-enabled"
        ]
      }
    },
    "name": "projects/215695389495/services/artifactregistry.googleapis.com",
    "parent": "projects/215695389495",
    "state": "ENABLED"
  },
  {
    "config": {
      "authentication": {},
      "documentation": {
        "summary": "A data platform for customers to create, manage, share and query data."
      },
      "monitoredResources": [
        {
          "description": "BigQuery Table Resource.",
          "displayName": "BigQuery Table Resource.",
          "labels": [
            {
              "description": "The identifier of the GCP resource container associated with this resource, such as \"my-project\" or \"organizations/123\".",
              "key": "resource_container"
            },
            {
              "description": "The cloud location of the BigQuery table.",
              "key": "location"
            },
            {
              "description": "The table reference in the format of project_id:dataset_id.table_id for the BigQuery table.",
              "key": "table_reference"
            }
          ],
          "launchStage": "ALPHA",
          "type": "bigquery.googleapis.com/Table"
        },
        {
          "description": "A BigQuery Location (sometimes called Region).",
          "displayName": "CheckIamPolicy Request Location",
          "labels": [
            {
              "description": "The id of the GCP resource container associated with this resource.",
              "key": "resource_container"
            },
            {
              "description": "Location of resource.",
              "key": "location"
            }
          ],
          "launchStage": "ALPHA",
          "type": "bigquery.googleapis.com/Location"
        },
        {
          "description": "Differential Privacy Budget.",
          "displayName": "Differential Privacy Budget",
          "labels": [
            {
              "description": "The GCP container associated with the metric.",
              "key": "resource_container"
            },
            {
              "description": "Location for the quota.",
              "key": "location"
            },
            {
              "description": "A unique identifier for the budget basis of the privacy budget (e.g view_uuid for per-view budgets).",
              "key": "budget_id"
            },
            {
              "description": "The multi-region identifier for the associated resource (e.g \"us\", \"eu\"). Used only for multi-region quota metrics.",
              "key": "multi_region"
            }
          ],
          "launchStage": "ALPHA",
          "type": "bigquery.googleapis.com/InternalDifferentialPrivacyBudget"
        },
        {
          "description": "Differential Privacy Budget exposed externally to provide privacy budget metrics.",
          "displayName": "Differential Privacy Budget External",
          "labels": [
            {
              "description": "The GCP container associated with the metric.",
              "key": "resource_container"
            },
            {
              "description": "Location for the quota.",
              "key": "location"
            },
            {
              "description": "A unique identifier for the budget basis of the privacy budget (e.g view_uuid for per-view budgets).",
              "key": "budget_id"
            }
          ],
          "launchStage": "BETA",
          "type": "bigquery.googleapis.com/ExternalDifferentialPrivacyBudget"
        }
      ],
      "monitoring": {
        "consumerDestinations": [
          {
            "metrics": [
              "bigquery.googleapis.com/quota/internal/table/base_table_bytes_for_free_indexing_per_org/exceeded",
              "bigquery.googleapis.com/quota/internal/table/base_table_bytes_for_free_indexing_per_org_eu/exceeded",
              "bigquery.googleapis.com/quota/internal/table/base_table_bytes_for_free_indexing_per_org_us/exceeded",
              "bigquery.googleapis.com/quota/internal/table/base_table_bytes_for_free_indexing_per_project/exceeded",
              "bigquery.googleapis.com/quota/internal/table/base_table_bytes_for_free_indexing_per_project_eu/exceeded",
              "bigquery.googleapis.com/quota/internal/table/base_table_bytes_for_free_indexing_per_project_us/exceeded"
            ],
            "monitoredResource": "bigquery.googleapis.com/Table"
          },
          {
            "metrics": [
              "bigquery.googleapis.com/quota/internalCheckIamPolicyRequests/exceeded",
              "bigquery.googleapis.com/quota/internalCheckIamPolicyRequests/usage"
            ],
            "monitoredResource": "bigquery.googleapis.com/Location"
          },
          {
            "metrics": [
              "bigquery.googleapis.com/internal/privacybudget/dp_delta_budget",
              "bigquery.googleapis.com/internal/privacybudget/dp_delta_budget_multi_regional",
              "bigquery.googleapis.com/internal/privacybudget/dp_epsilon_budget",
              "bigquery.googleapis.com/internal/privacybudget/dp_epsilon_budget_multi_regional",
              "bigquery.googleapis.com/quota/internal/privacybudget/dp_delta_budget_multi_regional/exceeded",
              "bigquery.googleapis.com/quota/internal/privacybudget/dp_epsilon_budget_multi_regional/exceeded"
            ],
            "monitoredResource": "bigquery.googleapis.com/InternalDifferentialPrivacyBudget"
          },
          {
            "metrics": [
              "bigquery.googleapis.com/quota/internalCheckIamPolicyRequests/limit"
            ],
            "monitoredResource": "bigquery.googleapis.com/Location"
          },
          {
            "metrics": [
              "bigquery.googleapis.com/quota/internal/table/base_table_bytes_for_free_indexing_per_org/limit",
              "bigquery.googleapis.com/quota/internal/table/base_table_bytes_for_free_indexing_per_org/usage",
              "bigquery.googleapis.com/quota/internal/table/base_table_bytes_for_free_indexing_per_org_eu/limit",
              "bigquery.googleapis.com/quota/internal/table/base_table_bytes_for_free_indexing_per_org_eu/usage",
              "bigquery.googleapis.com/quota/internal/table/base_table_bytes_for_free_indexing_per_org_us/limit",
              "bigquery.googleapis.com/quota/internal/table/base_table_bytes_for_free_indexing_per_org_us/usage",
              "bigquery.googleapis.com/quota/internal/table/base_table_bytes_for_free_indexing_per_project/limit",
              "bigquery.googleapis.com/quota/internal/table/base_table_bytes_for_free_indexing_per_project/usage",
              "bigquery.googleapis.com/quota/internal/table/base_table_bytes_for_free_indexing_per_project_eu/limit",
              "bigquery.googleapis.com/quota/internal/table/base_table_bytes_for_free_indexing_per_project_eu/usage",
              "bigquery.googleapis.com/quota/internal/table/base_table_bytes_for_free_indexing_per_project_us/limit",
              "bigquery.googleapis.com/quota/internal/table/base_table_bytes_for_free_indexing_per_project_us/usage"
            ],
            "monitoredResource": "bigquery.googleapis.com/Table"
          },
          {
            "metrics": [
              "bigquery.googleapis.com/quota/internal/privacybudget/dp_delta_budget_multi_regional/limit",
              "bigquery.googleapis.com/quota/internal/privacybudget/dp_delta_budget_multi_regional/usage",
              "bigquery.googleapis.com/quota/internal/privacybudget/dp_epsilon_budget_multi_regional/limit",
              "bigquery.googleapis.com/quota/internal/privacybudget/dp_epsilon_budget_multi_regional/usage"
            ],
            "monitoredResource": "bigquery.googleapis.com/InternalDifferentialPrivacyBudget"
          },
          {
            "metrics": [
              "bigquery.googleapis.com/privacybudget/dp_delta_budget",
              "bigquery.googleapis.com/privacybudget/dp_epsilon_budget",
              "bigquery.googleapis.com/quota/privacybudget/dp_delta_budget/exceeded",
              "bigquery.googleapis.com/quota/privacybudget/dp_epsilon_budget/exceeded"
            ],
            "monitoredResource": "bigquery.googleapis.com/ExternalDifferentialPrivacyBudget"
          },
          {
            "metrics": [
              "bigquery.googleapis.com/quota/privacybudget/dp_delta_budget/limit",
              "bigquery.googleapis.com/quota/privacybudget/dp_delta_budget/usage",
              "bigquery.googleapis.com/quota/privacybudget/dp_epsilon_budget/limit",
              "bigquery.googleapis.com/quota/privacybudget/dp_epsilon_budget/usage"
            ],
            "monitoredResource": "bigquery.googleapis.com/ExternalDifferentialPrivacyBudget"
          }
        ]
      },
      "name": "bigquery.googleapis.com",
      "quota": {},
      "title": "BigQuery API",
      "usage": {
        "requirements": [
          "serviceusage.googleapis.com/tos/cloud"
        ]
      }
    },
    "name": "projects/215695389495/services/bigquery.googleapis.com",
    "parent": "projects/215695389495",
    "state": "ENABLED"
  },
  {
    "config": {
      "authentication": {},
      "documentation": {
        "summary": "Allows users to manage BigQuery connections to external data sources."
      },
      "monitoring": {},
      "name": "bigqueryconnection.googleapis.com",
      "quota": {},
      "title": "BigQuery Connection API",
      "usage": {
        "requirements": [
          "serviceusage.googleapis.com/tos/cloud"
        ]
      }
    },
    "name": "projects/215695389495/services/bigqueryconnection.googleapis.com",
    "parent": "projects/215695389495",
    "state": "ENABLED"
  },
  {
    "config": {
      "authentication": {},
      "documentation": {
        "summary": "Allows users to manage BigQuery data policies."
      },
      "monitoring": {},
      "name": "bigquerydatapolicy.googleapis.com",
      "quota": {},
      "title": "BigQuery Data Policy API",
      "usage": {
        "requirements": [
          "serviceusage.googleapis.com/tos/cloud"
        ]
      }
    },
    "name": "projects/215695389495/services/bigquerydatapolicy.googleapis.com",
    "parent": "projects/215695389495",
    "state": "ENABLED"
  },
  {
    "config": {
      "authentication": {},
      "documentation": {
        "summary": "The migration service, exposing apis for migration jobs operations, and agent management."
      },
      "monitoring": {},
      "name": "bigquerymigration.googleapis.com",
      "quota": {},
      "title": "BigQuery Migration API",
      "usage": {
        "requirements": [
          "serviceusage.googleapis.com/tos/cloud"
        ]
      }
    },
    "name": "projects/215695389495/services/bigquerymigration.googleapis.com",
    "parent": "projects/215695389495",
    "state": "ENABLED"
  },
  {
    "config": {
      "authentication": {},
      "documentation": {
        "summary": "A service to modify your BigQuery flat-rate reservations."
      },
      "monitoring": {},
      "name": "bigqueryreservation.googleapis.com",
      "quota": {},
      "title": "BigQuery Reservation API",
      "usage": {
        "requirements": [
          "serviceusage.googleapis.com/tos/cloud"
        ]
      }
    },
    "name": "projects/215695389495/services/bigqueryreservation.googleapis.com",
    "parent": "projects/215695389495",
    "state": "ENABLED"
  },
  {
    "config": {
      "authentication": {},
      "documentation": {},
      "monitoredResources": [
        {
          "description": "BigQuery Storage Write API metrics for Dataflow jobs.",
          "displayName": "BigQuery Storage Write API metrics for Dataflow jobs.",
          "labels": [
            {
              "description": "The identifier of the GCP project/folder/org associated with this resource. This is the project that runs the Dataflow job.",
              "key": "resource_container"
            },
            {
              "description": "The BigQuery region in which the Storage API server locates.",
              "key": "location"
            },
            {
              "description": "The name of the Dataflow job this worker belongs to.",
              "key": "job_name"
            },
            {
              "description": "The id of the dataflow job the worker belongs to.",
              "key": "job_id"
            },
            {
              "description": "The ID of the worker, unique for this job_id.",
              "key": "worker_id"
            },
            {
              "description": "The project of BigQuery destination table of the Dataflow job.",
              "key": "destination_project"
            }
          ],
          "launchStage": "ALPHA",
          "type": "bigquerystorage.googleapis.com/DataflowWrite"
        }
      ],
      "monitoring": {
        "consumerDestinations": [
          {
            "metrics": [
              "bigquerystorage.googleapis.com/dataflow_write/request_count",
              "bigquerystorage.googleapis.com/dataflow_write/uploaded_row_count",
              "bigquerystorage.googleapis.com/dataflow_write/uploaded_bytes_count",
              "bigquerystorage.googleapis.com/dataflow_write/billed_bytes_count",
              "bigquerystorage.googleapis.com/dataflow_write/connection_results_count",
              "bigquerystorage.googleapis.com/dataflow_write/server_side_latencies",
              "bigquerystorage.googleapis.com/dataflow_write/transcoding_latencies",
              "bigquerystorage.googleapis.com/dataflow_write/concurrent_connections"
            ],
            "monitoredResource": "bigquerystorage.googleapis.com/DataflowWrite"
          }
        ]
      },
      "name": "bigquerystorage.googleapis.com",
      "quota": {},
      "title": "BigQuery Storage API",
      "usage": {
        "requirements": [
          "serviceusage.googleapis.com/tos/cloud"
        ]
      }
    },
    "name": "projects/215695389495/services/bigquerystorage.googleapis.com",
    "parent": "projects/215695389495",
    "state": "ENABLED"
  },
  {
    "config": {
      "authentication": {},
      "documentation": {},
      "monitoredResources": [
        {
          "description": "Certificate Manager project.",
          "displayName": "Certificate Manager project",
          "labels": [
            {
              "description": "The GCP container associated with the resource.",
              "key": "resource_container"
            },
            {
              "description": "GCP location.",
              "key": "location"
            }
          ],
          "launchStage": "GA",
          "type": "certificatemanager.googleapis.com/Project"
        },
        {
          "description": "Certificate Map instance.",
          "displayName": "Certificate Map",
          "labels": [
            {
              "description": "The GCP container associated with the resource.",
              "key": "resource_container"
            },
            {
              "description": "GCP location.",
              "key": "location"
            },
            {
              "description": "ID of Certificate Map.",
              "key": "certificate_map_id"
            }
          ],
          "launchStage": "GA",
          "type": "certificatemanager.googleapis.com/CertificateMap"
        }
      ],
      "monitoring": {
        "consumerDestinations": [
          {
            "metrics": [
              "certificatemanager.googleapis.com/project/certificates"
            ],
            "monitoredResource": "certificatemanager.googleapis.com/Project"
          },
          {
            "metrics": [
              "certificatemanager.googleapis.com/map/entries"
            ],
            "monitoredResource": "certificatemanager.googleapis.com/CertificateMap"
          }
        ]
      },
      "name": "certificatemanager.googleapis.com",
      "quota": {},
      "title": "Certificate Manager API",
      "usage": {
        "requirements": [
          "serviceusage.googleapis.com/billing-enabled",
          "serviceusage.googleapis.com/tos/cloud"
        ]
      }
    },
    "name": "projects/215695389495/services/certificatemanager.googleapis.com",
    "parent": "projects/215695389495",
    "state": "ENABLED"
  },
  {
    "config": {
      "authentication": {},
      "documentation": {
        "summary": "This is a meta service for Google Cloud APIs for convenience. Enabling this service enables all commonly used Google Cloud APIs for the project. By default, it is enabled for all projects created through Google Cloud Console and Google Cloud SDK, and should be manually enabled for all other projects that intend to use Google Cloud APIs. Note: disabling this service has no effect on other services.\n"
      },
      "monitoring": {},
      "name": "cloudapis.googleapis.com",
      "quota": {},
      "title": "Google Cloud APIs",
      "usage": {
        "requirements": [
          "serviceusage.googleapis.com/tos/cloud"
        ]
      }
    },
    "name": "projects/215695389495/services/cloudapis.googleapis.com",
    "parent": "projects/215695389495",
    "state": "ENABLED"
  },
  {
    "config": {
      "authentication": {},
      "documentation": {
        "summary": "The Cloud Asset API manages the history and inventory of Google Cloud resources."
      },
      "monitoring": {},
      "name": "cloudasset.googleapis.com",
      "quota": {},
      "title": "Cloud Asset API",
      "usage": {
        "requirements": [
          "serviceusage.googleapis.com/tos/cloud"
        ]
      }
    },
    "name": "projects/215695389495/services/cloudasset.googleapis.com",
    "parent": "projects/215695389495",
    "state": "ENABLED"
  },
  {
    "config": {
      "authentication": {},
      "documentation": {
        "summary": "Creates and manages builds on Google Cloud Platform."
      },
      "monitoredResources": [
        {
          "description": "A location in the Cloud Build API.",
          "displayName": "Cloud Build Location",
          "labels": [
            {
              "description": "The identified of the GCP resource container associated with this resource, such as \"my_project\" or \"organizations/5678\".",
              "key": "resource_container"
            },
            {
              "description": "Location of resource.",
              "key": "location"
            }
          ],
          "launchStage": "ALPHA",
          "type": "cloudbuild.googleapis.com/Location"
        },
        {
          "description": "GKE instance.",
          "displayName": "GKE instance",
          "labels": [
            {
              "description": "The identifier of the GCP resource container associated with this resource, such as \"my_project\" or \"organizations/5678\".",
              "key": "resource_container"
            },
            {
              "description": "Location of resource.",
              "key": "location"
            },
            {
              "description": "The identifier of the GKE instance.",
              "key": "gke_instance_id"
            }
          ],
          "launchStage": "ALPHA",
          "type": "cloudbuild.googleapis.com/GkeInstance"
        },
        {
          "description": "Private Worker Pool.",
          "displayName": "Private Worker Pool",
          "labels": [
            {
              "description": "The identifier of the GCP resource container associated with this resource, such as \"my_project\" or \"organizations/5678\".",
              "key": "resource_container"
            },
            {
              "description": "Location of resource.",
              "key": "location"
            },
            {
              "description": "The UUID of the worker pool.",
              "key": "worker_pool_uuid"
            }
          ],
          "launchStage": "ALPHA",
          "type": "cloudbuild.googleapis.com/PrivatePool"
        }
      ],
      "monitoring": {
        "consumerDestinations": [
          {
            "metrics": [
              "cloudbuild.googleapis.com/internal/gke_instance/pod",
              "cloudbuild.googleapis.com/internal/gke_instance/node"
            ],
            "monitoredResource": "cloudbuild.googleapis.com/GkeInstance"
          },
          {
            "metrics": [
              "cloudbuild.googleapis.com/internal/private_pool_ready_worker_replicas"
            ],
            "monitoredResource": "cloudbuild.googleapis.com/PrivatePool"
          },
          {
            "metrics": [
              "cloudbuild.googleapis.com/concurrent_public_pool_build_cpus",
              "cloudbuild.googleapis.com/quota/concurrent_public_pool_build_cpus/exceeded"
            ],
            "monitoredResource": "cloudbuild.googleapis.com/Location"
          },
          {
            "metrics": [
              "cloudbuild.googleapis.com/quota/concurrent_public_pool_build_cpus/limit",
              "cloudbuild.googleapis.com/quota/concurrent_public_pool_build_cpus/usage"
            ],
            "monitoredResource": "cloudbuild.googleapis.com/Location"
          }
        ]
      },
      "name": "cloudbuild.googleapis.com",
      "quota": {},
      "title": "Cloud Build API",
      "usage": {
        "requirements": [
          "serviceusage.googleapis.com/tos/cloud",
          "serviceusage.googleapis.com/billing-enabled"
        ]
      }
    },
    "name": "projects/215695389495/services/cloudbuild.googleapis.com",
    "parent": "projects/215695389495",
    "state": "ENABLED"
  },
  {
    "config": {
      "authentication": {},
      "documentation": {
        "summary": "Creates and manages jobs run on a regular recurring schedule."
      },
      "monitoring": {},
      "name": "cloudscheduler.googleapis.com",
      "quota": {},
      "title": "Cloud Scheduler API",
      "usage": {
        "requirements": [
          "serviceusage.googleapis.com/tos/cloud",
          "serviceusage.googleapis.com/tos/cloud",
          "serviceusage.googleapis.com/billing-enabled"
        ]
      }
    },
    "name": "projects/215695389495/services/cloudscheduler.googleapis.com",
    "parent": "projects/215695389495",
    "state": "ENABLED"
  },
  {
    "config": {
      "authentication": {},
      "documentation": {
        "summary": "Sends application trace data to Cloud Trace for viewing. Trace data is collected for all App Engine applications by default. Trace data from other applications can be provided using this API. This library is used to interact with the Cloud Trace API directly. If you are looking to instrument your application for Cloud Trace, we recommend using OpenTelemetry.\n"
      },
      "monitoredResources": [
        {
          "labels": [
            {
              "key": "cloud.googleapis.com/project"
            },
            {
              "key": "monitoring.googleapis.com/service"
            },
            {
              "key": "cloud.googleapis.com/location"
            },
            {
              "key": "cloud.googleapis.com/uid"
            }
          ],
          "type": "cloudtrace.googleapis.com/charged_project"
        },
        {
          "description": "A cloud trace specialization target schema of cloud.ChargedProject.",
          "displayName": "Cloud trace target",
          "labels": [
            {
              "description": "The monitored resource container. Could be project, workspace, etc.",
              "key": "resource_container"
            },
            {
              "description": "The service-specific notion of location.",
              "key": "location"
            },
            {
              "description": "The name of the API service with which the data is associated (e.g.,'cloudtrace.googleapis.com').",
              "key": "api_service"
            }
          ],
          "launchStage": "ALPHA",
          "type": "cloudtrace.googleapis.com/ChargedProject"
        },
        {
          "description": "Cloud trace resource, e.g. project.",
          "displayName": "Cloud Trace",
          "labels": [
            {
              "description": "The identifier of the GCP container associated with the resource.",
              "key": "resource_container"
            },
            {
              "description": "The location that the Cloud Trace service recording the metrics is running.",
              "key": "location"
            }
          ],
          "launchStage": "EARLY_ACCESS",
          "type": "cloudtrace.googleapis.com/CloudtraceProject"
        }
      ],
      "monitoring": {
        "consumerDestinations": [
          {
            "metrics": [
              "cloudtrace.googleapis.com/billing/ingested_spans",
              "cloudtrace.googleapis.com/billing/ingested_bytes"
            ],
            "monitoredResource": "cloudtrace.googleapis.com/ChargedProject"
          },
          {
            "metrics": [
              "cloudtrace.googleapis.com/billing/retrieved_spans"
            ],
            "monitoredResource": "cloudtrace.googleapis.com/charged_project"
          },
          {
            "metrics": [
              "cloudtrace.googleapis.com/internal/plugin_server_span_count",
              "cloudtrace.googleapis.com/internal/reader_root_query_count",
              "cloudtrace.googleapis.com/internal/reader_root_query_latencies",
              "cloudtrace.googleapis.com/bigquery_export/exported_span_count"
            ],
            "monitoredResource": "cloudtrace.googleapis.com/CloudtraceProject"
          }
        ]
      },
      "name": "cloudtrace.googleapis.com",
      "quota": {},
      "title": "Cloud Trace API",
      "usage": {
        "requirements": [
          "serviceusage.googleapis.com/tos/cloud"
        ]
      }
    },
    "name": "projects/215695389495/services/cloudtrace.googleapis.com",
    "parent": "projects/215695389495",
    "state": "ENABLED"
  },
  {
    "config": {
      "authentication": {},
      "documentation": {
        "summary": "Creates and runs virtual machines on Google Cloud Platform.\n"
      },
      "monitoredResources": [
        {
          "description": "VPC Network.",
          "displayName": "VPC Network",
          "labels": [
            {
              "description": "The identifier of the GCP container (i.e. project) associated with the VPC Network.",
              "key": "resource_container"
            },
            {
              "description": "Location of the VPC Network, global always.",
              "key": "location"
            },
            {
              "description": "VPC Network resource ID.",
              "key": "network_id"
            }
          ],
          "launchStage": "GA",
          "type": "compute.googleapis.com/VpcNetwork"
        },
        {
          "description": "A location in the Compute API.",
          "displayName": "Compute Location",
          "labels": [
            {
              "description": "The identifier of the GCP container (i.e. project) associated with the Compute Location.",
              "key": "resource_container"
            },
            {
              "description": "Location of resource.",
              "key": "location"
            }
          ],
          "launchStage": "GA",
          "type": "compute.googleapis.com/Location"
        },
        {
          "description": "Interconnect.",
          "displayName": "Interconnect",
          "labels": [
            {
              "description": "The identifier of the GCP container (i.e. project) associated with the Interconnect.",
              "key": "resource_container"
            },
            {
              "description": "Location of the Interconnect.",
              "key": "location"
            },
            {
              "description": "Interconnect resource ID.",
              "key": "interconnect_id"
            }
          ],
          "launchStage": "GA",
          "type": "compute.googleapis.com/Interconnect"
        },
        {
          "description": "Firewall policy.",
          "displayName": "Firewall policy",
          "labels": [
            {
              "description": "The identifier of the GCP container (i.e. project or organization) associated with the firewall policy.",
              "key": "resource_container"
            },
            {
              "description": "Location of the firewall policy.",
              "key": "location"
            },
            {
              "description": "Firewall policy resource ID.",
              "key": "firewall_policy_id"
            }
          ],
          "launchStage": "GA",
          "type": "compute.googleapis.com/FirewallPolicy"
        },
        {
          "description": "Security policy.",
          "displayName": "Security policy",
          "labels": [
            {
              "description": "The identifier of the GCP container (i.e. project) associated with the security policy.",
              "key": "resource_container"
            },
            {
              "description": "Location of the security policy.",
              "key": "location"
            },
            {
              "description": "Security policy resource ID.",
              "key": "security_policy_id"
            }
          ],
          "launchStage": "ALPHA",
          "type": "compute.googleapis.com/SecurityPolicy"
        },
        {
          "description": "Operation Type.",
          "displayName": "Operation Type",
          "labels": [
            {
              "description": "The identifier of the GCP container (i.e. project) associated with the operation.",
              "key": "resource_container"
            },
            {
              "description": "Location of the operation.",
              "key": "location"
            },
            {
              "description": "Operation type.",
              "key": "operation_type"
            }
          ],
          "launchStage": "ALPHA",
          "type": "compute.googleapis.com/OperationType"
        },
        {
          "description": "Monitored resource representing a reservation.",
          "displayName": "Reservation",
          "labels": [
            {
              "description": "The GCP container (e.g. project number) associated with the reservation.",
              "key": "resource_container"
            },
            {
              "description": "The zone that contains the reservation.",
              "key": "location"
            },
            {
              "description": "Reservation resource ID.",
              "key": "reservation_id"
            }
          ],
          "launchStage": "GA",
          "type": "compute.googleapis.com/Reservation"
        },
        {
          "description": "Monitored resource representing a storage pool.",
          "displayName": "Storage Pool",
          "labels": [
            {
              "description": "The GCP container (e.g. project number) associated with the reservation.",
              "key": "resource_container"
            },
            {
              "description": "The location that contains the storage pool.",
              "key": "location"
            },
            {
              "description": "Numerical resource ID of the storage pool.",
              "key": "storage_pool_id"
            }
          ],
          "launchStage": "BETA",
          "type": "compute.googleapis.com/StoragePool"
        },
        {
          "description": "A virtual machine instance hosted in Compute Engine.",
          "displayName": "VM Instance",
          "labels": [
            {
              "description": "The identifier of the GCP project associated with this resource, such as \"my-project\".",
              "key": "project_id"
            },
            {
              "description": "The numeric VM instance identifier assigned by Compute Engine.",
              "key": "instance_id"
            },
            {
              "description": "The Compute Engine zone in which the VM is running.",
              "key": "zone"
            }
          ],
          "launchStage": "GA",
          "type": "gce_instance"
        }
      ],
      "monitoring": {
        "consumerDestinations": [
          {
            "metrics": [
              "compute.googleapis.com/cloud_router_prefixes_from_other_regions_per_region_per_vpc_network",
              "compute.googleapis.com/cloud_router_prefixes_from_own_region_per_region_per_vpc_network",
              "compute.googleapis.com/dynamic_routes_per_region_per_peering_group",
              "compute.googleapis.com/global_internal_managed_forwarding_rules_per_region_per_vpc_network",
              "compute.googleapis.com/instances_per_peering_group",
              "compute.googleapis.com/instances_per_vpc_network",
              "compute.googleapis.com/internal_lb_forwarding_rules_per_peering_group",
              "compute.googleapis.com/internal_lb_forwarding_rules_per_vpc_network",
              "compute.googleapis.com/internal_managed_forwarding_rules_per_peering_group",
              "compute.googleapis.com/internal_managed_forwarding_rules_per_vpc_network",
              "compute.googleapis.com/internal_protocol_forwarding_rules_per_peering_group",
              "compute.googleapis.com/internal_protocol_forwarding_rules_per_vpc_network",
              "compute.googleapis.com/ip_aliases_per_peering_group",
              "compute.googleapis.com/ip_aliases_per_vpc_network",
              "compute.googleapis.com/peerings_per_vpc_network",
              "compute.googleapis.com/psc_google_apis_forwarding_rules_per_vpc_network",
              "compute.googleapis.com/psc_ilb_consumer_forwarding_rules_per_producer_vpc_network",
              "compute.googleapis.com/psc_propagated_connections_per_vpc_network",
              "compute.googleapis.com/quota/cloud_router_prefixes_from_other_regions_per_region_per_vpc_network/exceeded",
              "compute.googleapis.com/quota/cloud_router_prefixes_from_own_region_per_region_per_vpc_network/exceeded",
              "compute.googleapis.com/quota/dynamic_routes_per_region_per_peering_group/exceeded",
              "compute.googleapis.com/quota/global_internal_managed_forwarding_rules_per_region_per_vpc_network/exceeded",
              "compute.googleapis.com/quota/global_network_firewall_policy_associations_per_vpc_network/exceeded",
              "compute.googleapis.com/quota/global_network_firewall_policy_associations_per_vpc_network_system/exceeded",
              "compute.googleapis.com/quota/instances_per_peering_group/exceeded",
              "compute.googleapis.com/quota/instances_per_regional_vpc_network/exceeded",
              "compute.googleapis.com/quota/instances_per_vpc_network/exceeded",
              "compute.googleapis.com/quota/internal_lb_forwarding_rules_per_peering_group/exceeded",
              "compute.googleapis.com/quota/internal_lb_forwarding_rules_per_regional_vpc_network/exceeded",
              "compute.googleapis.com/quota/internal_lb_forwarding_rules_per_vpc_network/exceeded",
              "compute.googleapis.com/quota/internal_managed_forwarding_rules_per_peering_group/exceeded",
              "compute.googleapis.com/quota/internal_managed_forwarding_rules_per_regional_vpc_network/exceeded",
              "compute.googleapis.com/quota/internal_managed_forwarding_rules_per_vpc_network/exceeded",
              "compute.googleapis.com/quota/internal_protocol_forwarding_rules_per_peering_group/exceeded",
              "compute.googleapis.com/quota/internal_protocol_forwarding_rules_per_regional_vpc_network/exceeded",
              "compute.googleapis.com/quota/internal_protocol_forwarding_rules_per_vpc_network/exceeded",
              "compute.googleapis.com/quota/ip_aliases_per_peering_group/exceeded",
              "compute.googleapis.com/quota/ip_aliases_per_regional_vpc_network/exceeded",
              "compute.googleapis.com/quota/ip_aliases_per_vpc_network/exceeded",
              "compute.googleapis.com/quota/peerings_per_vpc_network/exceeded",
              "compute.googleapis.com/quota/psc_accepted_connections_per_producer_vpc_network/exceeded",
              "compute.googleapis.com/quota/psc_connections_per_vpc_network/exceeded",
              "compute.googleapis.com/quota/psc_google_apis_forwarding_rules_per_vpc_network/exceeded",
              "compute.googleapis.com/quota/psc_ilb_consumer_forwarding_rules_per_producer_regional_vpc_network/exceeded",
              "compute.googleapis.com/quota/psc_ilb_consumer_forwarding_rules_per_producer_vpc_network/exceeded",
              "compute.googleapis.com/quota/psc_incoming_connections_per_producer_vpc_network/exceeded",
              "compute.googleapis.com/quota/psc_outgoing_connections_per_consumer_vpc_network/exceeded",
              "compute.googleapis.com/quota/psc_propagated_connections_per_vpc_network/exceeded",
              "compute.googleapis.com/quota/regional_external_managed_forwarding_rules_per_region_per_vpc_network/exceeded",
              "compute.googleapis.com/quota/regional_fast_ip_move_backend_services_per_region_per_vpc_network/exceeded",
              "compute.googleapis.com/quota/regional_fast_ip_move_domains_per_region_per_vpc_network/exceeded",
              "compute.googleapis.com/quota/regional_internal_managed_forwarding_rules_per_region_per_vpc_network/exceeded",
              "compute.googleapis.com/quota/regional_network_firewall_policy_associations_per_region_per_vpc_network/exceeded",
              "compute.googleapis.com/quota/regional_network_firewall_policy_associations_per_region_per_vpc_network_system/exceeded",
              "compute.googleapis.com/quota/static_routes_per_peering_group/exceeded",
              "compute.googleapis.com/quota/static_routes_per_vpc_network/exceeded",
              "compute.googleapis.com/quota/subnet_ranges_per_peering_group/exceeded",
              "compute.googleapis.com/quota/subnet_ranges_per_regional_vpc_network/exceeded",
              "compute.googleapis.com/quota/subnet_ranges_per_vpc_network/exceeded",
              "compute.googleapis.com/regional_external_managed_forwarding_rules_per_region_per_vpc_network",
              "compute.googleapis.com/regional_internal_managed_forwarding_rules_per_region_per_vpc_network",
              "compute.googleapis.com/static_routes_per_peering_group",
              "compute.googleapis.com/static_routes_per_vpc_network",
              "compute.googleapis.com/subnet_ranges_per_peering_group",
              "compute.googleapis.com/subnet_ranges_per_vpc_network"
            ],
            "monitoredResource": "compute.googleapis.com/VpcNetwork"
          },
          {
            "metrics": [
              "compute.googleapis.com/cpus_per_vm_family",
              "compute.googleapis.com/global_dns/request_count",
              "compute.googleapis.com/gpus_per_gpu_family",
              "compute.googleapis.com/inter_region_egress_bandwidth",
              "compute.googleapis.com/local_ssd_total_storage_per_vm_family",
              "compute.googleapis.com/quota/asynchronously_replicating_disk_pairs_per_project_region_pair/exceeded",
              "compute.googleapis.com/quota/cpus_per_vm_family/exceeded",
              "compute.googleapis.com/quota/gpus_per_gpu_family/exceeded",
              "compute.googleapis.com/quota/inter_region_egress_bandwidth/exceeded",
              "compute.googleapis.com/quota/inter_region_egress_bandwidth/usage",
              "compute.googleapis.com/quota/local_ssd_total_storage_per_vm_family/exceeded",
              "compute.googleapis.com/quota/preemptible_gpus_per_gpu_family/exceeded",
              "compute.googleapis.com/quota/rdma_networking_cards_per_vm_family/exceeded",
              "compute.googleapis.com/quota/reserved_resource_per_aggregate_reservation_per_cluster/exceeded",
              "compute.googleapis.com/quota/tpus_per_tpu_family/exceeded"
            ],
            "monitoredResource": "compute.googleapis.com/Location"
          },
          {
            "metrics": [
              "compute.googleapis.com/interconnect_attachments_per_interconnect",
              "compute.googleapis.com/quota/interconnect_attachments_per_interconnect/exceeded"
            ],
            "monitoredResource": "compute.googleapis.com/Interconnect"
          },
          {
            "metrics": [
              "compute.googleapis.com/fqdns_per_global_network_firewall_policy",
              "compute.googleapis.com/fqdns_per_hierarchical_firewall_policy",
              "compute.googleapis.com/fqdns_per_regional_network_firewall_policy",
              "compute.googleapis.com/quota/fqdns_per_global_network_firewall_policy/exceeded",
              "compute.googleapis.com/quota/fqdns_per_hierarchical_firewall_policy/exceeded",
              "compute.googleapis.com/quota/fqdns_per_regional_network_firewall_policy/exceeded",
              "compute.googleapis.com/quota/rule_attributes_per_global_network_firewall_policy/exceeded",
              "compute.googleapis.com/quota/rule_attributes_per_hierarchical_firewall_policy/exceeded",
              "compute.googleapis.com/quota/rule_attributes_per_regional_network_firewall_policy/exceeded",
              "compute.googleapis.com/rule_attributes_per_global_network_firewall_policy",
              "compute.googleapis.com/rule_attributes_per_hierarchical_firewall_policy",
              "compute.googleapis.com/rule_attributes_per_regional_network_firewall_policy"
            ],
            "monitoredResource": "compute.googleapis.com/FirewallPolicy"
          },
          {
            "metrics": [
              "compute.googleapis.com/quota/advanced_rules_per_edge_security_policy/exceeded",
              "compute.googleapis.com/quota/advanced_rules_per_regional_security_policy/exceeded",
              "compute.googleapis.com/quota/advanced_rules_per_security_policy/exceeded"
            ],
            "monitoredResource": "compute.googleapis.com/SecurityPolicy"
          },
          {
            "metrics": [
              "compute.googleapis.com/global_concurrent_operations",
              "compute.googleapis.com/quota/concurrent/global_concurrent_operations/exceeded",
              "compute.googleapis.com/quota/concurrent/internal/global_concurrent_operations/combined_units",
              "compute.googleapis.com/quota/concurrent/internal/regional_concurrent_operations/combined_units",
              "compute.googleapis.com/quota/concurrent/regional_concurrent_operations/exceeded",
              "compute.googleapis.com/regional_concurrent_operations"
            ],
            "monitoredResource": "compute.googleapis.com/OperationType"
          },
          {
            "metrics": [
              "compute.googleapis.com/instance/global_dns/request_count"
            ],
            "monitoredResource": "gce_instance"
          },
          {
            "metrics": [
              "compute.googleapis.com/reservation/reserved",
              "compute.googleapis.com/reservation/assured",
              "compute.googleapis.com/reservation/used",
              "compute.googleapis.com/reservation/internal/matching_instances",
              "compute.googleapis.com/reservation/internal/prespuns_by_state"
            ],
            "monitoredResource": "compute.googleapis.com/Reservation"
          },
          {
            "metrics": [
              "compute.googleapis.com/storage_pool/disks",
              "compute.googleapis.com/storage_pool/provisioned_capacity",
              "compute.googleapis.com/storage_pool/used_capacity",
              "compute.googleapis.com/storage_pool/total_disk_provisioned_capacity",
              "compute.googleapis.com/storage_pool/provisioned_iops",
              "compute.googleapis.com/storage_pool/used_iops",
              "compute.googleapis.com/storage_pool/total_disk_provisioned_iops",
              "compute.googleapis.com/storage_pool/provisioned_throughput",
              "compute.googleapis.com/storage_pool/used_throughput",
              "compute.googleapis.com/storage_pool/total_disk_provisioned_throughput",
              "compute.googleapis.com/storage_pool/capacity_utilization",
              "compute.googleapis.com/storage_pool/iops_utilization",
              "compute.googleapis.com/storage_pool/throughput_utilization"
            ],
            "monitoredResource": "compute.googleapis.com/StoragePool"
          },
          {
            "metrics": [
              "compute.googleapis.com/quota/asynchronously_replicating_disk_pairs_per_project_region_pair/limit",
              "compute.googleapis.com/quota/asynchronously_replicating_disk_pairs_per_project_region_pair/usage",
              "compute.googleapis.com/quota/cpus_per_vm_family/limit",
              "compute.googleapis.com/quota/cpus_per_vm_family/usage",
              "compute.googleapis.com/quota/gpus_per_gpu_family/limit",
              "compute.googleapis.com/quota/gpus_per_gpu_family/usage",
              "compute.googleapis.com/quota/inter_region_egress_bandwidth/limit",
              "compute.googleapis.com/quota/local_ssd_total_storage_per_vm_family/limit",
              "compute.googleapis.com/quota/local_ssd_total_storage_per_vm_family/usage",
              "compute.googleapis.com/quota/preemptible_gpus_per_gpu_family/limit",
              "compute.googleapis.com/quota/preemptible_gpus_per_gpu_family/usage",
              "compute.googleapis.com/quota/rdma_networking_cards_per_vm_family/limit",
              "compute.googleapis.com/quota/rdma_networking_cards_per_vm_family/usage",
              "compute.googleapis.com/quota/reserved_resource_per_aggregate_reservation_per_cluster/limit",
              "compute.googleapis.com/quota/reserved_resource_per_aggregate_reservation_per_cluster/usage",
              "compute.googleapis.com/quota/tpus_per_tpu_family/limit",
              "compute.googleapis.com/quota/tpus_per_tpu_family/usage"
            ],
            "monitoredResource": "compute.googleapis.com/Location"
          },
          {
            "metrics": [
              "compute.googleapis.com/quota/cloud_router_prefixes_from_other_regions_per_region_per_vpc_network/limit",
              "compute.googleapis.com/quota/cloud_router_prefixes_from_other_regions_per_region_per_vpc_network/usage",
              "compute.googleapis.com/quota/cloud_router_prefixes_from_own_region_per_region_per_vpc_network/limit",
              "compute.googleapis.com/quota/cloud_router_prefixes_from_own_region_per_region_per_vpc_network/usage",
              "compute.googleapis.com/quota/dynamic_routes_per_region_per_peering_group/limit",
              "compute.googleapis.com/quota/dynamic_routes_per_region_per_peering_group/usage",
              "compute.googleapis.com/quota/global_internal_managed_forwarding_rules_per_region_per_vpc_network/limit",
              "compute.googleapis.com/quota/global_internal_managed_forwarding_rules_per_region_per_vpc_network/usage",
              "compute.googleapis.com/quota/global_network_firewall_policy_associations_per_vpc_network/limit",
              "compute.googleapis.com/quota/global_network_firewall_policy_associations_per_vpc_network/usage",
              "compute.googleapis.com/quota/global_network_firewall_policy_associations_per_vpc_network_system/limit",
              "compute.googleapis.com/quota/global_network_firewall_policy_associations_per_vpc_network_system/usage",
              "compute.googleapis.com/quota/instances_per_peering_group/limit",
              "compute.googleapis.com/quota/instances_per_peering_group/usage",
              "compute.googleapis.com/quota/instances_per_regional_vpc_network/limit",
              "compute.googleapis.com/quota/instances_per_regional_vpc_network/usage",
              "compute.googleapis.com/quota/instances_per_vpc_network/limit",
              "compute.googleapis.com/quota/instances_per_vpc_network/usage",
              "compute.googleapis.com/quota/internal_lb_forwarding_rules_per_peering_group/limit",
              "compute.googleapis.com/quota/internal_lb_forwarding_rules_per_peering_group/usage",
              "compute.googleapis.com/quota/internal_lb_forwarding_rules_per_regional_vpc_network/limit",
              "compute.googleapis.com/quota/internal_lb_forwarding_rules_per_regional_vpc_network/usage",
              "compute.googleapis.com/quota/internal_lb_forwarding_rules_per_vpc_network/limit",
              "compute.googleapis.com/quota/internal_lb_forwarding_rules_per_vpc_network/usage",
              "compute.googleapis.com/quota/internal_managed_forwarding_rules_per_peering_group/limit",
              "compute.googleapis.com/quota/internal_managed_forwarding_rules_per_peering_group/usage",
              "compute.googleapis.com/quota/internal_managed_forwarding_rules_per_regional_vpc_network/limit",
              "compute.googleapis.com/quota/internal_managed_forwarding_rules_per_regional_vpc_network/usage",
              "compute.googleapis.com/quota/internal_managed_forwarding_rules_per_vpc_network/limit",
              "compute.googleapis.com/quota/internal_managed_forwarding_rules_per_vpc_network/usage",
              "compute.googleapis.com/quota/internal_protocol_forwarding_rules_per_peering_group/limit",
              "compute.googleapis.com/quota/internal_protocol_forwarding_rules_per_peering_group/usage",
              "compute.googleapis.com/quota/internal_protocol_forwarding_rules_per_regional_vpc_network/limit",
              "compute.googleapis.com/quota/internal_protocol_forwarding_rules_per_regional_vpc_network/usage",
              "compute.googleapis.com/quota/internal_protocol_forwarding_rules_per_vpc_network/limit",
              "compute.googleapis.com/quota/internal_protocol_forwarding_rules_per_vpc_network/usage",
              "compute.googleapis.com/quota/ip_aliases_per_peering_group/limit",
              "compute.googleapis.com/quota/ip_aliases_per_peering_group/usage",
              "compute.googleapis.com/quota/ip_aliases_per_regional_vpc_network/limit",
              "compute.googleapis.com/quota/ip_aliases_per_regional_vpc_network/usage",
              "compute.googleapis.com/quota/ip_aliases_per_vpc_network/limit",
              "compute.googleapis.com/quota/ip_aliases_per_vpc_network/usage",
              "compute.googleapis.com/quota/peerings_per_vpc_network/limit",
              "compute.googleapis.com/quota/peerings_per_vpc_network/usage",
              "compute.googleapis.com/quota/psc_accepted_connections_per_producer_vpc_network/limit",
              "compute.googleapis.com/quota/psc_accepted_connections_per_producer_vpc_network/usage",
              "compute.googleapis.com/quota/psc_connections_per_vpc_network/limit",
              "compute.googleapis.com/quota/psc_connections_per_vpc_network/usage",
              "compute.googleapis.com/quota/psc_google_apis_forwarding_rules_per_vpc_network/limit",
              "compute.googleapis.com/quota/psc_google_apis_forwarding_rules_per_vpc_network/usage",
              "compute.googleapis.com/quota/psc_ilb_consumer_forwarding_rules_per_producer_regional_vpc_network/limit",
              "compute.googleapis.com/quota/psc_ilb_consumer_forwarding_rules_per_producer_regional_vpc_network/usage",
              "compute.googleapis.com/quota/psc_ilb_consumer_forwarding_rules_per_producer_vpc_network/limit",
              "compute.googleapis.com/quota/psc_ilb_consumer_forwarding_rules_per_producer_vpc_network/usage",
              "compute.googleapis.com/quota/psc_incoming_connections_per_producer_vpc_network/limit",
              "compute.googleapis.com/quota/psc_incoming_connections_per_producer_vpc_network/usage",
              "compute.googleapis.com/quota/psc_outgoing_connections_per_consumer_vpc_network/limit",
              "compute.googleapis.com/quota/psc_outgoing_connections_per_consumer_vpc_network/usage",
              "compute.googleapis.com/quota/psc_propagated_connections_per_vpc_network/limit",
              "compute.googleapis.com/quota/psc_propagated_connections_per_vpc_network/usage",
              "compute.googleapis.com/quota/regional_external_managed_forwarding_rules_per_region_per_vpc_network/limit",
              "compute.googleapis.com/quota/regional_external_managed_forwarding_rules_per_region_per_vpc_network/usage",
              "compute.googleapis.com/quota/regional_fast_ip_move_backend_services_per_region_per_vpc_network/limit",
              "compute.googleapis.com/quota/regional_fast_ip_move_backend_services_per_region_per_vpc_network/usage",
              "compute.googleapis.com/quota/regional_fast_ip_move_domains_per_region_per_vpc_network/limit",
              "compute.googleapis.com/quota/regional_fast_ip_move_domains_per_region_per_vpc_network/usage",
              "compute.googleapis.com/quota/regional_internal_managed_forwarding_rules_per_region_per_vpc_network/limit",
              "compute.googleapis.com/quota/regional_internal_managed_forwarding_rules_per_region_per_vpc_network/usage",
              "compute.googleapis.com/quota/regional_network_firewall_policy_associations_per_region_per_vpc_network/limit",
              "compute.googleapis.com/quota/regional_network_firewall_policy_associations_per_region_per_vpc_network/usage",
              "compute.googleapis.com/quota/regional_network_firewall_policy_associations_per_region_per_vpc_network_system/limit",
              "compute.googleapis.com/quota/regional_network_firewall_policy_associations_per_region_per_vpc_network_system/usage",
              "compute.googleapis.com/quota/static_routes_per_peering_group/limit",
              "compute.googleapis.com/quota/static_routes_per_peering_group/usage",
              "compute.googleapis.com/quota/static_routes_per_vpc_network/limit",
              "compute.googleapis.com/quota/static_routes_per_vpc_network/usage",
              "compute.googleapis.com/quota/subnet_ranges_per_peering_group/limit",
              "compute.googleapis.com/quota/subnet_ranges_per_peering_group/usage",
              "compute.googleapis.com/quota/subnet_ranges_per_regional_vpc_network/limit",
              "compute.googleapis.com/quota/subnet_ranges_per_regional_vpc_network/usage",
              "compute.googleapis.com/quota/subnet_ranges_per_vpc_network/limit",
              "compute.googleapis.com/quota/subnet_ranges_per_vpc_network/usage"
            ],
            "monitoredResource": "compute.googleapis.com/VpcNetwork"
          },
          {
            "metrics": [
              "compute.googleapis.com/quota/interconnect_attachments_per_interconnect/limit",
              "compute.googleapis.com/quota/interconnect_attachments_per_interconnect/usage"
            ],
            "monitoredResource": "compute.googleapis.com/Interconnect"
          },
          {
            "metrics": [
              "compute.googleapis.com/quota/fqdns_per_global_network_firewall_policy/limit",
              "compute.googleapis.com/quota/fqdns_per_global_network_firewall_policy/usage",
              "compute.googleapis.com/quota/fqdns_per_hierarchical_firewall_policy/limit",
              "compute.googleapis.com/quota/fqdns_per_hierarchical_firewall_policy/usage",
              "compute.googleapis.com/quota/fqdns_per_regional_network_firewall_policy/limit",
              "compute.googleapis.com/quota/fqdns_per_regional_network_firewall_policy/usage",
              "compute.googleapis.com/quota/rule_attributes_per_global_network_firewall_policy/limit",
              "compute.googleapis.com/quota/rule_attributes_per_global_network_firewall_policy/usage",
              "compute.googleapis.com/quota/rule_attributes_per_hierarchical_firewall_policy/limit",
              "compute.googleapis.com/quota/rule_attributes_per_hierarchical_firewall_policy/usage",
              "compute.googleapis.com/quota/rule_attributes_per_regional_network_firewall_policy/limit",
              "compute.googleapis.com/quota/rule_attributes_per_regional_network_firewall_policy/usage"
            ],
            "monitoredResource": "compute.googleapis.com/FirewallPolicy"
          },
          {
            "metrics": [
              "compute.googleapis.com/quota/advanced_rules_per_edge_security_policy/limit",
              "compute.googleapis.com/quota/advanced_rules_per_edge_security_policy/usage",
              "compute.googleapis.com/quota/advanced_rules_per_regional_security_policy/limit",
              "compute.googleapis.com/quota/advanced_rules_per_regional_security_policy/usage",
              "compute.googleapis.com/quota/advanced_rules_per_security_policy/limit",
              "compute.googleapis.com/quota/advanced_rules_per_security_policy/usage"
            ],
            "monitoredResource": "compute.googleapis.com/SecurityPolicy"
          },
          {
            "metrics": [
              "compute.googleapis.com/quota/concurrent/global_concurrent_operations/limit",
              "compute.googleapis.com/quota/concurrent/regional_concurrent_operations/limit"
            ],
            "monitoredResource": "compute.googleapis.com/OperationType"
          }
        ]
      },
      "name": "compute.googleapis.com",
      "quota": {},
      "title": "Compute Engine API",
      "usage": {
        "requirements": [
          "serviceusage.googleapis.com/tos/cloud",
          "serviceusage.googleapis.com/billing-enabled"
        ]
      }
    },
    "name": "projects/215695389495/services/compute.googleapis.com",
    "parent": "projects/215695389495",
    "state": "ENABLED"
  },
  {
    "config": {
      "authentication": {},
      "documentation": {
        "summary": "Google Container Registry provides secure, private Docker image storage on Google Cloud Platform.  Our API follows the Docker Registry API specification, so we are fully compatible with the Docker CLI client, as well as standard tooling using the Docker Registry API."
      },
      "monitoring": {},
      "name": "containerregistry.googleapis.com",
      "quota": {},
      "title": "Container Registry API",
      "usage": {
        "requirements": [
          "serviceusage.googleapis.com/tos/cloud",
          "serviceusage.googleapis.com/billing-enabled"
        ]
      }
    },
    "name": "projects/215695389495/services/containerregistry.googleapis.com",
    "parent": "projects/215695389495",
    "state": "ENABLED"
  },
  {
    "config": {
      "authentication": {},
      "documentation": {
        "summary": "Service to develop, version control, and operationalize SQL pipelines in BigQuery."
      },
      "monitoring": {},
      "name": "dataform.googleapis.com",
      "quota": {},
      "title": "Dataform API",
      "usage": {
        "requirements": [
          "serviceusage.googleapis.com/tos/cloud"
        ]
      }
    },
    "name": "projects/215695389495/services/dataform.googleapis.com",
    "parent": "projects/215695389495",
    "state": "ENABLED"
  },
  {
    "config": {
      "authentication": {},
      "documentation": {
        "summary": "Dataplex API is used to manage the lifecycle of data lakes."
      },
      "monitoredResources": [
        {
          "description": "A Cloud Dataplex Lake.",
          "displayName": "Cloud Dataplex Lake",
          "labels": [
            {
              "description": "The identifier of GCP project associated with this resource.",
              "key": "resource_container"
            },
            {
              "description": "The GCP region associated with this resource.",
              "key": "location"
            },
            {
              "description": "The identifier of this Lake resource.",
              "key": "lake_id"
            }
          ],
          "launchStage": "BETA",
          "type": "dataplex.googleapis.com/Lake"
        },
        {
          "description": "A Zone within a Cloud Dataplex Lake.",
          "displayName": "Cloud Dataplex Zone",
          "labels": [
            {
              "description": "The identifier of GCP project associated with this resource.",
              "key": "resource_container"
            },
            {
              "description": "The GCP region associated with this resource.",
              "key": "location"
            },
            {
              "description": "The identifier of the Lake resource containing this resource.",
              "key": "lake_id"
            },
            {
              "description": "The identifier of this Zone resource.",
              "key": "zone_id"
            }
          ],
          "launchStage": "BETA",
          "type": "dataplex.googleapis.com/Zone"
        },
        {
          "description": "An Asset within a Cloud Dataplex Lake.",
          "displayName": "Cloud Dataplex Asset",
          "labels": [
            {
              "description": "The identifier of GCP project associated with this resource.",
              "key": "resource_container"
            },
            {
              "description": "The GCP region associated with this resource.",
              "key": "location"
            },
            {
              "description": "The identifier of the Lake resource containing this resource.",
              "key": "lake_id"
            },
            {
              "description": "The identifier of the Zone resource containing this resource.",
              "key": "zone_id"
            },
            {
              "description": "The identifier of this Asset resource.",
              "key": "asset_id"
            }
          ],
          "launchStage": "BETA",
          "type": "dataplex.googleapis.com/Asset"
        },
        {
          "description": "An Environment within a Cloud Dataplex Lake.",
          "displayName": "Cloud Dataplex Environment",
          "labels": [
            {
              "description": "The identifier of GCP project associated with this resource.",
              "key": "resource_container"
            },
            {
              "description": "The GCP region associated with this resource.",
              "key": "location"
            },
            {
              "description": "The identifier of the Lake resource containing this resource.",
              "key": "lake_id"
            },
            {
              "description": "The identifier of this Environment resource.",
              "key": "environment_id"
            }
          ],
          "launchStage": "BETA",
          "type": "dataplex.googleapis.com/Environment"
        }
      ],
      "monitoring": {
        "consumerDestinations": [
          {
            "metrics": [
              "dataplex.googleapis.com/lake/requires_action"
            ],
            "monitoredResource": "dataplex.googleapis.com/Lake"
          },
          {
            "metrics": [
              "dataplex.googleapis.com/zone/requires_action"
            ],
            "monitoredResource": "dataplex.googleapis.com/Zone"
          },
          {
            "metrics": [
              "dataplex.googleapis.com/asset/requires_action",
              "dataplex.googleapis.com/asset/active",
              "dataplex.googleapis.com/asset/data_items",
              "dataplex.googleapis.com/asset/data_size",
              "dataplex.googleapis.com/asset/tables",
              "dataplex.googleapis.com/asset/filesets",
              "dataplex.googleapis.com/asset/entities_pending_bigquery_metadata_updates",
              "dataplex.googleapis.com/asset/entities_pending_bigquery_iampolicy_updates"
            ],
            "monitoredResource": "dataplex.googleapis.com/Asset"
          }
        ]
      },
      "name": "dataplex.googleapis.com",
      "quota": {},
      "title": "Cloud Dataplex API",
      "usage": {
        "requirements": [
          "serviceusage.googleapis.com/tos/cloud",
          "serviceusage.googleapis.com/tos/cloud"
        ]
      }
    },
    "name": "projects/215695389495/services/dataplex.googleapis.com",
    "parent": "projects/215695389495",
    "state": "ENABLED"
  },
  {
    "config": {
      "authentication": {},
      "documentation": {
        "summary": "Accesses the schemaless NoSQL database to provide fully managed, robust, scalable storage for your application.\n"
      },
      "monitoring": {},
      "name": "datastore.googleapis.com",
      "quota": {},
      "title": "Cloud Datastore API",
      "usage": {
        "requirements": [
          "serviceusage.googleapis.com/tos/cloud"
        ]
      }
    },
    "name": "projects/215695389495/services/datastore.googleapis.com",
    "parent": "projects/215695389495",
    "state": "ENABLED"
  },
  {
    "config": {
      "authentication": {},
      "documentation": {
        "summary": "Creates and manages rules that determine when a Firebase Rules-enabled service should permit a request.\n"
      },
      "monitoring": {},
      "name": "firebaserules.googleapis.com",
      "quota": {},
      "title": "Firebase Rules API",
      "usage": {
        "requirements": [
          "serviceusage.googleapis.com/tos/universal"
        ]
      }
    },
    "name": "projects/215695389495/services/firebaserules.googleapis.com",
    "parent": "projects/215695389495",
    "state": "ENABLED"
  },
  {
    "config": {
      "authentication": {},
      "documentation": {
        "summary": "Accesses the NoSQL document database built for automatic scaling, high performance, and ease of application development.\n"
      },
      "monitoredResources": [
        {
          "description": "A Firestore Database.",
          "displayName": "Firestore Database",
          "labels": [
            {
              "description": "The identifier of the GCP project associated with this resource.",
              "key": "resource_container"
            },
            {
              "description": "The location of the database.",
              "key": "location"
            },
            {
              "description": "The database id.",
              "key": "database_id"
            }
          ],
          "launchStage": "BETA",
          "type": "firestore.googleapis.com/Database"
        }
      ],
      "monitoring": {
        "consumerDestinations": [
          {
            "metrics": [
              "firestore.googleapis.com/composite_indexes_per_database",
              "firestore.googleapis.com/quota/composite_indexes_per_database/exceeded"
            ],
            "monitoredResource": "firestore.googleapis.com/Database"
          },
          {
            "metrics": [
              "firestore.googleapis.com/quota/composite_indexes_per_database/limit",
              "firestore.googleapis.com/quota/composite_indexes_per_database/usage"
            ],
            "monitoredResource": "firestore.googleapis.com/Database"
          }
        ]
      },
      "name": "firestore.googleapis.com",
      "quota": {},
      "title": "Cloud Firestore API",
      "usage": {
        "requirements": [
          "serviceusage.googleapis.com/tos/cloud"
        ]
      }
    },
    "name": "projects/215695389495/services/firestore.googleapis.com",
    "parent": "projects/215695389495",
    "state": "ENABLED"
  },
  {
    "config": {
      "authentication": {},
      "documentation": {
        "summary": "View your database traffic patterns in Firestore Key Visualizer."
      },
      "monitoring": {},
      "name": "firestorekeyvisualizer.googleapis.com",
      "quota": {},
      "title": "Firestore Key Visualizer API",
      "usage": {
        "requirements": [
          "serviceusage.googleapis.com/tos/cloud"
        ]
      }
    },
    "name": "projects/215695389495/services/firestorekeyvisualizer.googleapis.com",
    "parent": "projects/215695389495",
    "state": "ENABLED"
  },
  {
    "config": {
      "authentication": {},
      "documentation": {
        "summary": "Manages identity and access control for Google Cloud resources, including the creation of service accounts, which you can use to authenticate to Google and make API calls. Enabling this API also enables the IAM Service Account Credentials API (iamcredentials.googleapis.com). However, disabling this API doesn't disable the IAM Service Account Credentials API.\n"
      },
      "monitoredResources": [
        {
          "description": "An IAM Service Account.",
          "displayName": "IAM Service Account",
          "labels": [
            {
              "description": "The identifier of the GCP project associated with this resource, such as 'my-project'.",
              "key": "project_id"
            },
            {
              "description": "The unique_id of the service account.",
              "key": "unique_id"
            }
          ],
          "launchStage": "GA",
          "type": "iam_service_account"
        },
        {
          "description": "A workload identity pool provider.",
          "displayName": "Workload Identity Pool Provider",
          "labels": [
            {
              "description": "The identifier of the GCP project associated with this resource, such as 'my-project'.",
              "key": "resource_container"
            },
            {
              "description": "The location of the resource.",
              "key": "location"
            },
            {
              "description": "The ID of the provider's workload identity pool parent resource.",
              "key": "pool_id"
            },
            {
              "description": "The ID of the workload identity pool provider resource.",
              "key": "provider_id"
            }
          ],
          "launchStage": "BETA",
          "type": "iam.googleapis.com/WorkloadIdentityPoolProvider"
        },
        {
          "description": "A workforce identity pool provider.",
          "displayName": "Workforce Identity Pool Provider",
          "labels": [
            {
              "description": "The identifier of the Google Cloud organization associated with this resource.",
              "key": "resource_container"
            },
            {
              "description": "The location of the resource.",
              "key": "location"
            },
            {
              "description": "The ID of the provider's workforce pool parent resource.",
              "key": "pool_id"
            },
            {
              "description": "The ID of the workforce pool provider resource.",
              "key": "provider_id"
            }
          ],
          "launchStage": "BETA",
          "type": "iam.googleapis.com/WorkforcePoolProvider"
        }
      ],
      "monitoring": {
        "consumerDestinations": [
          {
            "metrics": [
              "iam.googleapis.com/workload_identity_federation/count",
              "iam.googleapis.com/workload_identity_federation/key_usage_count"
            ],
            "monitoredResource": "iam.googleapis.com/WorkloadIdentityPoolProvider"
          },
          {
            "metrics": [
              "iam.googleapis.com/service_account/authn_events_count",
              "iam.googleapis.com/service_account/key/authn_events_count",
              "iam.googleapis.com/service_account/authn_events_count_preprod",
              "iam.googleapis.com/service_account/key/authn_events_count_preprod"
            ],
            "monitoredResource": "iam_service_account"
          },
          {
            "metrics": [
              "iam.googleapis.com/workforce_identity_federation/count"
            ],
            "monitoredResource": "iam.googleapis.com/WorkforcePoolProvider"
          }
        ]
      },
      "name": "iam.googleapis.com",
      "quota": {},
      "title": "Identity and Access Management (IAM) API",
      "usage": {
        "requirements": [
          "serviceusage.googleapis.com/tos/cloud"
        ]
      }
    },
    "name": "projects/215695389495/services/iam.googleapis.com",
    "parent": "projects/215695389495",
    "state": "ENABLED"
  },
  {
    "config": {
      "authentication": {},
      "documentation": {
        "summary": "Creates short-lived credentials for impersonating IAM service accounts. Disabling this API also disables the IAM API (iam.googleapis.com). However, enabling this API doesn't enable the IAM API.\n"
      },
      "monitoring": {},
      "name": "iamcredentials.googleapis.com",
      "quota": {},
      "title": "IAM Service Account Credentials API",
      "usage": {
        "requirements": [
          "serviceusage.googleapis.com/tos/cloud"
        ]
      }
    },
    "name": "projects/215695389495/services/iamcredentials.googleapis.com",
    "parent": "projects/215695389495",
    "state": "ENABLED"
  },
  {
    "config": {
      "authentication": {},
      "documentation": {
        "summary": "Controls access to cloud applications running on Google Cloud Platform."
      },
      "monitoring": {},
      "name": "iap.googleapis.com",
      "quota": {},
      "title": "Cloud Identity-Aware Proxy API",
      "usage": {
        "requirements": [
          "serviceusage.googleapis.com/tos/cloud"
        ]
      }
    },
    "name": "projects/215695389495/services/iap.googleapis.com",
    "parent": "projects/215695389495",
    "state": "ENABLED"
  },
  {
    "config": {
      "authentication": {},
      "documentation": {
        "summary": "Writes log entries and manages your Cloud Logging configuration."
      },
      "monitoredResources": [
        {
          "description": "A cloud logging specialization target schema of cloud.ChargedProject.",
          "displayName": "Cloud logging target",
          "labels": [
            {
              "description": "The monitored resource container. Could be project, workspace, etc.",
              "key": "resource_container"
            },
            {
              "description": "The service-specific notion of location.",
              "key": "location"
            },
            {
              "description": "The name of the API service with which the data is associated (e.g.,'logging.googleapis.com').",
              "key": "service"
            }
          ],
          "launchStage": "ALPHA",
          "type": "logging.googleapis.com/ChargedProject"
        }
      ],
      "monitoring": {
        "consumerDestinations": [
          {
            "metrics": [
              "logging.googleapis.com/billing/ingested_bytes",
              "logging.googleapis.com/billing/stored_bytes"
            ],
            "monitoredResource": "logging.googleapis.com/ChargedProject"
          }
        ]
      },
      "name": "logging.googleapis.com",
      "quota": {},
      "title": "Cloud Logging API",
      "usage": {
        "requirements": [
          "serviceusage.googleapis.com/tos/cloud"
        ]
      }
    },
    "name": "projects/215695389495/services/logging.googleapis.com",
    "parent": "projects/215695389495",
    "state": "ENABLED"
  },
  {
    "config": {
      "authentication": {},
      "documentation": {
        "summary": "Manages your Cloud Monitoring data and configurations.\n"
      },
      "monitoredResources": [
        {
          "description": "A cloud monitoring specialization target schema of cloud.ChargedProject.",
          "displayName": "Cloud monitoring target",
          "labels": [
            {
              "description": "The monitored resource container. Could be project, workspace, etc.",
              "key": "resource_container"
            },
            {
              "description": "The service-specific notion of location.",
              "key": "location"
            },
            {
              "description": "The name of the API service with which the data is associated (e.g.,'monitoring.googleapis.com').",
              "key": "service"
            }
          ],
          "launchStage": "ALPHA",
          "type": "monitoring.googleapis.com/ChargedProject"
        },
        {
          "description": "Information about a user-written metric in Cloud Monitoring.",
          "displayName": "Metric Statistics",
          "labels": [
            {
              "description": "The identifier of the GCP project to which the metric is written, such as 'my-project'.",
              "key": "resource_container"
            },
            {
              "description": "The cloud region where the metric was received.",
              "key": "location"
            },
            {
              "description": "The metric type.",
              "key": "metric_type"
            }
          ],
          "launchStage": "BETA",
          "type": "monitoring.googleapis.com/MetricStatistics"
        },
        {
          "description": "Attribution for metric ingestion.",
          "displayName": "Metric Ingestion Attribution",
          "labels": [
            {
              "description": "The identifier of the GCP project to which the metric is written, such as 'my-project'.",
              "key": "resource_container"
            },
            {
              "description": "The location of the resource that the metric ingestion was associated with, unless it was 'global', in which case this will be the cloud region where the metric was received.",
              "key": "location"
            },
            {
              "description": "The dimension used for attribution reporting. It is not recommended that aggregations are performed across dimensions because a single metric point can be recorded with multiple dimensions which could cause double counting. Currently only \"namespace\" and \"cluster\" are supported.",
              "key": "attribution_dimension"
            },
            {
              "description": "The attribution id of the source of the metric write.",
              "key": "attribution_id"
            }
          ],
          "launchStage": "BETA",
          "type": "monitoring.googleapis.com/MetricIngestionAttribution"
        }
      ],
      "monitoring": {
        "consumerDestinations": [
          {
            "metrics": [
              "monitoring.googleapis.com/billing/bytes_ingested",
              "monitoring.googleapis.com/billing/samples_ingested",
              "monitoring.googleapis.com/internal/billing/gke_enterprise_samples_ingested",
              "monitoring.googleapis.com/internal/billing/non_chargeable_samples_ingested",
              "monitoring.googleapis.com/internal/stats/filtered_sample_count",
              "monitoring.googleapis.com/internal/stats/filtered_byte_count",
              "monitoring.googleapis.com/internal/stats/metrics_queried_count"
            ],
            "monitoredResource": "monitoring.googleapis.com/ChargedProject"
          },
          {
            "metrics": [
              "monitoring.googleapis.com/collection/write_request_count",
              "monitoring.googleapis.com/collection/write_request_point_count"
            ],
            "monitoredResource": "monitoring.googleapis.com/MetricStatistics"
          },
          {
            "metrics": [
              "monitoring.googleapis.com/collection/attribution/sample_count",
              "monitoring.googleapis.com/collection/attribution/write_sample_count"
            ],
            "monitoredResource": "monitoring.googleapis.com/MetricIngestionAttribution"
          }
        ]
      },
      "name": "monitoring.googleapis.com",
      "quota": {},
      "title": "Cloud Monitoring API",
      "usage": {
        "requirements": [
          "serviceusage.googleapis.com/tos/cloud"
        ]
      }
    },
    "name": "projects/215695389495/services/monitoring.googleapis.com",
    "parent": "projects/215695389495",
    "state": "ENABLED"
  },
  {
    "config": {
      "authentication": {},
      "documentation": {
        "summary": "You can use OS Login to manage access to your VM instances using IAM roles."
      },
      "monitoring": {},
      "name": "oslogin.googleapis.com",
      "quota": {},
      "title": "Cloud OS Login API",
      "usage": {
        "requirements": [
          "serviceusage.googleapis.com/tos/cloud"
        ]
      }
    },
    "name": "projects/215695389495/services/oslogin.googleapis.com",
    "parent": "projects/215695389495",
    "state": "ENABLED"
  },
  {
    "config": {
      "authentication": {},
      "documentation": {
        "summary": "Provides reliable, many-to-many, asynchronous messaging between applications.\n"
      },
      "monitoring": {},
      "name": "pubsub.googleapis.com",
      "quota": {},
      "title": "Cloud Pub/Sub API",
      "usage": {
        "requirements": [
          "serviceusage.googleapis.com/tos/cloud"
        ]
      }
    },
    "name": "projects/215695389495/services/pubsub.googleapis.com",
    "parent": "projects/215695389495",
    "state": "ENABLED"
  },
  {
    "config": {
      "authentication": {},
      "documentation": {
        "summary": "Deploy and manage user provided container images that scale automatically based on incoming requests. The Cloud Run Admin API v1 follows the Knative Serving API specification, while v2 is aligned with Google Cloud AIP-based API standards, as described in https://google.aip.dev/."
      },
      "monitoredResources": [
        {
          "labels": [
            {
              "key": "cloud.googleapis.com/project"
            },
            {
              "key": "run.googleapis.com/service_name"
            },
            {
              "key": "run.googleapis.com/revision_name"
            },
            {
              "key": "cloud.googleapis.com/location"
            },
            {
              "key": "run.googleapis.com/configuration_name"
            },
            {
              "key": "cloud.googleapis.com/uid"
            }
          ],
          "type": "run.googleapis.com/revision"
        }
      ],
      "monitoring": {
        "consumerDestinations": [
          {
            "metrics": [
              "run.googleapis.com/request_count",
              "run.googleapis.com/request_latencies",
              "run.googleapis.com/container/instance_time",
              "run.googleapis.com/container/cpu/allocation_time",
              "run.googleapis.com/container/memory/allocation_time",
              "run.googleapis.com/container/labelled_instance_time",
              "run.googleapis.com/container/cpu/scaled_usage",
              "run.googleapis.com/container/memory/utilization",
              "run.googleapis.com/tenant_project",
              "run.googleapis.com/internal/eventflow_filter/cloudevent_recordedtime_latencies",
              "run.googleapis.com/internal/eventflow_filter/cloudevent_time_latencies",
              "run.googleapis.com/internal/eventflow_filter/transformation_count",
              "run.googleapis.com/internal/eventflow_filter/transformation_latencies",
              "run.googleapis.com/internal/pod_service_client/request_count",
              "run.googleapis.com/internal/pod_service_client/request_latencies"
            ],
            "monitoredResource": "run.googleapis.com/revision"
          }
        ]
      },
      "name": "run.googleapis.com",
      "quota": {},
      "title": "Cloud Run Admin API",
      "usage": {
        "requirements": [
          "serviceusage.googleapis.com/tos/cloud",
          "serviceusage.googleapis.com/billing-enabled"
        ]
      }
    },
    "name": "projects/215695389495/services/run.googleapis.com",
    "parent": "projects/215695389495",
    "state": "ENABLED"
  },
  {
    "config": {
      "authentication": {},
      "documentation": {
        "summary": "Google Service Management allows service producers to publish their services on Google Cloud Platform so that they can be discovered and used by service consumers."
      },
      "monitoring": {},
      "name": "servicemanagement.googleapis.com",
      "quota": {},
      "title": "Service Management API",
      "usage": {
        "requirements": [
          "serviceusage.googleapis.com/tos/cloud"
        ]
      }
    },
    "name": "projects/215695389495/services/servicemanagement.googleapis.com",
    "parent": "projects/215695389495",
    "state": "ENABLED"
  },
  {
    "config": {
      "authentication": {},
      "documentation": {
        "summary": "Enables services that service consumers want to use on Google Cloud Platform, lists the available or enabled services, or disables services that service consumers no longer use."
      },
      "monitoring": {},
      "name": "serviceusage.googleapis.com",
      "quota": {},
      "title": "Service Usage API",
      "usage": {
        "requirements": [
          "serviceusage.googleapis.com/tos/cloud"
        ]
      }
    },
    "name": "projects/215695389495/services/serviceusage.googleapis.com",
    "parent": "projects/215695389495",
    "state": "ENABLED"
  },
  {
    "config": {
      "authentication": {},
      "documentation": {
        "summary": "Google Cloud SQL is a hosted and fully managed relational database service\n    on Google's infrastructure."
      },
      "monitoredResources": [
        {
          "labels": [
            {
              "key": "cloud.googleapis.com/location"
            },
            {
              "key": "cloud.googleapis.com/uid"
            },
            {
              "key": "serviceruntime.googleapis.com/api_version"
            },
            {
              "key": "serviceruntime.googleapis.com/api_method"
            },
            {
              "key": "serviceruntime.googleapis.com/consumer_project"
            },
            {
              "key": "cloud.googleapis.com/project"
            },
            {
              "key": "cloud.googleapis.com/service"
            }
          ],
          "type": "serviceruntime.googleapis.com/api"
        },
        {
          "labels": [
            {
              "key": "cloud.googleapis.com/location"
            },
            {
              "key": "cloud.googleapis.com/uid"
            },
            {
              "key": "cloud.googleapis.com/service"
            },
            {
              "key": "cloud.googleapis.com/resource_id"
            },
            {
              "key": "cloud.googleapis.com/resource_node"
            },
            {
              "key": "cloud.googleapis.com/quota_metric"
            },
            {
              "key": "cloud.googleapis.com/quota_location"
            }
          ],
          "type": "serviceruntime.googleapis.com/consumer_quota"
        },
        {
          "labels": [
            {
              "key": "cloud.googleapis.com/location"
            },
            {
              "key": "cloud.googleapis.com/uid"
            },
            {
              "key": "cloud.googleapis.com/service"
            },
            {
              "key": "cloud.googleapis.com/resource_id"
            },
            {
              "key": "cloud.googleapis.com/resource_node"
            },
            {
              "key": "cloud.googleapis.com/consumer_resource_node"
            },
            {
              "key": "cloud.googleapis.com/quota_metric"
            },
            {
              "key": "cloud.googleapis.com/quota_location"
            }
          ],
          "type": "serviceruntime.googleapis.com/producer_quota"
        }
      ],
      "monitoring": {
        "consumerDestinations": [
          {
            "metrics": [
              "serviceruntime.googleapis.com/api/consumer/request_count",
              "serviceruntime.googleapis.com/api/consumer/error_count",
              "serviceruntime.googleapis.com/api/consumer/quota_used_count",
              "serviceruntime.googleapis.com/api/consumer/quota_refund_count",
              "serviceruntime.googleapis.com/api/consumer/total_latencies",
              "serviceruntime.googleapis.com/api/consumer/request_overhead_latencies",
              "serviceruntime.googleapis.com/api/consumer/backend_latencies",
              "serviceruntime.googleapis.com/api/consumer/request_sizes",
              "serviceruntime.googleapis.com/api/consumer/response_sizes",
              "serviceruntime.googleapis.com/api/consumer/top_request_count_by_end_user",
              "serviceruntime.googleapis.com/api/consumer/top_request_count_by_end_user_country",
              "serviceruntime.googleapis.com/api/consumer/top_request_count_by_referer",
              "serviceruntime.googleapis.com/quota/used",
              "serviceruntime.googleapis.com/quota/limit",
              "serviceruntime.googleapis.com/quota/exceeded",
              "serviceruntime.googleapis.com/allocation/consumer/quota_used_count"
            ],
            "monitoredResource": "serviceruntime.googleapis.com/api"
          },
          {
            "metrics": [
              "serviceruntime.googleapis.com/quota/rate/consumer/used_count",
              "serviceruntime.googleapis.com/quota/rate/consumer/refund_count",
              "serviceruntime.googleapis.com/quota/allocation/consumer/usage",
              "serviceruntime.googleapis.com/quota/consumer/limit",
              "serviceruntime.googleapis.com/quota/consumer/exceeded"
            ],
            "monitoredResource": "serviceruntime.googleapis.com/consumer_quota"
          }
        ]
      },
      "name": "sql-component.googleapis.com",
      "quota": {},
      "title": "Cloud SQL",
      "usage": {
        "requirements": [
          "serviceusage.googleapis.com/tos/cloud"
        ]
      }
    },
    "name": "projects/215695389495/services/sql-component.googleapis.com",
    "parent": "projects/215695389495",
    "state": "ENABLED"
  },
  {
    "config": {
      "authentication": {},
      "documentation": {
        "summary": "Lets you store and retrieve potentially-large, immutable data objects."
      },
      "monitoring": {},
      "name": "storage-api.googleapis.com",
      "quota": {},
      "title": "Google Cloud Storage JSON API",
      "usage": {
        "requirements": [
          "serviceusage.googleapis.com/tos/cloud"
        ]
      }
    },
    "name": "projects/215695389495/services/storage-api.googleapis.com",
    "parent": "projects/215695389495",
    "state": "ENABLED"
  },
  {
    "config": {
      "authentication": {},
      "documentation": {
        "summary": "Google Cloud Storage is a RESTful service for storing and accessing your data on Google's\n    infrastructure."
      },
      "monitoredResources": [
        {
          "labels": [
            {
              "key": "cloud.googleapis.com/location"
            },
            {
              "key": "cloud.googleapis.com/uid"
            },
            {
              "key": "serviceruntime.googleapis.com/api_version"
            },
            {
              "key": "serviceruntime.googleapis.com/api_method"
            },
            {
              "key": "serviceruntime.googleapis.com/consumer_project"
            },
            {
              "key": "cloud.googleapis.com/project"
            },
            {
              "key": "cloud.googleapis.com/service"
            }
          ],
          "type": "serviceruntime.googleapis.com/api"
        },
        {
          "labels": [
            {
              "key": "cloud.googleapis.com/location"
            },
            {
              "key": "cloud.googleapis.com/uid"
            },
            {
              "key": "cloud.googleapis.com/service"
            },
            {
              "key": "cloud.googleapis.com/resource_id"
            },
            {
              "key": "cloud.googleapis.com/resource_node"
            },
            {
              "key": "cloud.googleapis.com/quota_metric"
            },
            {
              "key": "cloud.googleapis.com/quota_location"
            }
          ],
          "type": "serviceruntime.googleapis.com/consumer_quota"
        },
        {
          "labels": [
            {
              "key": "cloud.googleapis.com/location"
            },
            {
              "key": "cloud.googleapis.com/uid"
            },
            {
              "key": "cloud.googleapis.com/service"
            },
            {
              "key": "cloud.googleapis.com/resource_id"
            },
            {
              "key": "cloud.googleapis.com/resource_node"
            },
            {
              "key": "cloud.googleapis.com/consumer_resource_node"
            },
            {
              "key": "cloud.googleapis.com/quota_metric"
            },
            {
              "key": "cloud.googleapis.com/quota_location"
            }
          ],
          "type": "serviceruntime.googleapis.com/producer_quota"
        }
      ],
      "monitoring": {
        "consumerDestinations": [
          {
            "metrics": [
              "serviceruntime.googleapis.com/api/consumer/request_count",
              "serviceruntime.googleapis.com/api/consumer/error_count",
              "serviceruntime.googleapis.com/api/consumer/quota_used_count",
              "serviceruntime.googleapis.com/api/consumer/quota_refund_count",
              "serviceruntime.googleapis.com/api/consumer/total_latencies",
              "serviceruntime.googleapis.com/api/consumer/request_overhead_latencies",
              "serviceruntime.googleapis.com/api/consumer/backend_latencies",
              "serviceruntime.googleapis.com/api/consumer/request_sizes",
              "serviceruntime.googleapis.com/api/consumer/response_sizes",
              "serviceruntime.googleapis.com/api/consumer/top_request_count_by_end_user",
              "serviceruntime.googleapis.com/api/consumer/top_request_count_by_end_user_country",
              "serviceruntime.googleapis.com/api/consumer/top_request_count_by_referer",
              "serviceruntime.googleapis.com/quota/used",
              "serviceruntime.googleapis.com/quota/limit",
              "serviceruntime.googleapis.com/quota/exceeded",
              "serviceruntime.googleapis.com/allocation/consumer/quota_used_count"
            ],
            "monitoredResource": "serviceruntime.googleapis.com/api"
          },
          {
            "metrics": [
              "serviceruntime.googleapis.com/quota/rate/consumer/used_count",
              "serviceruntime.googleapis.com/quota/rate/consumer/refund_count",
              "serviceruntime.googleapis.com/quota/allocation/consumer/usage",
              "serviceruntime.googleapis.com/quota/consumer/limit",
              "serviceruntime.googleapis.com/quota/consumer/exceeded"
            ],
            "monitoredResource": "serviceruntime.googleapis.com/consumer_quota"
          }
        ]
      },
      "name": "storage-component.googleapis.com",
      "quota": {},
      "title": "Cloud Storage",
      "usage": {
        "requirements": [
          "serviceusage.googleapis.com/tos/cloud"
        ]
      }
    },
    "name": "projects/215695389495/services/storage-component.googleapis.com",
    "parent": "projects/215695389495",
    "state": "ENABLED"
  },
  {
    "config": {
      "authentication": {},
      "documentation": {
        "summary": "Lets you store and retrieve potentially-large, immutable data objects."
      },
      "monitoredResources": [
        {
          "description": "GCS Location.",
          "displayName": "GCS Location",
          "labels": [
            {
              "description": "The project number of the bucket.",
              "key": "resource_container"
            },
            {
              "description": "The location of the bucket.",
              "key": "location"
            }
          ],
          "launchStage": "ALPHA",
          "type": "storage.googleapis.com/Location"
        },
        {
          "description": "GCS Project.",
          "displayName": "GCS Project",
          "labels": [
            {
              "description": "The identifier of the GCP project associated with this resource, such as \\\"my-project\\\".",
              "key": "resource_container"
            },
            {
              "description": "The location where the quota is consumed. It is a region for regional quota, or a zone for zonal quota, or \\\"global\\\" otherwise.",
              "key": "location"
            }
          ],
          "launchStage": "GA",
          "type": "storage.googleapis.com/Project"
        },
        {
          "labels": [
            {
              "key": "storage.googleapis.com/bucket_name"
            },
            {
              "key": "storage.googleapis.com/bucket_storage_class"
            },
            {
              "key": "cloud.googleapis.com/location"
            },
            {
              "key": "cloud.googleapis.com/project"
            }
          ],
          "type": "storage.googleapis.com/storage"
        },
        {
          "description": "storage.googleapis.com/Storage target schema.",
          "displayName": "Cloud storage target schema.",
          "labels": [
            {
              "description": "The monitored resource container. Usually a project.",
              "key": "resource_container"
            },
            {
              "description": "The location of the resource.",
              "key": "location"
            },
            {
              "description": "The bucket name associated with the resource.",
              "key": "bucket_name"
            }
          ],
          "launchStage": "ALPHA",
          "type": "storage.googleapis.com/Storage"
        }
      ],
      "monitoring": {
        "consumerDestinations": [
          {
            "metrics": [
              "storage.googleapis.com/storage/total_bytes",
              "storage.googleapis.com/storage/object_count"
            ],
            "monitoredResource": "storage.googleapis.com/storage"
          },
          {
            "metrics": [
              "storage.googleapis.com/quota/turbo_replication_ingress_bandwidth/exceeded",
              "storage.googleapis.com/quota/turbo_replication_ingress_bandwidth/usage"
            ],
            "monitoredResource": "storage.googleapis.com/Location"
          },
          {
            "metrics": [
              "storage.googleapis.com/dualregion_google_egress_bandwidth",
              "storage.googleapis.com/dualregion_internet_egress_bandwidth",
              "storage.googleapis.com/quota/dualregion_anywhere_cache_egress_bandwidth/exceeded",
              "storage.googleapis.com/quota/dualregion_anywhere_cache_egress_bandwidth/usage",
              "storage.googleapis.com/quota/dualregion_google_egress_bandwidth/exceeded",
              "storage.googleapis.com/quota/dualregion_google_egress_bandwidth/usage",
              "storage.googleapis.com/quota/dualregion_internet_egress_bandwidth/exceeded",
              "storage.googleapis.com/quota/dualregion_internet_egress_bandwidth/usage",
              "storage.googleapis.com/quota/dualregion_request_rate/exceeded",
              "storage.googleapis.com/quota/dualregion_request_rate/usage"
            ],
            "monitoredResource": "storage.googleapis.com/Project"
          },
          {
            "metrics": [
              "storage.googleapis.com/quota/dualregion_anywhere_cache_egress_bandwidth/limit",
              "storage.googleapis.com/quota/dualregion_google_egress_bandwidth/limit",
              "storage.googleapis.com/quota/dualregion_internet_egress_bandwidth/limit",
              "storage.googleapis.com/quota/dualregion_request_rate/limit"
            ],
            "monitoredResource": "storage.googleapis.com/Project"
          },
          {
            "metrics": [
              "storage.googleapis.com/quota/turbo_replication_ingress_bandwidth/limit"
            ],
            "monitoredResource": "storage.googleapis.com/Location"
          },
          {
            "metrics": [
              "storage.googleapis.com/anywhere_cache_metering/cache_storage_kbsec_count",
              "storage.googleapis.com/anywhere_cache_metering/eviction_byte_count"
            ],
            "monitoredResource": "storage.googleapis.com/Storage"
          }
        ]
      },
      "name": "storage.googleapis.com",
      "quota": {},
      "title": "Cloud Storage API",
      "usage": {
        "requirements": [
          "serviceusage.googleapis.com/tos/cloud"
        ]
      }
    },
    "name": "projects/215695389495/services/storage.googleapis.com",
    "parent": "projects/215695389495",
    "state": "ENABLED"
  }
]
'''  # NOQA
