import pandas as pd;
df=pd.read_csv("test.csv");
print(df);
data={"Name": ["abhi", "Astitva", "Aradhya"],
      "rollno":[1,2,3],
      "Age":[12,18,20]
      }
df1=data;
print(df1);
df1=pd.DataFrame(df);