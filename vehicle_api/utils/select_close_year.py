import numpy as np
from utils.ai_price_calculation import calculate_ai_price
import logging

def round_nearest_50000(number):
    return round(number / 50000) * 50000

def select_year(grouped_df,year):
    print(grouped_df)
    print(year)
    
    if int(year) in grouped_df['year_of_manufacture'].values:
        logging.info('year found in dataset')
        print('year found in dataset')
        estimated_price=grouped_df[grouped_df['year_of_manufacture'] == int(year)]['vehicle_price'].mean()
        estimated_price=round(float(estimated_price),0)
        estimated_price=round_nearest_50000(estimated_price)
        return estimated_price 

    # If the year doesn't exist, find the two closest years
    logging.info('find the two closest years--')
    print('year not found in dataset')

    print(grouped_df['year_of_manufacture'] )
    
    below_year = grouped_df[grouped_df['year_of_manufacture'] < int(year)]['year_of_manufacture'].max()
    print(below_year)
    above_year = grouped_df[grouped_df['year_of_manufacture'] > int(year)]['year_of_manufacture'].min()
    print(above_year)

    if below_year is np.nan:
        logging.info('below closest year not found')
        year_count=(above_year-int(year))

        reduced_presentage=(2*year_count)/100

        above_year_price=grouped_df[grouped_df['year_of_manufacture'] == above_year]['vehicle_price'].mean()

        estimated_price=above_year_price-(above_year_price*reduced_presentage)

        estimated_price=round(float(estimated_price),0)

        estimated_price=round_nearest_50000(estimated_price)
        print(f"estimate price database - {estimated_price}")

        return estimated_price
    
    if above_year is np.nan:
        logging.info('above closest year not found')
        year_count=(int(year)-below_year)

        reduced_presentage=(2*year_count)/100

        below_year_price=grouped_df[grouped_df['year_of_manufacture'] == below_year]['vehicle_price'].mean()

        estimated_price=below_year_price+(below_year_price*reduced_presentage)

        estimated_price=round(float(estimated_price),0)

        estimated_price=round_nearest_50000(estimated_price)
        print(f"estimate price database - {estimated_price}")

        return estimated_price


    # Calculate the average prices for the closest years
    below_price = grouped_df[grouped_df['year_of_manufacture'] == below_year]['vehicle_price'].mean()
    above_price = grouped_df[grouped_df['year_of_manufacture'] == above_year]['vehicle_price'].mean()

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

def estimate_price(df,model_path,preprocessor_path, cdb_model, fuel, transmission, year,engine_capacity):

    list_models = df['model'].unique().tolist()

    if cdb_model in list_models:
        print("model found in database")
        grouped_df = df[(df['model'] == cdb_model) &
                        (df['transmission'] == transmission)]
        
        if grouped_df.empty:
            print("transmission not found in database")
            grouped_df = df[(df['model'] == cdb_model) &
                        (df['fuel_type'] == fuel)]
            
            if grouped_df.empty:
                print("transmission not found fuel_type not found in database")
                estimated_price=0
                return estimated_price
                # if fuel  in ['HYBRID', 'ELECTRIC']:
                #     logging.info('ai prediction process')
                #     estimated_price=calculate_ai_price(cdb_model,model_path,preprocessor_path, fuel, transmission, year,engine_capacity)
                #     return estimated_price
                # else:            
                #     estimated_price=0
                #     return estimated_price
            else:
                estimated_price=select_year(grouped_df,year)
                return estimated_price

        else:
            print("transmission  found in database")
        
            grouped_df = df[(df['model'] == cdb_model) &
                        (df['transmission'] == transmission) &
                        (df['fuel_type']==fuel)]
        
            if grouped_df.empty:
                print("transmission found fuel not in database")
                grouped_df = df[(df['model'] == cdb_model) &
                        (df['transmission'] == transmission)]
                
                # print(grouped_df)
                
                # grouped_df = df[(df['model'] == cdb_model) &
                #         (df['transmission'] == transmission) &
                #         (df['fuel_type'].isin(['PETROL', 'DIESEL']))]
                
                estimated_price=select_year(grouped_df,year)
                return estimated_price
    
                # if fuel  in ['HYBRID', 'ELECTRIC']:
                #     logging.info('ai prediction process')
                #     print("ai model called")
                #     estimated_price=calculate_ai_price(cdb_model,model_path,preprocessor_path, fuel, transmission, year,engine_capacity)
                #     return estimated_price


                # else:
                #     print("ai model not called")
                #     print(fuel)
                #     grouped_df = df[(df['model'] == cdb_model) &
                #             (df['transmission'] == transmission)]
                    
                #     print(grouped_df)
                    
                #     # grouped_df = df[(df['model'] == cdb_model) &
                #     #         (df['transmission'] == transmission) &
                #     #         (df['fuel_type'].isin(['PETROL', 'DIESEL']))]
                    
                #     estimated_price=select_year(grouped_df,year)
                #     return estimated_price
                    
            else:
                print("transmission  found fuel found in database")    
                estimated_price=select_year(grouped_df,year)
                return estimated_price
            
    else:
        estimated_price=0
        return estimated_price

            
