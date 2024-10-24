# Fairness in Focus: A tale of two worlds
Author: [Anusha Umashankar](https://github.com/Anusha-raju)
Created on : October 23rd, 2024

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

#

## Objective <a name="objective"></a>
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




**Summary of quantitative variables of world1**

![Summary of quantitative of world1](https://github.com/Anusha-raju/Utopia/blob/main/images/world1%20quantitaive%20summary.png)



**Summary of qualitative variables of world1**

![Summary of qualitative variables of world1](https://github.com/Anusha-raju/Utopia/blob/main/images/categorical%20summary%201.png)


![Summary of qualitative variables of world1](https://github.com/Anusha-raju/Utopia/blob/main/images/categorical%20summary%202.png)



**Remarks: Since the median is less than the mean for income in world1, it indicates that the data distribution is skewed to the right (positively skewed).**

#### Data Visualization & Hypothesis testing  <a name="datavisualization"></a>
##### Plot: Income distribution in world1


![Income in world1](https://github.com/Anusha-raju/Utopia/blob/main/images/world1%20income.png)



**Observation: As remarked, the distribution of income for world1 is *right* skewed**

##### Plot: Distribution of years of education in world1


![education distribution image](https://github.com/Anusha-raju/Utopia/blob/main/images/world1%20education.png)



- The shape of the distribution of education for world1 is Multimodal distribution.

##### Plot: Relationship Between Income and Education Levels in world1


![Income and Education Levels in world1](https://github.com/Anusha-raju/Utopia/blob/main/images/income%20education%20world1.png)



- There seems to be no significant influence of education on income in world1.

The Correlation coefficient between education and income in world1: -5.1988070239674995e-05 which implies that there isn't significant correlation between education and income in world1.

##### Plot: Relationship Between Income and Marital status in world1

![income and marital status world1](https://github.com/Anusha-raju/Utopia/blob/main/images/income%20marital%20status%20world1.png)

**Seems to be like there is no significant difference in average income among the different marital groups in world1.**

##### Plot: Correlation matrix to identify the interdependency among the variables in world1.


![correlation matrix world1](https://github.com/Anusha-raju/Utopia/blob/main/images/correlation%20matrix%20world1.png)



** Observations:**

1. A strong positive correlation exists between income and industry.

2. A considerable correlation exists between income and both ethnicity and gender.

3. There is a correlation between industry and ethnic and industry and gender.

##### Plot: Average income by industry and gender in world1

![Average income by industry and gender in world1](https://github.com/Anusha-raju/Utopia/blob/main/images/income%20industry%20gender%20world1.png)


**Remark:**

1. There are significant differences in income based on both industry and gender in world1.

2. The distribution of genders across different industries is unequal in world1, indicating that certain industries have a higher representation of one gender over the other. This disparity suggests potential biases or systemic factors influencing gender representation in various fields in world1.


##### **ANOVA** test to check if there is difference in income based on gender in world1.
Using a significance level of 0.05.

Stating the Hypothesis:
Null hypothesis: There is no difference in income based on gender.
Alternate hypothesis: There is difference in income based on gender.

The obtained test results are -> F-statistic: 923.1415737034732, P-value: 5.355760965843564e-199

***Conclusion:* Since the p-value is much less than the significance level of 0.05, we can reject the null hypothesis. This suggests that there is difference in income based on gender in world1.**

##### **ANOVA** test to check if there is difference in income based on industry in world1.
Using a significance level of 0.05.

Stating the Hypothesis:
Null hypothesis: There is no difference in income based on industry.
Alternate hypothesis: There is difference in income based on industry.

The obtained test results are -> F-statistic: 19091.648128224577, P-value: 0.0

***Conclusion:* Since the p-value is much less than the significance level of 0.05, we can reject the null hypothesis. This suggests that there is difference in income based on industry in world1.**


##### Plot:  Average income by ethnic in world1


![Average income by ethnic in world1](https://github.com/Anusha-raju/Utopia/blob/main/images/income%20by%20ethnicity%20world1.png)



***Remark:* There seems to be difference in income based on ethnicity in world1.**


##### **ANOVA** test to check if there is difference in income based on ethnic in world1.
Using a significance level of 0.05.

Stating the Hypothesis:
Null hypothesis: There is no difference in income based on ethnic category.
Alternate hypothesis: There is difference in income based on ethnic category.

The obtained test results are ->F-statistic: 1125.691934385774, P-value: 0.0

***Conclusion:* Since the p-value is significantly less than the alpha value of 0.05, we can reject the null hypothesis. This suggests that there is difference in income based on ethnicity in world1.**

** Post hoc tests**
- Performed Tukey's HSD test



![Tukey's HSD test world1](https://github.com/Anusha-raju/Utopia/blob/main/images/tuskey%20result%20world1.png)



**In summary, all comparisons show significant differences in mean income between the ethnic groups analyzed, indicating that ethnicity does have an impact on income in world1.**

##### **Examined the differences in years of education by gender in world1.**

**Chi-squared test between gender and education in world1.**

Using a significance level of 0.05.

Stating the Hypothesis:
Null hypothesis: The variables gender and education are independent
Alternate hypothesis: The variables gender and education are not independent



![Chi-squared test](https://github.com/Anusha-raju/Utopia/blob/main/images/chisuare%20world1.png)




***Conclusion:* Since the p-value is greater than the significance level of 0.05, we fail to reject the null hypothesis. This suggests that there is not enough evidence to conclude that gender has an effect on education levels in world1,meaning that any observed differences in education levels between genders in world1 could likely be due to random chance rather than a systematic relationship.

## Interpretation on World1: <a name="interpretationonWorld1"></a>

1. Since the income histogram is right skewed, it indicates that a small number of individuals earn significantly more than the rest, which may suggest inequality.

2. The plots and ANOVA tests suggest that the annual income depends on gender, ethnicity and industry in world1, indicating systemic inequities.

3. The plot average income by industry and gender also suggests potential biases influencing gender representation in various industries.



