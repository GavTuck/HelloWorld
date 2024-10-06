import numpy as np
import pandas as pd
df = pd.read_csv("speeddating.csv")


# b = df.sort_values("b'0").head(10)

# b = df.columns
b = df.describe(include=["object", "float64"])
c = df["decision"].value_counts()
d = df["samerace"].value_counts()
df_race_check = df
# df = pd.read_csv("train.csv", usecols= ["PassengerId", "Survived", "Pclass"]) 

df_race_check = (df["samerace"] == "b'1'")
df_like_check = (df["decision"] == "b'1'")
df_check = (df_race_check & df_like_check).value_counts()
df_check = (df_race_check & df_like_check).sum()
e = df_race_check
g = df_check

h = df['race'].value_counts()
objecttypes = 'Asian/Pacific Islander/Asian-American', 'European/Caucasian-American', 'Latino/Hispanic American', 'Black/African American', '?'

asian = (df['race'] == "b'Asian/Pacific Islander/Asian-American'")
euro = (df['race'] == "b'European/Caucasian-American'")
latin = (df['race'] == "b'Latino/Hispanic American'")
black = (df['race'] == "b'Black/African American'")
idk = (df['race'] == "b'?'")
other = (df['race'] == "b'Other'")

# df_check2 = (df_race_check & df_like_check & asian).sum()

for i in objecttypes:
    df_check2 = (df_race_check & df_like_check & (df['race'] == f"b'{i}'")).sum()
    df_check3 = (df_check2 / (df['race'] == f"b'{i}'").sum()) * 100
    

z = df['decision'].value_counts()
y = df['decision_o'].value_counts()

 df['like'].describe()



print(y)
print(z)
print(w)
# test_df_check1 = (df['race'] == "b'European/Caucasian-American'").sum()
# test_df_check2 = (df_race_check & df_like_check & (df['race'] == f"b'European/Caucasian-American'")).sum()
# test_df_check3 = (test_df_check2 / (df['race'] == "b'European/Caucasian-American'").sum()) * 100
# print(test_df_check1)
# print(test_df_check2)
# print(test_df_check3)


# thing = df.sort_values("Fare").head(10)
# a = df["Embarked"] == "C" 

# decision
# decision_o


