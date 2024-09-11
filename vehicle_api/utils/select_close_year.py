import numpy as np
from utils.ai_price_calculation import calculate_ai_price
import logging
import os

def round_nearest_50000(number):
    return round(number / 50000) * 50000

def select_year(grouped_df,year):
    
    if int(year) in grouped_df['year'].values:
        logging.info('year found in dataset')
        print('year found in dataset')
        estimated_price=grouped_df[grouped_df['year'] == int(year)]['vehicle_price'].mean()
        estimated_price=round(float(estimated_price),0)
        estimated_price=round_nearest_50000(estimated_price)
        return estimated_price 

    # If the year doesn't exist, find the two closest years
    logging.info('find the two closest years--')
    below_year = grouped_df[grouped_df['year'] < int(year)]['year'].max()
    above_year = grouped_df[grouped_df['year'] > int(year)]['year'].min()

    if below_year is np.nan:
        logging.info('below closest year not found')
        year_count=(above_year-int(year))

        reduced_presentage=(2*year_count)/100

        above_year_price=grouped_df[grouped_df['year'] == above_year]['vehicle_price'].mean()

        estimated_price=above_year_price-(above_year_price*reduced_presentage)

        estimated_price=round(float(estimated_price),0)

        estimated_price=round_nearest_50000(estimated_price)
        print(f"estimate price database - {estimated_price}")

        return estimated_price
    
    if above_year is np.nan:
        logging.info('above closest year not found')
        year_count=(int(year)-below_year)

        reduced_presentage=(2*year_count)/100

        below_year_price=grouped_df[grouped_df['year'] == below_year]['vehicle_price'].mean()

        estimated_price=below_year_price+(below_year_price*reduced_presentage)

        estimated_price=round(float(estimated_price),0)

        estimated_price=round_nearest_50000(estimated_price)
        print(f"estimate price database - {estimated_price}")

        return estimated_price


    # Calculate the average prices for the closest years
    below_price = grouped_df[grouped_df['year'] == below_year]['vehicle_price'].mean()
    above_price = grouped_df[grouped_df['year'] == above_year]['vehicle_price'].mean()

    # Calculate the price difference and the year count between the closest years
    price_diff = above_price - below_price
    year_count = above_year - below_year

    # Calculate the price increment per year
    price_increment_per_year = price_diff / year_count

    # Estimate the price for the input year
    estimated_price = below_price + price_increment_per_year * (int(year) - below_year)

    logging.info('Calculated the average prices for the 2 closest years')

    estimated_price=round(float(estimated_price),0)

    estimated_price=round_nearest_50000(estimated_price)
    

    return estimated_price

def estimate_price(df,model_path, cdb_model, fuel, transmission, year,engine_capacity):

    list_models = df['model'].unique().tolist()

    if cdb_model in list_models:
        grouped_df = df[(df['model'] == cdb_model) &
                        (df['transmision'] == transmission)]
        
        if grouped_df.empty:
            grouped_df = df[(df['model'] == cdb_model) &
                        (df['fuel_type'] == fuel)]
            
            if grouped_df.empty:
                if fuel  in ['HYBRID', 'ELECTRIC']:
                    logging.info('ai prediction process')
                    estimated_price=calculate_ai_price(cdb_model,model_path, fuel, transmission, year,engine_capacity)
                    return estimated_price
                else:
                    grouped_df = df[(df['model'] == cdb_model) &
                            (df['fuel_type'].isin(['PETROL', 'DIESEL']))]
                    
                    estimated_price=select_year(grouped_df,year)
                    return estimated_price
            else:
                estimated_price=select_year(grouped_df,year)
                return estimated_price

        else:
        
            grouped_df = df[(df['model'] == cdb_model) &
                        (df['transmision'] == transmission) &
                        (df['fuel_type']==fuel)]
        
            if grouped_df.empty:
    
                if fuel  in ['HYBRID', 'ELECTRIC']:
                    logging.info('ai prediction process')
                    print("ai model called")
                    estimated_price=calculate_ai_price(cdb_model,model_path, fuel, transmission, year,engine_capacity)
                    return estimated_price
                else:
                    grouped_df = df[(df['model'] == cdb_model) &
                            (df['transmision'] == transmission) &
                            (df['fuel_type'].isin(['PETROL', 'DIESEL']))]
                    
                    estimated_price=select_year(grouped_df,year)
                    return estimated_price
                    
            else:
                print("not empty")    
                estimated_price=select_year(grouped_df,year)
                return estimated_price
            
    else:
        estimated_price=0
        return estimated_price

            
