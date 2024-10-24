# To add a new cell, type '#%%'
# To add a new markdown cell, type '#%%[markdown]'

#%%
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns #optional
import scipy.stats as stats
from statsmodels.stats.multicomp import pairwise_tukeyhsd

world1 = pd.read_csv("world1.csv", index_col="id") #reading world1 csv
world2 = pd.read_csv("world2.csv", index_col="id") # reading world2 csv

print("\nReady to continue.")

#%%[markdown]

# Project website: [UTOPIA](https://anusha-raju.github.io/Utopia/)
# Project Git: [utopia.git](https://github.com/Anusha-raju/Utopia.git)

#%%[markdown]
# # Two Worlds 
# 
# I was searching for utopia, and came to this conclusion: If you want to do it right, do it yourself. 
# So I created two worlds. 
#
# Data dictionary:
# * age00: the age at the time of creation. This is only the population from age 30-60.  
# * education: years of education they have had. Education assumed to have stopped. A static data column.  
# * marital: 0-never married, 1-married, 2-divorced, 3-widowed  
# * gender: 0-female, 1-male (for simplicity)  
# * ethnic: 0, 1, 2 (just made up)  
# * income00: annual income at the time of creation   
# * industry: (ordered with increasing average annual salary, according to govt data.)   
#   0. leisure n hospitality  
#   1. retail   
#   2. Education   
#   3. Health   
#   4. construction   
#   5. manufacturing   
#   6. professional n business   
#   7. finance   
# 
# 
# Please do whatever analysis you need, convince your audience both, one, or none of these 
# worlds is fair, or close to a utopia. 
# Use plots, maybe pivot tables, and statistical tests (optional), whatever you deem appropriate 
# and convincing, to draw your conclusions. 
# 
# There are no must-dos, should-dos, cannot-dos. The more convenicing your analysis, 
# the higher the grade. It's an art.
#

#%%
print("World1 data->\n",world1.head())
print("World2 data->\n",world2.head())

#%%
#basic checks for world1
print("World1 basic info:")
print("Checking for any missing values(or na's):\n", world1.isna().any())
print("Dimensions of world1 dataset: ",world1.shape)
print("Concise info of world1: \n",world1.info)

#%%
#continuing for world1
#checking for the quantitative variables
print("Summary of quantitative variables of world1")
print(world1.describe()[['age00','income00']])
print("Median age value for world1:",world1['age00'].median())
print("Median income value for world1:",world1['income00'].median())

#%%[markdown]
# **Remarks: Since the median is less than the mean for income in world1 it indicates that the data distribution is skewed to the right (positively skewed).**
#%%[markdown]
##### Plotting the income distribution in world1
#%%
sns.histplot(data=world1, x='income00').set(xlabel='Annual Income',
       ylabel='Frequency',
       title='Income Distribution for world1')
plt.show()

#%%[markdown]
#  **Observation: As remarked, the distribution of income for world1 is *right* skewed**

#%%
print("Info of categorical variables of world1")
print(world1['education'].value_counts().sort_index())
print(world1['marital'].value_counts().sort_index())
print(world1['gender'].value_counts().sort_index())
print(world1['ethnic'].value_counts().sort_index())
print(world1['industry'].value_counts().sort_index())

#%%[markdown]
###### Distribution of years of education in world1
#%%

plt.figure(figsize=(8, 6))
sns.countplot(x ='education', data = world1, palette = "Set2")\
    .set(xlabel='Years of education',
       ylabel='Count',
       title='Education Distribution Count Plot for world1')
plt.show()

#%%[markdown]
# - The shape of the distribution of education for world1 is Multimodal distribution. 



#%%[markdown]
# #### Exploring the Relationship Between Income and Education Levels in world1
# %%
sns.scatterplot(data=world1, x='education', y='income00')\
    .set(xlabel='Years of education',
       ylabel='Annual Income',
       title='Relationship Between Income and Education Levels(world1)')

plt.show()

#%%[markdown]
# - There seems to be no significant influence of education on income in world1.

#%%
print("Checking for the Correlation coefficient between education and income in world1.")
correlation = world1['education'].corr(world1['income00'])
print(f'Correlation coefficient: {correlation}')


#%%[markdown]
# The above correlation coefficient implies that there isn't significant correlation between education and income in world1.

#%%[markdown]
# #### Exploring the Relationship Between Income and Marital status in world1
#%%
pivot_table = world1.pivot_table(values='income00', index='marital', aggfunc='mean')
pivot_table.columns = ['Average Income']  # Renaming column for clarity
print(pivot_table)

