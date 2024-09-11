# import pandas as pd
import os
import pandas as pd

#main databases
honda_database = pd.read_csv(os.path.join("databases","vehicle_databases","honda_database.csv"))
nissan__database = pd.read_csv(os.path.join("databases","vehicle_databases","nissan_database.csv"))
suzuki__database = pd.read_csv(os.path.join("databases","vehicle_databases","suzuki_database.csv"))
toyota__database = pd.read_csv(os.path.join("databases","vehicle_databases","toyota_database.csv"))
micro__database = pd.read_csv(os.path.join("databases","vehicle_databases","micro_database.csv"))
mitsubishi__database = pd.read_csv(os.path.join("databases","vehicle_databases","mitsubishi_database.csv"))

#mapping dataset
honda_mapp = pd.read_csv(os.path.join("databases","model_mapped_list","honda_mapped.csv"))
nissan_mapp = pd.read_csv(os.path.join("databases","model_mapped_list","nissan_mapped.csv"))
suzuki_mapp = pd.read_csv(os.path.join("databases","model_mapped_list","suzuki_mapped.csv"))
toyota_mapp = pd.read_csv(os.path.join("databases","model_mapped_list","toyota_mapped.csv"))
micro_mapp = pd.read_csv(os.path.join("databases","model_mapped_list","micro_mapped.csv"))
mitsubishi_mapp = pd.read_csv(os.path.join("databases","model_mapped_list","mitsubishi_mapped.csv"))

honda_name_mapping = honda_mapp.set_index('model')['map_model_name'].to_dict()
nisaan_name_mapping = nissan_mapp.set_index('model')['map_model_name'].to_dict()
suzuki_name_mapping = suzuki_mapp.set_index('model')['map_model_name'].to_dict()
toyota_name_mapping = toyota_mapp.set_index('model')['map_model_name'].to_dict()
micro_name_mapping = micro_mapp.set_index('model')['map_model_name'].to_dict()
mitsubishi_name_mapping = mitsubishi_mapp.set_index('model')['map_model_name'].to_dict()
