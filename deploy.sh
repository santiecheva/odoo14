#!/bin/sh
cd /home/ubuntu/odoo14
git pull origin main
sudo cp -r /home/ubuntu/odoo14/crm_cumplimiento /odoo/custom/addons/
sudo cp -r /home/ubuntu/odoo14/rut_res_partner /odoo/custom/addons/
sudo cp -r /home/ubuntu/odoo14/padrino /odoo/custom/addons/


sudo service odoo-server restart


