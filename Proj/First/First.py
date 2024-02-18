import pandas as pd

my_list = [
    {"Name": "Danil", "Age": 19, "City": "Sotira"},
    {"Name": "Sasha", "Age": 20, "City": "Poltava"},
    {"Name": "Vlad", "Age": 22, "City": "Kyiv"}
]

df = pd.DataFrame(my_list)
my_list = df.to_dict(orient='records')

print(df)
print(my_list)