pivot_table.plot(kind='bar', legend=False)
plt.title('Average Income by Marital Status(world1)')
plt.xlabel('Marital Status')
plt.ylabel('Average Income')
plt.xticks(ticks=[0, 1, 2, 3], labels=['Never Married', 'Married', 'Divorced', 'Widowed'], rotation=0)
plt.show()

#%%[markdown]
#**Seems to be like there is no significant difference in average income among the different marital groups in world1.**



#%%[markdown]
# #### Plotting the correlation matrix to identify the interdependency among the variables in world1.
#%%
correlation_matrix = world1.corr()

# Create the heatmap
sns.heatmap(correlation_matrix, annot=True, fmt=".2f", cmap='coolwarm', square=True, cbar_kws={"shrink": .8})

# Add titles and labels
plt.title('Correlation Heatmap of Dataset Variables(world1)')
plt.show()

#%%[markdown]
# Observations:
# 1. A strong positive correlation exists between income and industry.
# 2. A considerable correlation exists between income and both ethnicity and gender.
# 3. There is a correlation between industry and ethnic and industry and gender.


#%%[markdown]
# ##### Analyze average income by industry and gender in world1
#%%
sns.scatterplot(data=world1, x='industry', y='income00', hue='gender')\
    .set(xlabel='Industry',
       ylabel='Annual Income',
       title='Plotting average income by industry and gender(world1)')

plt.show()

#%%[markdown]
# Remark: 
# 1. There are significant differences in income based on both industry and gender in world1.
# 2. The distribution of genders across different industries is unequal in world1, indicating that certain industries have a higher representation of one gender over the other. This disparity suggests potential biases or systemic factors influencing gender representation in various fields in world1.


#%%[markdown]
# ##### Conducting a **ANOVA** test to check if there is difference in income based on gender in world1.
#%%
print("Using a significance level of 0.05.")
print("Stating the Hypothesis:")
print("Null hypothesis: There is no difference in income based on gender.")
print("Alternate hypothesis: There is difference in income based on gender.")
# grouping the income by gender
groups = [group['income00'].values for name, group in world1.groupby('gender')]

# performing ANOVA test
f_statistic, p_value = stats.f_oneway(*groups)
print(f'F-statistic: {f_statistic}, P-value: {p_value}')

#%%[markdown]

# ***Conclusion:* Since the p-value is much less than the significance level of 0.05, we can reject the null hypothesis. This suggests that there is difference in income based on gender in world1.**

#%%[markdown]
# ##### Conducting a **ANOVA** test to check if there is difference in income based on industry in world1.
#%%
print("Using a significance level of 0.05.")
print("Stating the Hypothesis:")
print("Null hypothesis: There is no difference in income based on industry.")
print("Alternate hypothesis: There is difference in income based on industry.")
# grouping the income by industry
groups = [group['income00'].values for name, group in world1.groupby('industry')]

# performing ANOVA test
f_statistic, p_value = stats.f_oneway(*groups)
print(f'F-statistic: {f_statistic}, P-value: {p_value}')

#%%[markdown]

# ***Conclusion:* Since the p-value is much less than the significance level of 0.05, we can reject the null hypothesis. This suggests that there is difference in income based on industry in world1.**


#%%[markdown]
# ##### Analyze average income by ethnic in world1
#%%
sns.barplot(data=world1, x='ethnic', y='income00')\
.set(xlabel='Ethnic',
       ylabel='Annual Income',
       title='Plotting average income by ethnicity in world1')

plt.show()

#%%[markdown]
# Remark: There seems to be difference in income based on ethnicity in world1

#%%[markdown]
# ##### Conducting a **ANOVA** test to check if there is difference in income based on ethnic in world1.

#%%
print("Using a significance level of 0.05.")
print("Stating the Hypothesis:")
print("Null hypothesis: There is no difference in income based on ethnic category.")
print("Alternate hypothesis: There is difference in income based on ethnic category.")

# grouping the income by ethnic category
groups = [group['income00'].values for name, group in world1.groupby('ethnic')]
# perform ANOVA test
f_statistic, p_value = stats.f_oneway(*groups)

print(f'F-statistic: {f_statistic}, P-value: {p_value}')

#%%[markdown]

# ***Conclusion:* Since the p-value is significantly less than the alpha value of 0.05, we can reject the null hypothesis. This suggests that there is difference in income based on ethnicity in world1.**

#
# Following up with a post hoc tests

#%%
# performing Tukey's HSD test
tukey_result = pairwise_tukeyhsd(endog=world1['income00'], groups=world1['ethnic'], alpha=0.05)

