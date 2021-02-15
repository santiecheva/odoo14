#!/bin/sh
cd /home/ubuntu
git init
git pull origin main
sudo cp -r /home/ubuntu/odoo14/rut_res_partner /odoo/custom/addons/
sudo service odoo-server restart

