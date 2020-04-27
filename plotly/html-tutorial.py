# html-tutorial.py

'''
Following tutorial at 

https://t.co/rSxex593JM?amp=1
'''

import pandas as pd

def clean_data(df):
    '''
    Cleans the dataframe

    Parameters
    ----------
    df: pandas dataframe

    Returns
    -------
    df: dataframe
        Cleaned dataframe
    '''

    # Replace numbers with strings
    df.neighborhood = df.neighborhood.map(
        {
            1: 'Friedrichshain-Kreuzberg',
            2: 'Mitte',
            3: 'Pankow',
            4: 'Neukölln',
            5: 'Charlottenburg-Wilm',
            6: 'Tempelhof - Schöneberg',
            7: 'Lichtenberg',
            8: 'Treptow - Köpenick',
            9: 'Steglitz - Zehlendorf',
            10: 'Reinickendorf',
            11: 'Marzahn - Hellersdorf',
            12: 'Spandau',
        }
    )

    df.room_type = df.room_type.map(
        {
            1: 'Entire home/apt',
            2: 'Private room',
            3: 'Shared room',
        }
    )

    yes_no_dict = {0: 'No', 1: 'Yes'}
    df.wifi = df.wifi.map(yes_no_dict)
    df.washer = df.washer.map(yes_no_dict)
    df.cable_tv = df.cable_tv.map(yes_no_dict)
    df.kitchen = df.kitchen.map(yes_no_dict)

    # Rename columns
    df.rename(
        columns={
            'neighborhood': 'Neighborhood',
            'room_type': 'Room Type',
            'accommodates': 'Accommodates',
            'bedrooms': 'Bedrooms',
            'number_of_reviews': 'Number of Reviews',
            'wifi': 'Wifi',
            'cable_tv': 'Cable TV',
            'washer': 'Washer',
            'kitchen': 'Kitchen',
            'price': 'Price (US Dollars)'
        },
        inplace=True
    )

    # Remove outliers
    df = df[df['Price (US Dollars)'] < 501]

    return df

if __name__ == '__main__':
    # Import csv
    df = pd.read_csv(
        (r'https://raw.githubusercontent.com/elizabethts/publish-plotly-website'
        r'/master/airbnb.csv')
    )

    # Clean data
    df = clean_data(df)
