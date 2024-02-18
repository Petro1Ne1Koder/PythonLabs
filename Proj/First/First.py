import pandas as pd

my_list = [
    {"Name": "Danil", "Age": 19, "City": "Sotira"},
    {"Name": "Sasha", "Age": 20, "City": "Poltava"},
    {"Name": "Vlad", "Age": 22, "City": "Kyiv"}
]

df = pd.DataFrame(my_list)

print(df)

dataf = pd.DataFrame({
    "Name": ["Danil", "Sasha", "Vlad"],
    "Age": [19, 20, 22],
    "City": ["Sotira", "Poltava", "Kyiv"]
})

my_list = dataf.to_dict(orient='records')

print(my_list)