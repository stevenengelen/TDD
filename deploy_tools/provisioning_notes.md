Provisioning a new site
=======================

## Required packages:

* nginx
* Python3
* Git
* pip
* virtualenv

e.g.,, on Ubuntu:

    sudo apt-get install nginx git python3 python3-pip
    sudo pip3 install virtualenv

## Nginx Virtual Host Config

* see nginx.template.conf
* replace SITENAME with, e.g., staging.my-domain.com

## Systemd start

* see gunicorn-systemd.template.conf
* replace SITENAME with, e.g., staging.my-domain.com

## Folder structure:
Assume we have a user account at /home/username

/home/username
|__sites
   |__SITENAME
      |__database
      |__source
      |__static
      |__virtualenv
