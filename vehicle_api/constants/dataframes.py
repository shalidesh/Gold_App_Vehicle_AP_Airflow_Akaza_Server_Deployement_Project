# import pandas as pd
import os
import pandas as pd

#main databases
honda_database = pd.read_csv(os.path.join("databases","dynamic_db","airflow_scrape_databases","HONDA_train_data.csv"))
nissan__database = pd.read_csv(os.path.join("databases","dynamic_db","airflow_scrape_databases","NISSAN_train_data.csv"))
suzuki__database = pd.read_csv(os.path.join("databases","dynamic_db","airflow_scrape_databases","SUZUKI_train_data.csv"))
toyota__database = pd.read_csv(os.path.join("databases","dynamic_db","airflow_scrape_databases","TOYOTA_train_data.csv"))
micro__database = pd.read_csv(os.path.join("databases","dynamic_db","airflow_scrape_databases","MICRO_train_data.csv"))
mitsubishi__database = pd.read_csv(os.path.join("databases","dynamic_db","airflow_scrape_databases","MITSUBISHI_train_data.csv"))

#mapping dataset
honda_mapp = pd.read_csv(os.path.join("databases","static_db","model_mapped_list","honda_mapped.csv"))
nissan_mapp = pd.read_csv(os.path.join("databases","static_db","model_mapped_list","nissan_mapped.csv"))
suzuki_mapp = pd.read_csv(os.path.join("databases","static_db","model_mapped_list","suzuki_mapped.csv"))
toyota_mapp = pd.read_csv(os.path.join("databases","static_db","model_mapped_list","toyota_mapped.csv"))
micro_mapp = pd.read_csv(os.path.join("databases","static_db","model_mapped_list","micro_mapped.csv"))
mitsubishi_mapp = pd.read_csv(os.path.join("databases","static_db","model_mapped_list","mitsubishi_mapped.csv"))

honda_name_mapping = honda_mapp.set_index('model')['map_model_name'].to_dict()
nisaan_name_mapping = nissan_mapp.set_index('model')['map_model_name'].to_dict()
suzuki_name_mapping = suzuki_mapp.set_index('model')['map_model_name'].to_dict()
toyota_name_mapping = toyota_mapp.set_index('model')['map_model_name'].to_dict()
micro_name_mapping = micro_mapp.set_index('model')['map_model_name'].to_dict()
mitsubishi_name_mapping = mitsubishi_mapp.set_index('model')['map_model_name'].to_dict()
