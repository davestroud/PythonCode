import pandas as pd
import numpy as np
df = pd.read_csv('heart_disease.csv')

df.head()

print(df.info())

print(df['age'])

print(df.chest_pain.min(), df.chest_pain.max(), df.chest_pain.mean())

# lets get rid of the 'site variable'
if 'site' in df:
    del df['site']

print(df.info())

df = df.replace(to_replace='?', value=-1)

# let's start by first changing the numeric values to be floats
continuous_features = ['rest_blood_press', 'cholesterol',
                       'max_heart_rate', 'ST_depression']

# and the oridnal values to be integers
ordinal_features = ['age', 'major_vessels', 'chest_pain',
                    'rest_ecg', 'Peak_ST_seg', 'thal', 'has_heart_disease']

# we won't touch these variables, keep them as categorical
categ_features = ['is_male', 'high_blood_sugar', 'exer_angina']


# use the 'astype' function to change the variable type
df[continuous_features] = df[continuous_features].astype(np.float64)
df[ordinal_features] = df[ordinal_features].astype(np.int64)

df.info()  # now our data looks better!

df.head()

df.describe()
