import pandas as pd
import seaborn as sns #for graphical representation of the data we got it from pandas
import matplotlib.pyplot as plt #to represent the data into map form

df = pd.read_csv(r"D:\Programing\DataScience\DataCleaning\Personality_Analysis\personality_dataset.csv")
print(df.head(3))
print(df.shape)
print(df.isnull().sum())# null values
print("total null values\n",df.isnull().sum().sum())#total null valaue present inside a data set
print("total percentage of null value present:\n",(df.isnull().sum().sum()/(df.shape[0]*df.shape[1]))*100,"\n")#to find the total no of null
print((df.isnull().sum()/df.shape[0])*100) #percentage of null value
print(df.notnull().sum())#vqlues that are not null
print("total value of not nulls is \n",df.notnull().sum().sum(),"\n")#total value of not null

#data visualization using seaborn

sns.heatmap(df.isnull())
plt.show()