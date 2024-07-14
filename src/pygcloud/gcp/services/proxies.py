"""
echo "INFO: Checking status of HTTPS Proxy '${NAME}'"
gcloud compute target-https-proxies describe ${NAME} \
      --project=${PROJECT_ID} 2>/dev/null 1>/dev/null

if [ $? -eq 0 ]; then
    echo "NOTICE: ${NAME} already exists"
    _ACTION="update"
fi

_ACTION="${_ACTION:-create}"

echo "INFO: HTTPS Proxy $_ACTION '${NAME}'..."
gcloud compute target-https-proxies ${_ACTION} ${NAME} \
      --ssl-certificates=${NAME_CERTIFICATE} \
      --url-map=${NAME_URL_MAP} \
      --project=${PROJECT_ID} 2>/dev/null

@author: jldupont
"""
from pygcloud.models import GCPServiceUpdatable


class HTTPSProxyService(GCPServiceUpdatable):
    """
    https://cloud.google.com/sdk/gcloud/reference/beta/compute/target-https-proxies
    """
    REQUIRES_DESCRIBE_BEFORE_CREATE = True
    PREFIX = ["compute", "target-https-proxies"]

    def __init__(self, name: str, ssl_certificate_name: str,
                 url_map_name: str):
        assert isinstance(ssl_certificate_name, str)
        assert isinstance(url_map_name, str)
        super().__init__(name=name, ns="https-proxy")
        self._ssl_certificate_name = ssl_certificate_name
        self._url_map_name = url_map_name

    def params_describe(self):
        return self.PREFIX + [
            "describe", self.name,
        ]

    def params_create(self):
        return self.PREFIX + [
            "create",
            "--ssl-certificates", self._ssl_certificate_name,
            "--url-map", self._url_map_name
        ]

    def params_update(self):
        return self.PREFIX + [
            "update",
            "--ssl-certificates", self._ssl_certificate_name,
            "--url-map", self._url_map_name
        ]
