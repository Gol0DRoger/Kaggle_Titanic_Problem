import pandas as pd

tr = pd.read_csv("train.csv")
pd.options.display.max_rows= 100
pd.options.display.max_columns = 20
#print(tr.to_string())
print(tr.info())
tn = pd.read_csv("test.csv")
print(tn.info())
#tr.drop('Cabin',axis = 1,inplace = True)
tn.drop('Cabin',axis = 1,inplace = True)
m = tn["Age"].mean()
print(m)
tn["Age"].fillna(m,inplace=True)
tn.drop('Name',axis = 1,inplace = True)
tn.drop('Ticket',axis = 1,inplace = True)
tn.drop('Embarked',axis = 1,inplace = True)
tn['Sex'] = tr['Sex'].map({'male': 0, 'female': 1})
print(tn.info())
#print(tr.corr())
print(tn.corr())
tn.assign(Survived=0)
#Females have more survival chance than males according to correlation.
for x in tn.index:
    if tn.loc[x,"Sex"] == 1:
    #Females are more physically healthy till the age of 55.
        if tn.loc[x,"Age"]>=14 and tn.loc[x,"Age"] < 55:
            tn.loc[x,"Survived"]= 1
        else: tn.loc[x,"Survived"]= 0
    else: 
    #Rich/Superior male has more chanches of getting help than poor male of 3rd Pclass.  
         if tn.loc[x,"Pclass"] == 1:
             tn.loc[x,"Survived"]= 1
         else: tn.loc[x,"Survived"]= 0 
print(tn)