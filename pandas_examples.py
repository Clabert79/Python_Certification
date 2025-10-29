import pandas as pd

titanic = pd.read_csv('https://vincentarelbundock.github.io/' + 
                      'Rdatasets/csv/carData/TitanicSurvival.csv') 

titanic.columns = ['name', 'survived', 'sex', 'age', 'class'] # Renaming columns

print(titanic.describe())
print(titanic.head())
print(titanic.tail())