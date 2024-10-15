 export AIRFLOW_HOME=.
 py -3.8 -m venv airflow_env


 References

 https://vivekjadhavr.medium.com/how-to-easily-install-apache-airflow-on-windows-6f041c9c80d2



 postgres sql commands
  docker exec -it <container_id> bash

  psql -U <username> 

  \l

  \c scarpe_data  #connect databse

  \q  # Exit the PostgreSQL prompt





https://ikman.lk/en/ads/sri-lanka/cars/nissan?sort=date&order=desc&buy_now=0&urgent=0&page=6&tree.brand=nissan&enum.transmission=automatic&enum.fuel_type=petrol





## App Permissions
## airflow webserver
inside the scheduler service
docker exec -u root -it <container_name> /bin/bash
chmod -R 775 /opt/airflow/artifacts/gold
chmod -R 775 /opt/airflow/artifacts/vehicle
change the host name to service name 'host = "postgres"'


## postgress sql
inside the psql service

CREATE DATABASE pipeline_data;


docker exec -u root -it <container_name> /bin/bash
chmod  777 /var/lib/postgresql/gold
chmod  777 /var/lib/postgresql/vehicle