print(tukey_result)

#%%[markdown]
# **In summary, all comparisons show significant differences in mean income between the ethnic groups analyzed, indicating that ethnicity does have an impact on income in world1.**



#%%[markdown]
# #### Evaluating whether there are differences in years of education by gender in world1.
# Conducting a Chi-squared test between gender and education in world1.
#%%
# creating a contingency table
contingency_table = pd.crosstab(world1['gender'], world1['education'])
print(contingency_table)

print("Using a significance level of 0.05.")
print("Stating the Hypothesis:")
print("Null hypothesis: The variables gender and education are independent")
print("Alternate hypothesis: The variables gender and education are not independent")


# performing the Chi-squared test
chi2_statistic, p_value, dof, expected = stats.chi2_contingency(contingency_table)

print(f'Chi-squared Statistic: {chi2_statistic}')
print(f'P-value: {p_value}')
print(f'Degrees of Freedom: {dof}')
print(f'Expected Frequencies:\n{expected}')

#%%[markdown]

# ***Conclusion:* Since the p-value is greater than the significance level of 0.05, we fail to reject the null hypothesis. This suggests that there is not enough evidence to conclude that gender has an effect on education levels in world1,meaning that any observed differences in education levels between genders in world1 could likely be due to random chance rather than a systematic relationship.**


#%%[markdown]

# Interpretation on World1:
# 1. Since the income histogram is right skewed, it indicates that a small number of individuals earn significantly more than the rest, which may suggest inequality.
# 2. The plots and ANOVA tests suggest that the annual income depends on gender, ethnicity and industry in world1, indicating systemic inequities.
# 3. The plot average income by industry and gender also suggests potential biases influencing gender representation in various industries.



#%%
#basic checks for world2
print("World2 Basic info")
print("Checking for any missing values(or na's):\n", world2.isna().any())
print("Dimensions of world2 dataset: ",world2.shape)
print("Concise info of world2: \n",world2.info)

#%%
#continuing for world2
#checking for the quantitative variables
print("Summary of quantitative variables of world2")
print(world2.describe()[['age00','income00']])
print("Median age value for world2:",world2['age00'].median())
print("Median income value for world2:",world2['income00'].median())

#%%[markdown]
# **Remarks: Since the median is less than the mean for income in world2 it indicates that the data distribution is skewed to the right (positively skewed).**
#%%[markdown]
##### Plotting the income distribution for world2
#%%
sns.histplot(data=world2, x='income00').set(xlabel='Annual Income',
       ylabel='Frequency',
       title='Income Distribution for world2')

plt.show()

#%%[markdown]
#  **Observation: As remarked, the distribution of income for world2 is *right* skewed**

#%%
print("Info of categorical variables of world2")
print(world2['education'].value_counts().sort_index())
print(world2['marital'].value_counts().sort_index())
print(world2['gender'].value_counts().sort_index())
print(world2['ethnic'].value_counts().sort_index())
print(world2['industry'].value_counts().sort_index())

#%%[markdown]
###### Distribution of years of education for world2
#%%

plt.figure(figsize=(8, 6))
sns.countplot(x ='education', data = world2, palette = "Set2")\
    .set(xlabel='Years of education',
       ylabel='Count',
       title='Education Distribution Count Plot for world2')
plt.show()

#%%[markdown]
# - The shape of the distribution of education for world2 is Multimodal distribution. 

#%%[markdown]
# #### Plotting the correlation matrix to identify the interdependency among the variables in world2.
#%%
correlation_matrix = world2.corr()

# Create the heatmap
sns.heatmap(correlation_matrix, annot=True, fmt=".2f", cmap='coolwarm', square=True, cbar_kws={"shrink": .8})

# Add titles and labels
plt.title('Correlation Heatmap of Dataset Variables(world2)')
plt.show()

#%%[markdown]
# Observations:
# A strong positive correlation exists between income and industry.


#%%[markdown]
# ##### Analyze average income by industry and gender for world2
#%%
sns.barplot(data=world2, x='industry', y='income00', hue='gender')\
    .set(xlabel='Industry',
       ylabel='Annual Income',
       title='Plotting average income by industry and gender(world2)')

plt.show()

#%%[markdown]
# Remark: <br>
# There are significant differences in income based on industry in world2.


#%%[markdown]
# ##### Conducting a **ANOVA** test to check if there is difference in income based on industry in world2.
#%%
print("Using a significance level of 0.05.")
print("Stating the Hypothesis:")
print("Null hypothesis: There is no difference in income based on industry.")
print("Alternate hypothesis: There is difference in income based on industry.")
# grouping the income by industry
groups = [group['income00'].values for name, group in world2.groupby('industry')]

