# OWASP ModSecurity CRS WAF for app development

## Overview

This repository has an example of how to run OWASP ModSecurity CRS WAF with
Nginx locally against a custom application running on the same machine.

### Why use this thing?

This is useful for testing an application to make sure that the payloads being
sent to the web application are secure, or that you're handling certain types of
security concerns appropriately.

### References

- [OWASP ModSecurity Core Rule Set](https://coreruleset.org/)
- [GitHub: coreruleset/modsecurity-crs-docker](https://github.com/coreruleset/modsecurity-crs-docker)
- [GitHub: coreruleset/modsecurity-docker](https://github.com/coreruleset/modsecurity-docker)

## Requirements

- [Podman](https://podman.io)
- [Docker](https://docker.com)
  - You'll also want Docker-Compose.
- [Taskfile](https://taskfile.dev) - This is a task runner.

Normally, you can only run either Docker or Podman on the same Linux instance.
If you're running in WSLv2, just spin up a new ditribution.

## Running this thing

### Podman

To run this with Podman, you'll need to have at least Podman v4, which as of
this writing is only available on Fedora. Ubuntu does not yet have Podman v4,
only v3.

Run the following `task` command:

```bash
task podman-play
```

This will create a local Pod using the Kubernetes Deployment manifest. There
will be a container image reference that doesn't exist, so Podman will attempt
to build that for you.

To turn off, or bring down the Pod, use the alternate `task` command:

```bash
task podman-down
```

These commands were made this way to denote whether or not you're using Podman
or Docker, and then to bring a common naming strategy to both.
