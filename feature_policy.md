# Policing Infrastructure

`pygcloud` supports policing of infrastructure deployments. It can perform this function by inspecting the services listed for deployment in the `service group(s)`.

# Some Use-Cases

* Checking for isolated resources: some resources / services typically do not provide a solution in isolation e.g. Cloud Run service without a secure way of accessing it.

* Checking for dedicated service accounts instead of relying on the default: this is just good secure practice which helps enforce "least privileges" strategy

For a comprehensive list of policing strategies, see **TODO**

## Policy Categories

* Functional: policies that support checking for a functional solution
* Security: policies that support security measures

# Requirements

* Support development time i.e. not all services of the solution might be decided yet
* Support `dry run` policing to evaluate compliance
* Support `production` deployment phase policing
* Support for all supported `GCPService` classes (when applicable)
* Support for post-deployment policing

# How it works

* Policies can be evaluated followed, or not, by the deployment phase
* Policies can be evaluated after a deployment phase with the benefit of having access to more information
* Policies can be evaluated in `dry run` or `production` mode
  * In `dry run`, policy exception(s) are logged without exiting
  * In `production`, the first policy exception exists the process
* Policies are evaluated one after the other
* Policies are evaluated on the whole of the deployment i.e. all service groups are in scope

# Usage

By default, the default policies are enabled: this ensures a sensible security posture whilst also providing feedback. 

```python
    Policer.police()
```

It is possible to customize this.

## Customization

* Each policy is defined in a class
* Each policy can be enabled / disabled
* Custom policies can be defined

```python
    Policer.disable(policy_class) # this will emit a warning
```

All policies are derived from the `Policy` based class.

```python
    from pygcloud.models import Policy, GCPService

    class MyPolicy(Policy):
        ...

    # Once a policy is declared, it is automatically
    # added to the list of enabled policies.

    # Disable whilst testing it out.
    # The policy will still be evaluated with
    # accompanied warning messages.
    # Exceptions will not stop the Policer.
    Policer.disable(MyPolicy)

    class SomeGCPService(GCPService):
        ...

    #
    # A service can be allowed by default.
    # This can be useful during 
    #
    MyPolicy.allow(SomeGCPService, "Good reason here")

    # Usually this statement is added just before
    # invoking the Deployer
    #
    Policer.police()
```

# Post-Deployment Policing

It is possible to evaluate policies after the deployment too. The policies marked `REQUIRES_SERVICE_SPEC` are intended for this purpose and are skipped when the `spec` is not available on a service instance.

## Project Level Policing

`pygcloud` offers partial deployments through the use of `ServiceGroup`. When a deployment task does not include all the services, this means that the Policer will not have (by default) access to all the specifications of the services currently deployed in the target project.

**TODO** expand on this topic and provide example(s)

# Additional Considerations

* Consider the capability to decouple policing from deployment in order to uphold `separation of concerns` governance. A way to support this is to decouple infrastructure code & deployment in a separate project from application code.

* Consider policing "as-is" services in a project
