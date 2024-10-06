import numpy as np
import pandas as pd
df = pd.read_csv("speeddating.csv")

# Question 1
"""  On average are people more atracted or repulsed to others?"""

# attraction = df['like'].describe()
# print(attraction)

#Question 2
""" Who is more likely to like the other first, the guy or the girl?"""

# guy_girl = df['decision'].value_counts()
# print(guy_girl)

# Question 3
""" Which race is most likely to date exclusively?"""

racetypes = 'Asian/Pacific Islander/Asian-American', 'European/Caucasian-American', 'Latino/Hispanic American', 'Black/African American'
df_race = (df["samerace"] == "b'1'")
df_like = (df["decision"] == "b'1'")


for i in racetypes:
    sum_mutual_exclusive = (df_race & df_like & (df['race'] == f"b'{i}'")).sum()
    total_race = (df['race'] == f"b'{i}'").sum()
    percentage = (sum_mutual_exclusive / total_race ) * 100
    
    print("{}: {}%".format(i, percentage))