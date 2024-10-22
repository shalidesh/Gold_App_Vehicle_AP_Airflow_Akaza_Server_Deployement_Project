#!/bin/bash
# Change permissions as root
chmod 777 /var/lib/postgresql/gold
chmod 777 /var/lib/postgresql/vehicle/ikman_vehicle_post_links.csv
chmod 777 /var/lib/postgresql/vehicle/ikman_post_data.csv
chmod 777 /var/lib/postgresql/vehicle/unique_model.csv
chmod 777 /var/lib/postgresql/vehicle/ikman_post_data_preprocced.csv

# Switch to the postgres user and start the PostgreSQL server
exec gosu postgres postgres
