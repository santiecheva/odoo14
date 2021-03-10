#!/bin/sh
cd /home/ubuntu/odoo14
git init
git pull origin main
sudo cp -r /home/ubuntu/odoo14/web_gantt_project_task_app /odoo/custom/addons/
sudo service odoo-server restart

