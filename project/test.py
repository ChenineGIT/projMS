import pandas
file = "out/testEtude2.json"
pandas.read_json(file).to_excel("table_finale.xlsx")
