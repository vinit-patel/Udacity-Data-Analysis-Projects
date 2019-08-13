import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

#Load Houston tempereture data into hou_temp
hou_temp=pd.read_csv(r'C:\Vinit\Udacity\Project 1-Weather\houston_temp.csv')
hou_temp['mov_avg_temp']=hou_temp['avg_temp'].rolling(30).mean()

#Load Global tempereture data into global_temp
global_temp=pd.read_csv(r'C:\Vinit\Udacity\Project 1-Weather\global_temp.csv')
global_temp['mov_avg_temp']=global_temp['avg_temp'].rolling(30).mean()

#Plotting the global moving average temperature
fig=plt.figure(figsize=(7,4))
ax0=fig.add_axes([0.1,0.3,0.8,0.6])
#sns.set_style('whitegrid')
ax0.plot('year','mov_avg_temp',color='g',data=global_temp,label="Global Moving Avg Temp")
ax0.set_ylabel('Global Temperature in ºC',color='g')
ax0.tick_params('y',colors='g')
#ax0.set_xbound(1990,2015)

#Plotting Houston's moving average temperature
ax1=ax0.twinx()
ax1.plot('year','mov_avg_temp',color='b',data=hou_temp,label="Houston's Moving Avg Temp")
ax1.set_xlabel('Year')
ax1.set_ylabel('Houstan TX, US Temperature in ºC',color='b')
ax1.tick_params('y',colors='b')
ax1.set_title('Houston, TX USA vs Global Temperature Trend')
#ax1.set_xbound(1990,2015)

#setting up legends
#ax0.legend(loc='best',bbox_to_anchor=(0.22,0.98))
#ax1.legend(loc='best',bbox_to_anchor=(0.239,0.91))
ax0.legend(loc='best',bbox_to_anchor=(0.5,-0.05))
ax1.legend(loc='best',bbox_to_anchor=(0.8,-0.05))

plt.show()
fig.savefig(r'C:\Vinit\Udacity\Project 1-Weather\Hou_vs_Glob.png',orientation='landscape')
