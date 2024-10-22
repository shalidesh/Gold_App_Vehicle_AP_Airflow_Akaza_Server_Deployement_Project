
 ## References
 https://vivekjadhavr.medium.com/how-to-easily-install-apache-airflow-on-windows-6f041c9c80d2


# setup instructions

## 1.0 run docker compose file 

```bash

 docker-compose up -d

 ```

## 2.0 give Container Permissions

### 2.1 airflow webserver

```bash
docker exec -u root -it <container_name> /bin/bash
chmod -R 775 /opt/airflow/artifacts/gold
chmod -R 775 /opt/airflow/artifacts/vehicle

```
change the host name to service name


```bash

 'host = "postgres"

 ```

### 2.2 postgress sql

```bash

CREATE DATABASE pipeline_data;

docker exec -u root -it <container_name> /bin/bash
chmod  777 /var/lib/postgresql/gold
chmod 777 /var/lib/postgresql/vehicle/ikman_vehicle_post_links.csv
chmod 777 /var/lib/postgresql/vehicle/ikman_post_data.csv
chmod 777 /var/lib/postgresql/vehicle/unique_model.csv
chmod 777 /var/lib/postgresql/vehicle/ikman_post_data_preprocced.csv

```



# Testing Steps

- gold model training pipeline ✅
- gold news scrape pipeline ✅
- vehicle data scrape pipeline ✅
- vehicle model training pipeline ✅

- intergrate MLflow for monitoring ❌
