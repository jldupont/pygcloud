Much information is available to `pygcloud` when it is used to police and deploy infrastructure. This information can be used to build a graph of the services (nodes) and relationships (edges) between them.

# Available Information

* Service
  * Class (e.g. Cloud Run)
  * Name

There are different level of information available by service but the aforementionned are very common. Some resources do not have have names but only auto generated IDs (e.g. Firestore indexes): even in these cases, some valuable processes can be applied to them (e.g. policing).

* Relationships
  * "Has parent" (e.g. the service's parent project)
  * "Used by" (e.g. Backend service referring to a URL Map)
  * "Uses" (e.g. HTTPS Proxy uses URL Map)
  * "Member of" (e.g. pygcloud service group)

## IAM Bindings

The bindings provided information as to which service(s) (or application running on it) service accounts can perform on which other service(s). This information informs the `uses` relationship type.

## Explainability

Each reported relationship is labelled with a reference as to the `source`:

* From the service specification (gcloud ... describe)
* From the IAM bindings (project and service/resource levels)

# Relationships

The goal is to leverage the inherent relationships between GCP services as much as possible in order to limit the burden already imposed building the infrastructure.

The usage of the `policing` function can help surface more information: a good example is forcing the use of dedicated service accounts on compute related services and service level IAM bindings compared to using default (GCP provided) service accounts.

The only supported relation type is unidirectional.

The only non-native relation supported at the moment is `service group` used at deployment time.

## Used By

Why keep the "USED_BY" relation type as opposed to just exchanging nodes in an edge definition ?
It is to preserve the explicit information out of GCP as much as possible without performing
transformation to it.

# Grouping

The "group" construct is abstract by nature.

At the moment, there is only one group type defined: "Deployment Service Group". It is very likely we will want to introduce more group types in the future. In order to prepare for this future state, we need to make some provisions ahead of time in order to limit backward compatibility challenges.

In terms of requirements, I believe the following are valuable:

* Support backward compatibility
* Support type hinting
* Support user generated group types

## User defined groups

```python
# Some other tyoe of logical grouping for operational purposes maybe ?
group = SomeUserDefinedGroupClass(...)

srv = StorageBucket(...)
group.append(srv)

# Of the goals is to actually deploy this service too
deployment_group.append(srv)
```

## Implementation

There are a number of ways to solution for the group type and its role with the other graph related types. In order to account for the requirements above though, we can have a good level of confidence that a class based approach will meet them.

In terms of how this type fits with the others (i.e. Node, Edge), we have different options:

1. We could have the Node type contain a list of Groups for which it is member of
2. We could have the "Group" type with a list of Nodes
3. We could have another type "Members" which would reference both a "Group" and its member Nodes

By following the strategy "separation of concerns", option 3 comes on top.

# API in support of graphing

A generator based API is provided.

# Examples

TODO

# Future considerations

* Support for declaring non-native relationships (e.g. grouping of services differently than deployment level)
* Support for declaring external services and resources

