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
                "bucketName": "systemical-SERVICE-files-dev"
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
  "certificate": "-----BEGIN CERTIFICATE-----\n-----END CERTIFICATE-----\n",
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
}
"""  # NOQA

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
