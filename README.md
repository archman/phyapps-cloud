# phyapps-cloud

Cloud computing platform for software development for physics applications
on accelerators.

## Overview

* After logging onto this platform, each user can create/update their own
Jupyter-Notebook service with physics applications development environment
included, w/ or w/o virtual accelerator running or not.

* Each user has the private space to work with, e.g., the virtual
accelerator which the user is manipulating will not affect other users.

* Each user has the flexibility to adjust their own service settings, e.g.,
start virtual accelerator with different LINAC sections.

* The Jupyter-Notebook can only be accessed by the user who created.

* Within Jupyter-Notebook, user can do anything based on the provisioned
Python packages.

* The extensibility to support more services, currently, only supports VA with FRIB LINAC configurations.

* Available services:
  + `phyapps-va`
  + `phyapps-nb`

## Prerequisites

* Install [Docker](https://docs.docker.com/install/) & Pull Docker images:

    `docker pull tonyzhang/phyapps:<tagname>`

  where, `<tagname>` could be `nb`, `va`.

* Initialize [Swarm](https://docs.docker.com/engine/swarm/) environment for deployment: `docker swarm init` .

* Database configuration:

## Deployment

1. Clone this repository: ``git clone https://github.com/archman/phyapps-cloud.git``, locate [Makefile](https://github.com/archman/phyapps-cloud/blob/master/Makefile).

2. Set environmental variables in terminal or change in-place:
    * `SRV_IP`: IP address of the workstation as the swarm server
    * `TOKEN`: secret string for authentication
    * `MYSQL_ROOT_PASSWORD`: root password for MySQL service
    * `DATABASE_NAME`: database name for phyapps-gateway service
    * `DATABASE_USER`: database user account
    * `DATABASE_PASS`: `DATABASE_USER`'s password

3. Type `make deploy` to deploy.

4. Type `make stop` to stop.

5. The URL should be `https://<SRV_IP>:8000`

Here is an example to deploy the `phyapps_cloud` stack on the workstation with serving IP of `10.20.30.40`, with default configurations of MySQL service.
```shell
SRV_IP=10.20.30.40 TOKEN=6eec0c438f2e59711a1838d1207e1c make deploy
```
It is recommended to redirect the output to a file, e.g.
`make deploy 2>&1 | tee log`

## Screenshots

<img src="/screenshots/01_index.png?raw=true" alt="Home Page" title="Home Page" width="400"/><img src="/screenshots/02_login.png?raw=true" alt="Login Page" title="Login Page" width="400"/>
---
<img src="/screenshots/03_users.png?raw=true" alt="Users Activities" title="Users Activities" width="400"/><img src="/screenshots/04_service_admin.png?raw=true" alt="Service Control" title="Service Control" width="400"/>
---
<img src="/screenshots/05_service_new.png?raw=true" alt="Create New Service" title="Create New Service" width="400"/><img src="/screenshots/06_notebook.png?raw=true" alt="Jupyter Notebook" title="Jupyter Notebook" width="400"/>
---
