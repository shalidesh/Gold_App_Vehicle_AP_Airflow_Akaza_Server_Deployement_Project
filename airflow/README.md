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


 CREATE DATABASE scarpe_data;
 SELECT * FROM auto_finance LIMIT 10;

DROP TABLE auto_finance_honda;
DROP TABLE auto_finance_nissan;
DROP TABLE auto_finance_suzuki;
DROP TABLE auto_finance_toyota;
DROP TABLE honda_post_data;
DROP TABLE honda_preprocessed_data;
DROP TABLE nissan_post_data;
DROP TABLE nissan_preprocessed_data;
DROP TABLE suzuki_post_data;
DROP TABLE suzuki_preprocessed_data;
DROP TABLE toyota_post_data;
DROP TABLE toyota_preprocessed_data;

DROP TABLE ikman_post_data; 

https://ikman.lk/en/ads/sri-lanka/cars/nissan?sort=date&order=desc&buy_now=0&urgent=0&page=6&tree.brand=nissan&enum.transmission=automatic&enum.fuel_type=petrol

