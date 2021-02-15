#!/bin/sh
cd /home/ubuntu/miodoo
git init
git pull origin master
sudo cp -r /home/ubuntu/odoo14/rut_res_partner /odoo/custom/addons/
sudo service odoo-server restart

