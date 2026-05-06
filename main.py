import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df=pd.read_csv('student_raw_dataset.csv')

#remove duplicates rows
df=df.drop_duplicates()

#check Null values

print(df.isnull().sum())

#fill null values with mean
df["Science"].fillna(df['Science'].mean().round(),inplace=True)

df['English'].fillna(df['English'].mean().round(),inplace=True)

df['Attendance(%)'].fillna(df['Attendance(%)'].mean().round(),inplace=True)

#outliers remove
df["Maths"] = df["Maths"].apply(lambda x: np.nan if x < 0 or x > 100 else x)

df["Maths"].fillna(df["Maths"].mean().round(), inplace=True)

#Average Column
df['Average']=(df['Maths']+df['Science']+df['English'])/3
df['Average']=df['Average'].round()

#Grade Column

def grade(x):
    if x>=90:
        return 'A'
    elif x>=75:
        return 'B'
    elif x>=50:
        return 'C'
    else:
        return 'F'  
    
df['Grade']=df['Average'].apply(grade)

#Save the cleaned dataset
df.to_csv('student_cleaned_dataset.csv', index=False)

#Graphical representation

#Gender vs Average
gender_avg=df.groupby('Gender')['Average'].mean()
gender_avg.plot(kind='bar')
plt.title("Gender vs Average Marks")
plt.xlabel("Gender")
plt.ylabel("Average Marks")
plt.show()

#Subject Average
subject_avg=df[['Maths','Science','English']].mean()
subject_avg.plot(kind='bar')
plt.title("Average Marks per Subject")
plt.xlabel("Subject")
plt.ylabel("Average Marks")
plt.show()

#Scatter
df.plot.scatter(x='Attendance(%)', y='Average')
plt.title("Attendance vs Average Marks")
plt.xlabel("Attendance(%)")
plt.ylabel("Average Marks")
plt.show()


