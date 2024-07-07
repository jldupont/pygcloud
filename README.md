# Purpose

Wouldn't be nice to script your GCP infrastructure without having to learn a new language ?

# Description

This package simplifies the deployment of GCP services through the gcloud command line.

# Installation

`pip install pygcloud`

# Requirements

* Leverage `gcloud` command line tool
* Be as transparent to `gcloud` as possible
* Capability to group deployment of services together
* Capability to describe relationships between services
* Capability to perform trial run

# Enabling Features 

* Infrastructure governance
* Diagramming

The above features are supported by employing the `after_*` methods of the `GCPService` class.

# Categories of Services

1. SingletonImmutable e.g. Firestore indexes
2. RevisionBased e.g. Cloud Run service with revisions
3. Updatable e.g. GCS bucket

For the "SingletonImmutable" category, we ignore exceptions arising from the service already being created. The "describe" facility might be or not available.

For the "RevisionBased", we skip the "update" step. The "create" method will be called. The "describe" facility might be or not available.

For the "Updatable", we do the complete steps i.e. describe, create or update.

# Usage

TODO

# Links

* [Repository](https://github.com/jldupont/pygcloud)
* [Pypi](https://pypi.org/project/pygcloud/)

