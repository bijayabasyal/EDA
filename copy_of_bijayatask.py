# -*- coding: utf-8 -*-
"""Copy of bijayatask.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1R7BbZhTjODgV-UIYC_lIeNVw-iixRL81
"""

# Commented out IPython magic to ensure Python compatibility.
#importing numpy pandas mathplotand other methods
import pandas as pd # data manipulation
import numpy as np # math calculation/ numbers
import matplotlib.pyplot as plt #GRAPH
# %matplotlib inline
import seaborn as sns   #graphing

from google.colab import drive
drive.mount('/content/drive')

df = pd.read_csv('/content/drive/MyDrive/Student_performance_data _.csv')
df.head()

df.shape

df.info()

df.describe()

df.columns

df.isnull().sum()

"""no missing value"""

# seaborn histogram
sns.distplot(df['Age'], hist=True, kde=False,
             bins=10, color = 'blue',
             hist_kws={'edgecolor':'black'})
# Add labels
plt.title('Age count')
plt.xlabel('Age')

plt.ylabel('Count')

import seaborn as sns   #graphing
import matplotlib.pyplot as plt

plt.scatter(x= df['Age'], y =  df['Absences'])

plt.xlabel('Age')
plt.ylabel('Absences')
plt.show()

plt.scatter(x= df['ParentalSupport'], y =  df['GPA'])

plt.xlabel('ParentalSupport')
plt.ylabel('GPA')
plt.show()

"""The above figure shows scatter plot between parentalsupport and gpa."""

plt.scatter(x= df['Absences'], y =  df['GPA'])

plt.xlabel('Absences')
plt.ylabel('GPA')
plt.show()

"""Here appears to be a weak positive correlation between absences and GPA. This means that as the number of absences increases, the GPA also tends to increase, but not necessarily in a linear way.

"""

sns.lineplot(x='ParentalSupport',y='GradeClass', data=df )

"""There is a clear negative correlation between ParentalSupport and GradeClass. This means that higher levels of parental support are associated with lower average grades or class performance.

"""

sns.lineplot(x='Age',y='Absences', data=df )

"""Increasing Trend: From age 15 to 16, the number of absences increases. This could indicate that students around age 16 tend to have more absences.
Decreasing Trend: After age 16, the number of absences decreases slightly and then levels off as age increases to 18. This suggests that older students (ages 17 and 18) have fewer absences compared to those around age 16.


"""

corrmat = df.corr()
f, ax = plt.subplots(figsize=(16, 12))
sns.heatmap(corrmat, vmax=.8, square=True);

plt.figure(figsize=(20,20))
plt.title('Pearson Correlation of Features', size = 15)
colormap = sns.diverging_palette(10, 220, as_cmap = True)
sns.heatmap(df.corr(),
            cmap = colormap,
            square = True,
            annot = True,
            linewidths=0.1,vmax=1.0, linecolor='white',
            annot_kws={'fontsize':12 })
plt.show()