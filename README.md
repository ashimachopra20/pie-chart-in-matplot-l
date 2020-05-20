# pie-chart-in-matplot-l
#supervised machine learning
import matplotlib.pyplot as plt
Discipline=['Civil Engineering','Electrical Engineering','Mechanical Engineering','Chemical Engineering']
GraduateCount=[15000, 50000, 45000, 10000]
Branchcolors=['b', 'm', 'y','c']
BranchExplode=[0.1,0,0,0]
plt.pie(GraduateCount, labels=Discipline, explode=BranchExplode, colors=Branchcolors, autopct='%1.2f%%', shadow=True, startangle=90)
plt.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
plt.title("US Student Distribution")
plt.show()


import pandas as pd
df = pd.read_excel("C:/Users/Ashima/Desktop/Salaries.xlsx")
df1=df['sex'].value_counts().tolist()
print(df1)
z=list(df.columns)



import matplotlib.pyplot as plt


bcolors=['b', 'm']
aExplode=[0,0]
x=['Male','Female']
plt.pie(df1, labels=x, explode=aExplode, colors=bcolors, autopct='%1.2f%%', shadow=True, startangle=90)
plt.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
plt.title("Sex ratio of the Staff ")
plt.show()

df2=df['rank'].value_counts().tolist()
print(df2)

colorss=['y', 'c','r']
Explodee=[0,0,0]
y=['Prof','AsstProf','AssocProf']
plt.pie(df2, labels=y, explode=Explodee, colors=colorss, autopct='%1.2f%%', shadow=True, startangle=90)
plt.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
plt.title("Rank distribution ")
plt.show()
