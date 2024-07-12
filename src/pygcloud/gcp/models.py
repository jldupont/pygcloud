"""
Data models related to GCP services

@author: jldupont
"""
from typing import List
from dataclasses import dataclass


@dataclass
class IAMBindings:

    members: List[str]
    role: str


@dataclass
class IAMBinding:
    """
    By default, if the 'email' does not
    contain a namespace prefix, it will be
    set to "serviceAccount"
    """

    ns: str
    email: str
    role: str

    def __post_init__(self):

        maybe_split = self.email.split(":")
        if len(maybe_split) == 2:
            self.ns = maybe_split[0]
            self.email = maybe_split[1]
        else:
            self.ns = "serviceAccount"

    @property
    def sa_email(self):
        return f"{self.ns}:{self.email}"
