import pandas as pd
import codecademylib3

data = {'PassengerId': ['Id number'],
'Survived': ['Survival (1=Yes, 2=No)'],
'Pclass': ['Ticket class'],
'Name': ['Name of passenger'],
'Sex': ['Sex'],
'Age': ['Age in years'],
'SibSp': ['# of siblings / spouses aboard the Titanic'],
'Parch': ['# of parents / children aboard the Titanic | Ticket number'],
'Ticket': ['Ticket number'],
'Fare': ['Passenger fare'],
'Cabin': ['Cabin number'],
'Embarked': ['Port of Embarkation']
        }

df = pd.DataFrame(data)

print(df)