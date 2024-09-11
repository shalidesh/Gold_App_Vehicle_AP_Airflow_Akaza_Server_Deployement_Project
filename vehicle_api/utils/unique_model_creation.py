import pandas as pd 
import os

uniques_file_path = {
        'HONDA': 'honda_unique_models.csv',
        'TOYOTA': 'toyota_unique_models.csv',
        'NISSAN': 'nissan_unique_models.csv',
        'SUZUKI': 'suzuki_unique_models.csv'
    }

mapped_file_paths = {
    'HONDA': ('cdb_honda_unique_models.csv', 'honda_unique_models.csv', 'honda_mapped.csv'),
    'TOYOTA': ('cdb_toyota_unique_models.csv', 'toyota_unique_models.csv', 'toyota_mapped.csv'),
    'NISSAN': ('cdb_nissan_unique_models.csv', 'nissan_unique_models.csv', 'nissan_mapped.csv'),
    'SUZUKI': ('cdb_suzuki_unique_models.csv', 'suzuki_unique_models.csv', 'suzuki_mapped.csv')
}

final_databse_file_path = {
        'HONDA': 'honda_database.csv',
        'TOYOTA': 'toyota_database.csv',
        'NISSAN': 'nissan_database.csv',
        'SUZUKI': 'suzuki_database.csv'
}

def unique_model_creation(df):
   
    make = str(df['make'][0])

    try:
        file_path = uniques_file_path[make]
    except KeyError:
        raise ValueError(f"Unsupported make: {make}")

    unique_model_path = os.path.join("databases", "model_uniques_list", file_path)

    unique_models = df['model'].unique()
    unique_models_df = pd.DataFrame(unique_models, columns=['model'])
    unique_models_df['model'] = unique_models_df['model'].str.upper()
    unique_models_df.to_csv(unique_model_path, index=False)


def model_mapping(df):
    make = str(df['make'][0])
    try:
        file_paths = mapped_file_paths[make]
    except KeyError:
        raise ValueError(f"Unsupported make: {make}")

    unique_model_path_cdb = os.path.join("databases", "cdb_uniques_models", file_paths[0])
    unique_model_path_df = os.path.join("databases", "model_uniques_list", file_paths[1])
    mapped_dataset_path = os.path.join("databases", "model_mapped_list", file_paths[2])

    try:
        unique_model_cdb = pd.read_csv(unique_model_path_cdb)
        unique_model_df = pd.read_csv(unique_model_path_df)
    except FileNotFoundError as e:
        raise FileNotFoundError(f"File not found: {e.filename}")

    for model in unique_model_df['model']:
        mask = unique_model_cdb['model'].str.contains(model, na=False) 
        unique_model_cdb.loc[mask, 'map_model_name'] = model

    mapping_without_null = unique_model_cdb.dropna()
    mapping_without_null.to_csv(mapped_dataset_path, index=False)


def upload_database(df):

    make = str(df['make'][0])

    try:
        file_path = final_databse_file_path[make]
    except KeyError:
        raise ValueError(f"Unsupported make: {make}")

    final_database_path = os.path.join("databases", "vehicle_databases", file_path)

    df = df[["vehicle_price", "make", "model", "year", "transmision", "engine_capacity", "fuel_type"]]
    df.to_csv(final_database_path, index=False)
    


def dataset_processing(df):
    try:
        df['vehicle_price'] = df['vehicle_price'].astype(float)

        df['make'] = df['make'].str.upper().astype(str)
        df['transmision'] = df['transmision'].str.upper().astype(str)
        df['model'] = df['model'].str.upper().astype(str)

        df['engine_capacity'] = df['engine_capacity'].fillna(0).astype(int)
        
        return df
    except Exception as e:
        raise ValueError(f"Unsupported data conversion: {e}")
    