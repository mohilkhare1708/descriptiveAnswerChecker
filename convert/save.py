import os
import pandas as pd
import string
import random

def save_file(df):
    N = 7
    token = ''.join(random.choices(string.ascii_uppercase + string.digits, k=N))
    df.to_csv('token.csv')

