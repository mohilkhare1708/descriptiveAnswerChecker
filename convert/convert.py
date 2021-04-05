import pandas as pd

def file_to_csv(file):
    df = pd.read_csv(file)
    df.drop([''], [''], axis=1, inplace=true)
    for i in range(len(df)):
        return zip(df['Roll Number'], df['Name'])
        
    