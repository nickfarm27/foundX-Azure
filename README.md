# foundX-Azure
- - - -
## Table of Contents
- [Dataset Features Explanation](#Dataset-Features-Explanation)
- [AutoML](#AutoML)
- [Designer](#Designer)
- [datasets](#datasets)

## Dataset Features Explanation
The [raw dataset](https://github.com/nickfarm27/foundX-Azure/blob/main/datasets/raw_dataset.csv) is a collection of 17 socio-economic factors and health status data of a population from the counties of 26 selected states in the United States. The description of each feature of the dataset shown in the table below. The column 'Accepted Range of Values' is a guide on what values are accepted for the [regression model](https://github.com/nickfarm27/foundX-Azure/blob/main/AutoML/regression.py).

Feature  | Description | Accepted Range of Values
------------- | ------------- | -------------
% Fair or Poor Health | Percentage of adults that report poor health | None
% Smokers | Percentage of adults that reported currently smoking | 0 - 100
% Adults with Obesity | Percentage of adults that report BMI >= 30 | 0 - 100
Food Environment Index | Indicator of access to healthy foods (0 is worst, 10 is best) | 0 - 10
% Physically Inactive | Percentage of adults that report no leisure-time physical activity | 0 - 100
% With Access to Exercise Opportunities | Percentage of the population with access to places for physical activity | 0 - 100
% Excessive Drinking | Percentage of adults that report excessive drinking | 0 - 100
% Uninsured | Percentage of people under age 65 without insurance | 0 - 100
% Vaccinated | Percentage of annual Medicare enrollees having an annual flu vaccination | 0 - 100
High School Graduation Rate | Graduation rate | 0 - 100
% Some College | Percentage of adults age 25-44 with some post-secondary education | 0 - 100
% Unemployed | Percentage of population ages 16+ unemployed and looking for work | 0 - 100
% Children in Poverty | Percentage of children (under age 18) living in poverty | 0 - 100
Income Ratio | Ratio of household income at the 80th percentile to income at the 20th percentile | 0 - 10
% Single-Parent Households | Percentage of children that live in single-parent households | 0 - 100
Violent Crime Rate | Violent crimes per 100,000 population | 0 - 2,000
Average Daily PM2.5 | Average daily amount of fine particulate matter in micrograms per cubic meter | 5 - 20
% Severe Housing Problems | Percentage of households with at least 1 of 4 housing problems: overcrowding, high housing costs, or lack of kitchen or plumbing facilities | 0 - 100

## [AutoML](https://github.com/nickfarm27/foundX-Azure/tree/main/AutoML)
Contains the Python scripts to test custom input data on the deployed models from Automated ML.
- Regression Model - https://github.com/nickfarm27/foundX-Azure/blob/main/AutoML/regression.py
- Classification Model - https://github.com/nickfarm27/foundX-Azure/blob/main/AutoML/classifier.py

## [Designer](https://github.com/nickfarm27/foundX-Azure/tree/main/Designer)
Contains the Python scripts used in the 'Execute Python Script' module of our Designer pipeline.
[pythonscript1.py](https://github.com/nickfarm27/foundX-Azure/blob/main/Designer/pythonscript1.py) is used to generate the association rules.
[pythonscript2.py](https://github.com/nickfarm27/foundX-Azure/blob/main/Designer/pythonscript2.py) is used to run K-means clustering and assign tiers to the rules.

## [datasets](https://github.com/nickfarm27/foundX-Azure/tree/main/datasets)
Contains the raw dataset that is imported into Azure Machine Learning Designer and the output dataset that consists of the generated rules with their tier values.
- Raw Dataset - https://github.com/nickfarm27/foundX-Azure/blob/main/datasets/raw_dataset.csv
- Output Dataset - https://github.com/nickfarm27/foundX-Azure/blob/main/datasets/output_rules.csv
