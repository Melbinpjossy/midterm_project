import matplotlib.pyplot as plt; plt.rcdefaults()
import numpy as np
import matplotlib.pyplot as plt
 
objects = ('Komoka', 'Oxbow', "Dingman")
y_pos = np.arange(len(objects))
performance = [52, 40, 42]
 
plt.bar(y_pos, performance, align='center', alpha=0.5, width=0.5, color=['red', 'black', 'cyan'])
plt.xticks(y_pos, objects)
plt.ylabel('Number of Fish Caught')
plt.title('TRAA data-Comparison of fish caught in each creek from 2016 to 2018')
 
plt.show()

slices_hours = [33, 47]
activities = ['2016', '2017']
colors = ['grey', 'orange']
plt.pie(slices_hours, labels=activities, colors=colors, startangle=90, autopct='%.1f%%')
plt.title('Fishes Caught in 2016 vs 2017 ')
plt.show()
