import os

news_df_path = os.path.join("airflow_scrape_database", "gold_post_data.csv")
train_df_path = os.path.join("data_tables", "gold_train_data.csv")
gold_df_path = os.path.join("data_tables", "gold_databases.csv")


model_dir = os.path.join("artifacts")
dataset_dir = os.path.join("uploads", "df_interpolated_2024_10_21.csv")