# performing ANOVA test
f_statistic, p_value = stats.f_oneway(*groups)
print(f'F-statistic: {f_statistic}, P-value: {p_value}')

#%%[markdown]

# ***Conclusion:* Since the p-value is much less than the significance level of 0.05, we have evidence to reject the null hypothesis. This suggests that there is difference in income based on industry in world2.**

#%%[markdown]
# ##### Analyze average income by ethnic in world2
#%%
sns.barplot(data=world2, x='ethnic', y='income00')\
.set(xlabel='Ethnic',
       ylabel='Annual Income',
       title='Plotting average income by ethnicity(world2)')
plt.show()

#%%[markdown]
# Remark: There seems to be no significant difference in income based on ethnicity.

#%%[markdown]
# ##### Conducting a **ANOVA** test to check if there is difference in income based on ethnic in world2.

#%%
print("Using a significance level of 0.05.")
print("Stating the Hypothesis:")
print("Null hypothesis: There is no difference in income based on ethnic category.")
print("Alternate hypothesis: There is difference in income based on ethnic category.")

# grouping the income by ethnic category
groups = [group['income00'].values for name, group in world2.groupby('ethnic')]
# perform ANOVA test
f_statistic, p_value = stats.f_oneway(*groups)

print(f'F-statistic: {f_statistic}, P-value: {p_value}')

#%%[markdown]


# ***Conclusion:* Since the p-value is significantly high than the alpha value of 0.05, we fail to reject the null hypothesis. This suggests that there is no difference in income based on ethnicity in world2.**

#%%[markdown]
# #### Evaluating whether there are differences in years of education by gender in world2.
# Conducting a Chi-squared test between gender and education for world2.
#%%
# creating a contingency table
contingency_table = pd.crosstab(world2['gender'], world2['education'])
print(contingency_table)

print("Using a significance level of 0.05.")
print("Stating the Hypothesis:")
print("Null hypothesis: The variables gender and education are independent")
print("Alternate hypothesis: The variables gender and education are not independent")


# performing the Chi-squared test
chi2_statistic, p_value, dof, expected = stats.chi2_contingency(contingency_table)

print(f'Chi-squared Statistic: {chi2_statistic}')
print(f'P-value: {p_value}')
print(f'Degrees of Freedom: {dof}')
print(f'Expected Frequencies:\n{expected}')

#%%[markdown]

# ***Conclusion:* Since the p-value is greater than the significance level of 0.05, we fail to reject the null hypothesis. This suggests that there is not enough evidence to conclude that gender has an effect on education levels in world2.**


#%%[markdown]

# Interpretation on World2:
# 1. Since the income histogram is right skewed, it indicates that a small number of individuals earn significantly more than the rest.
# 2. The plots and ANOVA tests suggest that the annual income does not depend on gender and ethnicity in world2, indicating systemic equality.
# 3. The plots also suggest that there is difference in income based on industry.

#%%[markdown]
# # Final thoughts
# <br>A realistic utopia as quoted by [isocracy.org](https://isocracy.org/content/three-visions-realist-utopiais) are models for a Great Society, and any realist utopian model will share three essential characteristics.
# The basic structure is : 
# 1. entail liberal democracy or a republican form of government, in which people have a say in the matters that affect their lives
# 2. guard against the extremes of inequality so that concentrations of wealth cannot be used to exploit the less wealthy or to buy politicians
# 3. ensure that everyone has access to the necessities of life such as food, shelter, healthcare, etc.
# <br><br>
#
#
#
# In both the worlds<br>
#  - The variables defining Demographics are Age, gender, marital status and ethnicity<br>
#  - The variables defining Socioeconomic status are Education, income and industry<br><br>
# 
#
# Based on the interpretations on world1, there is an inequality in income and their is a potential bias influencing the gender representations in various industries and a difference in income based on ethnicity and gender which suggests that the ***world1 is not fair*** on both Demographics and Socioeconomic status and is not close to a utopia.<br>
# <br>The analysis of world2 indicates that income is skewed due to variations across industries, while gender and ethnicity do not appear to influence annual income.
# 
#
# In my view, different income levels across industries can still align with a utopian model due to the following reasons:
# - Value-Based Income: In a utopia, income could be based on the value and societal contribution of different industries.
# - Equity Over Equality: A utopian model might emphasize equity rather than strict equality. 
#
#
# Hence I fail to infer that the world2 is unfair and hence can suggest that world2 is close to a utopia.

 
