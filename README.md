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
