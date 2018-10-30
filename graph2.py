import matplotlib.pyplot as plt 

#X-COORDINATES
x=[1,2,3,4,5]
#Y COORDINATES
y=[10,24,36,40,5]
#LABELS FOR BARS
p=['one','two','three','four','five']
#PLOTTING A BAR GRAPH
plt.bar(x,y, tick_label= p, width=0.8, color=['blue','green'])


#NAMING X AXIS
plt.xlabel("X AXIS")
#NAMING Y AXIS
plt.ylabel("Y AXIS")
#TITLE OF THE GRAPH
plt.title("BAR GRAPH:")
#COMMAND TO DISPLAY THE GRAPH
plt.show()
