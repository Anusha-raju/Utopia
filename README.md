# [Fairness in Focus: A tale of two worlds](https://anusha-raju.github.io/Utopia/)
Project Website: [UTOPIA](https://anusha-raju.github.io/Utopia/)<br>
Author: [Anusha Umashankar](https://github.com/Anusha-raju)

Created on : October 24th, 2024

# Contents
1. [Objective](#objective)
2. [Data](#data)
    1. [Data source](#datasource)
    2. [Data dictionary](#datadictionary)
3. [WORLD1](#world1)
	1.  [EDA on World1](#edaonworld1)
		1. [Data Profiling](#dataprofiling)
		2. [Data Visualization & Hypothesis testing](#datavisualization)
	2. [Interpretation on World1](#interpretationonWorld1)
4. [WORLD2](#world2)
	1.  [EDA on World2](#edaonworld2)
		1. [Data Profiling](#dataprofiling2)
		2. [Data Visualization & Hypothesis testing](#datavisualization2)
	2. [Interpretation on World2](#interpretationonWorld2)

5. [Final thoughts](#Finalthoughts)
6. [Project Resources](#projectresources)
7. [Python Libraries Used](#pythonlibs)

#

![Utopia](https://github.com/Anusha-raju/Utopia/blob/main/images/utopia.jpg)

### Objective <a name="objective"></a>
To analyse if the two worlds are fair, or close to a utopia.

## Data <a name="data"></a>
### Data source <a name="datasource"></a>
The data is provided in CSV file format (world1.csv and world2.csv) and was created for the DATS6103 Introduction to Data Mining course, taught by Professor Divya Pandove Narula.

### Data dictionary <a name="datadictionary"></a>
Both the worlds has the below data dictionary:
* age00: The age at the time of creation. This is only the population from age 30-60. 
* education: Years of education they have had. Education assumed to have stopped and is a static data column.
* marital: 0-never married, 1-married, 2-divorced, 3-widowed.
* gender: 0-female, 1-male (for simplicity)
* ethnic: 0, 1, 2 (just made up).
* income00: Annual income at the time of creation.
* industry: (ordered with increasing average annual salary, according to govt data.).
	1. Leisure n hospitality
	2. Retail
	3. Education
	4. Health
	5. Construction
	6. Manufacturing
	7. Professional n business
	8. Finance

## WORLD1 <a name="world1"></a>

### EDA on World1 <a name="edaonworld1"></a>

#### Data Profiling <a name="dataprofiling"></a>
World1 dataset

![world1.head()](https://github.com/Anusha-raju/Utopia/blob/main/images/world1-head.png)



The above image shows the first five records in World1.

The World1 dataset has no missing values and the dimensions are 24000 rows across 7 columns.

![world1.describe()](https://github.com/Anusha-raju/Utopia/blob/main/images/world1%20missing%20values.png)





**Summary of qualitative variables of world1**

![Summary of qualitative variables of world1](https://github.com/Anusha-raju/Utopia/blob/main/images/categorical%20summary%201.png)


![Summary of qualitative variables of world1](https://github.com/Anusha-raju/Utopia/blob/main/images/categorical%20summary%202.png)



**Summary of quantitative variables of world1**

![Summary of quantitative of world1](https://github.com/Anusha-raju/Utopia/blob/main/images/world1%20quantitaive%20summary.png)




**Remarks: Since the median is less than the mean for income in world1, it indicates that the data distribution is skewed to the right (positively skewed).**

### Data Visualization & Hypothesis testing  <a name="datavisualization"></a>


#### Plot: Income distribution in world1


![Income in world1](https://github.com/Anusha-raju/Utopia/blob/main/images/world1%20income.png)



**Observation: As remarked, the distribution of income for world1 is *right* skewed**



#### Plot: Distribution of years of education in world1


![education distribution image](https://github.com/Anusha-raju/Utopia/blob/main/images/world1%20education.png)



- The shape of the distribution of education for world1 is Multimodal distribution.




#### Plot: Relationship Between Income and Education Levels in world1


![Income and Education Levels in world1](https://github.com/Anusha-raju/Utopia/blob/main/images/income%20education%20world1.png)



- There seems to be no significant influence of education on income in world1.

- The Correlation coefficient between education and income in world1: -5.1988070239674995e-05 ,which also implies that there isn't significant correlation between education and income in world1.




#### Plot: Relationship Between Income and Marital status in world1

![income and marital status world1](https://github.com/Anusha-raju/Utopia/blob/main/images/income%20marital%20status%20world1.png)

**Seems to be like there is no significant difference in average income among the different marital groups in world1.**




#### Plot: Correlation matrix to identify the interdependency among the variables in world1.


![correlation matrix world1](https://github.com/Anusha-raju/Utopia/blob/main/images/correlation%20matrix%20world1.png)



**Observations:**

1. A strong positive correlation exists between income and industry.

2. A considerable correlation exists between income and both ethnicity and gender.

3. There is a correlation between industry and ethnic and industry and gender.




#### Plot: Average income by industry and gender in world1

![Average income by industry and gender in world1](https://github.com/Anusha-raju/Utopia/blob/main/images/income%20industry%20gender%20world1.png)


**Remark:**

1. There are significant differences in income based on both industry and gender in world1.

2. The distribution of genders across different industries is unequal in world1, indicating that certain industries have a higher representation of one gender over the other. This disparity suggests potential biases or systemic factors influencing gender representation in various fields in world1.






#### **ANOVA** test to check if there is difference in income based on gender in world1.
Using a significance level of 0.05.<br><br>

Stating the Hypothesis:<br>
Null hypothesis: There is no difference in income based on gender.<br>
Alternate hypothesis: There is difference in income based on gender.<br><br>

The obtained test results are -> F-statistic: 923.1415737034732, P-value: 5.355760965843564e-199<br><br>

***Conclusion:* Since the p-value is much less than the significance level of 0.05, we can reject the null hypothesis. This suggests that there is difference in income based on gender in world1.**





#### **ANOVA** test to check if there is difference in income based on industry in world1.
Using a significance level of 0.05.<br><br>

Stating the Hypothesis:<br>
Null hypothesis: There is no difference in income based on industry.<br>
Alternate hypothesis: There is difference in income based on industry.<br><br>

The obtained test results are -> F-statistic: 19091.648128224577, P-value: 0.0<br><br>

***Conclusion:* Since the p-value is much less than the significance level of 0.05, we can reject the null hypothesis. This suggests that there is difference in income based on industry in world1.**





#### Plot:  Average income by ethnic in world1


![Average income by ethnic in world1](https://github.com/Anusha-raju/Utopia/blob/main/images/income%20by%20ethnicity%20world1.png)



***Remark:* There seems to be difference in income based on ethnicity in world1.**





#### **ANOVA** test to check if there is difference in income based on ethnic in world1.
Using a significance level of 0.05.<br><br>

Stating the Hypothesis:<br>
Null hypothesis: There is no difference in income based on ethnic category.<br>
Alternate hypothesis: There is difference in income based on ethnic category.<br><br>

The obtained test results are ->F-statistic: 1125.691934385774, P-value: 0.0
<br><br>
***Conclusion:* Since the p-value is significantly less than the alpha value of 0.05, we can reject the null hypothesis. This suggests that there is difference in income based on ethnicity in world1.**
<br><br><br>



**Post hoc tests**<br>
- Performed Tukey's HSD test<br><br>



![Tukey's HSD test world1](https://github.com/Anusha-raju/Utopia/blob/main/images/tuskey%20result%20world1.png)

<br><br>

**In summary, all comparisons show significant differences in mean income between the ethnic groups analyzed, indicating that ethnicity does have an impact on income in world1.**




#### **Examined the differences in years of education by gender in world1.**

**Chi-squared test between gender and education in world1.**<br>

Using a significance level of 0.05.<br><br>

Stating the Hypothesis:<br>
Null hypothesis: The variables gender and education are independent<br>
Alternate hypothesis: The variables gender and education are not independent<br><br>



![Chi-squared test](https://github.com/Anusha-raju/Utopia/blob/main/images/chisuare%20world1.png)




***Conclusion:* Since the p-value is greater than the significance level of 0.05, we fail to reject the null hypothesis. This suggests that there is not enough evidence to conclude that gender has an effect on education levels in world1,meaning that any observed differences in education levels between genders in world1 could likely be due to random chance rather than a systematic relationship.**



## Interpretation on World1: <a name="interpretationonWorld1"></a>

1. Since the income histogram is right skewed, it indicates that a small number of individuals earn significantly more than the rest, which may suggest inequality.

2. The plots and ANOVA tests suggest that the annual income depends on gender, ethnicity and industry in world1, indicating systemic inequities.

3. The plot average income by industry and gender also suggests potential biases influencing gender representation in various industries.





## WORLD2 <a name="world2"></a>

### EDA on World2 <a name="edaonworld2"></a>

#### Data Profiling <a name="dataprofiling2"></a>
World2 dataset

![world2.head()](https://github.com/Anusha-raju/Utopia/blob/main/images/world2-head.png)



The above image shows the first five records in World2.

The World2 dataset has no missing values and the dimensions are 24000 rows across 7 columns.

![world2.describe()](https://github.com/Anusha-raju/Utopia/blob/main/images/world2%20missing%20values.png)

**Summary of qualitative variables of world2**

![Summary of qualitative variables of world2](https://github.com/Anusha-raju/Utopia/blob/main/images/categorical%20summary%2021.png)


![Summary of qualitative variables of world2](https://github.com/Anusha-raju/Utopia/blob/main/images/categorical%20summary%2022.png)



**Summary of quantitative variables of world2**

![Summary of quantitative of world2](https://github.com/Anusha-raju/Utopia/blob/main/images/world2%20quantitaive%20summary.png)

**Remarks: Since the median is less than the mean for income in world2 it indicates that the data distribution is skewed to the right (positively skewed).**

### Data Visualization & Hypothesis testing  <a name="datavisualization2"></a>


#### Plot: Income distribution in world2

![Income in world2](https://github.com/Anusha-raju/Utopia/blob/main/images/world2%20income.png)

**Observation: As remarked, the distribution of income for world2 is *right* skewed**



#### Plot: Distribution of years of education in world2


![education distribution image](https://github.com/Anusha-raju/Utopia/blob/main/images/education%20world2.png)


- The shape of the distribution of education for world2 is Multimodal distribution.




#### Plot: Correlation matrix to identify the interdependency among the variables in world2.


![correlation matrix world2](https://github.com/Anusha-raju/Utopia/blob/main/images/correlation%20matrix%20world2.png)


**Observations:**
- A strong positive correlation exists between income and industry.




#### Plot: Average income by industry and gender for world2.


![Average income by industry and gender](https://github.com/Anusha-raju/Utopia/blob/main/images/average%20income%20by%20industry%20and%20gender(world2).png)


**Remark:** <br>
- There are significant differences in income based on industry in world2.



#### **ANOVA** test to check if there is difference in income based on industry in world2.


Using a significance level of 0.05.<br><br>

Stating the Hypothesis:<br>
Null hypothesis: There is no difference in income based on industry.<br>
Alternate hypothesis: There is difference in income based on industry.<br><br>


The obtained test results are -> F-statistic: 18810.332110998344, P-value: 0.0<br><br>


***Conclusion:* Since the p-value is much less than the significance level of 0.05, we have evidence to reject the null hypothesis. This suggests that there is difference in income based on industry in world2.**



#### Plot: Average income by ethnic in world2


![Average income by ethnic](https://github.com/Anusha-raju/Utopia/blob/main/images/Average%20income%20by%20ethnic%20world2.png)



***Remark:* There seems to be no significant difference in income based on ethnicity.**




#### **ANOVA** test to check if there is difference in income based on ethnic in world2.

Using a significance level of 0.05.<br><br>


Stating the Hypothesis:<br>
Null hypothesis: There is no difference in income based on ethnic category.<br>
Alternate hypothesis: There is difference in income based on ethnic category.<br><br>


The obtained test results are ->  F-statistic: 0.3428483735431711, P-value: 0.7097492961501475<br><br>


***Conclusion:* Since the p-value is significantly high than the alpha value of 0.05, we fail to reject the null hypothesis. This suggests that there is no difference in income based on ethnicity in world2.**



#### **Examined the differences in years of education by gender in world2.**


**Chi-squared test between gender and education in world2.**<br><br>
Using a significance level of 0.05.<br><br>


Stating the Hypothesis:<br>
Null hypothesis: The variables gender and education are independent<br>
Alternate hypothesis: The variables gender and education are not independent<br><br>




![Chi-squared test](https://github.com/Anusha-raju/Utopia/blob/main/images/chi%20square%20world2.png)


***Conclusion:* Since the p-value is greater than the significance level of 0.05, we fail to reject the null hypothesis. This suggests that there is not enough evidence to conclude that gender has an effect on education levels in world2.**




## Interpretation on World2: <a name="interpretationonWorld2"></a>


1. Since the income histogram is right skewed, it indicates that a small number of individuals earn significantly more than the rest.
2. The plots and ANOVA tests suggest that the annual income does not depend on gender and ethnicity in world2, indicating systemic equality.
3. The plots also suggest that there is difference in income based on industry.



## Final thoughts <a name="Finalthoughts"></a>

<br>A realistic utopia as quoted by [isocracy.org](https://isocracy.org/content/three-visions-realist-utopia) are models for a Great Society, and any realist utopian model will share three essential characteristics.


The basic structure is : 
1. entail liberal democracy or a republican form of government, in which people have a say in the matters that affect their lives
2. guard against the extremes of inequality so that concentrations of wealth cannot be used to exploit the less wealthy or to buy politicians
3. ensure that everyone has access to the necessities of life such as food, shelter, healthcare, etc.
<br><br>





In both the worlds<br>
 - The variables defining Demographics are Age, gender, marital status and ethnicity<br>
 - The variables defining Socioeconomic status are Education, income and industry<br><br>


Based on the interpretations on world1, there is an inequality in income and their is a potential bias influencing the gender representations in various industries and a difference in income based on ethnicity and gender which suggests that the ***world1 is not fair*** on both Demographics and Socioeconomic status and is not close to a utopia.<br>
<br>The analysis of world2 indicates that income is skewed due to variations across industries, while gender and ethnicity do not appear to influence annual income.


 
In my view, different income levels across industries can still align with a utopian model due to the following reasons:
- Value-Based Income: In a utopia, income could be based on the value and societal contribution of different industries.
- Equity Over Equality: A utopian model might emphasize equity rather than strict equality. 


Hence I fail to infer that the world2 is unfair and hence can suggest that world2 is close to a utopia.



## Project Resources <a name="projectresources"></a>
1. The code is in [Utopia.py](https://github.com/Anusha-raju/Utopia/blob/main/midterm_Utopia.py)
2. The world1 data is in [World1.csv](https://github.com/Anusha-raju/Utopia/blob/main/world1.csv)
3. The world2 data is in [World2.csv](https://github.com/Anusha-raju/Utopia/blob/main/world2.csv)
4. The project link is [Utopia-github](https://github.com/Anusha-raju/Utopia.git)


## Python Libraries Used <a name="pythonlibs"></a>

* numpy
* pandas
* matplotlib, pyplot
* seaborn
* scipy, stats
* statsmodels


