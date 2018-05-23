import pandas as pd
import numpy as np
import os

movies = sorted(os.listdir("training_set"))
chosen_movies = movies[:10000]

print("Creating DataFrame")
nuser = 2649429
data = pd.DataFrame(index = range(nuser), columns = range(1))

for i in range(len(chosen_movies)):
    col_name = f"{i+1}"

    data[col_name] = pd.Series(np.zeros(nuser), index = data.index)

    df = pd.read_csv('training_set/'+chosen_movies[i], header = None, skiprows = 1)

    for (j,rate) in zip(df[0],df[1]):
        data[col_name][j] = rate

    print("Processing of ",col_name," is complete")

data.to_csv("netflix_clean_data.csv")
