import pandas as pd

def process_data(data):
    df = pd.DataFrame(data)
    df = df[['name', 'email']]  # Select only necessary columns
    return df.to_dict('records')
