# phyapps-cloud

Cloud platform for physics applications development.

## Overview

* After loging onto this platform, each user can create/update their own
Jupyter-Notebook service with physics applications development environment
included.

* Each user has the private space to work with, e.g., the virtual
accelerator which the user is manipulating will not affect other users'.

* Each user has the flexibility to adjust their own service settings, e.g.,
start virtual accelerator with different LINAC sections, or start with
different versions.

* The Jupyter-Notebook can only be accessed by the owner.

* Within Jupyter-Notebook, user can do anything based on the provisoned
Python packages.

* The extensibility to support more serivces.

## Prerequisites

* Install Docker & Pull Docker images:
  tagname: `release-1.7-ss`, `release-1.7`, `release-1.6-ss`, `release-1.6`

    docker pull tonyzhang/phyapps:tagname

* Database configuration: see [this file](https://github.com/archman/phyapps-cloud/blob/master/phycloud/mysql.md).

## Deployment

1. Download the [Makefile](https://github.com/archman/phyapps-cloud/blob/master/Makefile) of this repo.
2. Change `ETH0` to be the name of your network interface.
2. Type `make deploy` to deploy.
3. Type `make stop` to stop.
4. The URL should be `https://<your-ip-address>:8000`

## Screenshots

<img src="/screenshots/01_index.png?raw=true" alt="Home Page" title="Home Page" width="400"/><img src="/screenshots/02_login.png?raw=true" alt="Login Page" title="Login Page" width="400"/>
---
<img src="/screenshots/03_users.png?raw=true" alt="Users Activities" title="Users Activities" width="400"/><img src="/screenshots/04_service_admin.png?raw=true" alt="Service Control" title="Service Control" width="400"/>
---
<img src="/screenshots/05_service_new.png?raw=true" alt="Create New Service" title="Create New Service" width="400"/><img src="/screenshots/06_notebook.png?raw=true" alt="Jupyter Notebook" title="Jupyter Notebook" width="400"/>
---
