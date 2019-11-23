# Food Safety in Chicago with Respect to Public Health

***_______________ UPDATED VERSION _______________ ***

## Abstract
In this project, our interest is focused on food inspections and the different violations with regards to the outcome of the inspection. In addition, we explore relations to food poisoning and economic status. A dataset providing information on the food inspections made from 01.01.2010 to the present, will be carefully studied. In addition we will look at data taken from a website with reports of food poisoning in Chicaco ([I was poisoned](https://iwaspoisoned.com/location/united-states/illinois/chicago#botpress)). 
> Last year, Foodborne Chicago classified over 2,600 tweets related to food poisoning in Chicago which led to 233 food poisoning reports submitted to CDPH. From those reports an additional 150 restaurant and food service inspections occurred ([City of Chicago](https://www.chicago.gov/city/en/depts/cdph/provdrs/healthy_communities/news/2014/apr/one-year-after-launch--foodborne-chicago-continues-to-enhance-fo.html)). 

Food poisoning is a health issue, and it is important to classify where they happen and take the right actions to ensure that it does not happen in the future. We will therefore explore if it is possible to predict if a facility can cause you food poisoning and also look at the financial status of the area to see if these factors also have an impact.

## Research Questions
- Is there a direct link between the inspection result and the risk factor of the facility given in the food inspection dataset? 
- Are the facilities with the lowest risk factors concentrated in certain areas? 
- What factors should we take into account to evaluate the food safety/quality coming from a specific facility? 
- Is there a correlation between the violations and reports of food poisoning? 
- Is there a correlation between financial status of an area and the reports of food poisoning?

## Dataset
The main dataset that we will use is open-sourced and hosted by the city of Chicago ([Food inspections Chicago]( https://kaggle.com/chicago/chicago-food-inspections)). The file has a size of 220 MB and contains the results of several food inspections conducted by the city within different food facilities (restaurants, groceries, and others) between January 1, 2010 and today. Other information that can be found includes institution-specific data (legal name, license number, address), their risk of altering public health from a nutritional point of view, and the type of violation(s) committed during the different inspections.

Other data of interest is the reports of food poisoning from ([I was poisoned](https://iwaspoisoned.com/location/united-states/illinois/chicago#botpress)). We will collect this data using webscrapping. **(SIZE?)**


**ARE WE STILL USING THE PUBLIC HEALTH DATASET?**
Another dataset of interest that we plan to use contains different health indicators (cancer, diabetes, ...) as well as economical status for the different community areas in Chicago ( <a href = "https://data.cityofchicago.org/Health-Human-Services/Public-Health-Statistics-Selected-public-health-in/iqnk-2tcu/data"> Public Health Statistics</a>). In order to merge our data, we will use another dataset of 2 MB that maps the different community areas according to their geographical location (<a href = "https://data.cityofchicago.org/dataset/Community-Areas/vrxf-vc4k/data?fbclid=IwAR2YiR_0kgW1s0iSrKFti5LXmy7zTqQDQqDpFGdaTQ92jS-TYA0gDsU5LzU" > Community Area Dataset </a>).
   

Finally, to enhance our data, we may use other public and small (< 5 MB) datasets available for the city of Chicago (<a href = "https://www.chicagohealthatlas.org"> Chicago Health Atlas</a>). These may include indicators like diabetes, obesity, alcoholism, wealth/income in the community.


## List of internal milestones up until project milestone 3
### Task 4 : Machine Learning predicting result of inspection (deadline = 02.12) 
  * Exlore different parameters, which are the optimal to use?
  * Finalise machine learning to predict result of inspection. 

### Task 5 : Explore correlations with food poisoning (deadline = 9.12)
  * Relationship between violations in food inspections and reports of food poisoning.
  * Visualise relationship. 
    

### Task 6 : Explore other correlations with food poisoning (deadline = 13.11)
  * Relationship between sanitation and food poisoning.  
  * Relationship between financial status an sanitation/food poisoning.


### Task 7 : Create datastory and write report (deadline = 20.12)
  * Create blog with datastory. 
  * Finalise the report for delivery. 


## Questions for TAs

- ?


***____________MILESTONE 1____________***
## Abstract

In this project, our interest is focused on the access to nutritionally adequate and safe food in different parts of Chicago and the impact on the local population's health. A dataset providing information on the food inspections made from 01.01.2010 to the present, will be carefully studied. Our first goal is to quantify the availability of safe food in each community based on the results from the food inspections. 
After illustrating this data, we may study the distribution of health indicators throughout Chicago (given by the Chicago Health Atlas website). These health issues are known to be particularly influenced by unhealthy diets, and so possibly linked to the food safety of the community. 
We may also be attentive to the economical status of the communities and check if there is a relationship with respect to the food safety concerns mentioned previously.


## Research questions

- Is there a direct link between the inspection result and the risk factor of the facility given in the food inspection dataset? 
- Are the facilities with the lowest risk factors concentrated in certain areas? 
- What factors should we take into account to evaluate the food safety/quality coming from a specific facility? 


## Dataset

The main dataset that we will use is open-sourced and hosted by the city of Chicago (<a href = "https://kaggle.com/chicago/chicago-food-inspections"> Food inspections Chicago</a>). The file has a size of 220 MB and contains the results of several food inspections conducted by the city within different food facilities (restaurants, groceries, and others) between January 1, 2010 and today. Other information that can be found includes institution-specific data (legal name, license number, address), their risk of altering public health from a nutritional point of view, and the type of violation(s) committed during the different inspections.

Another dataset of interest that we plan to use contains different health indicators (cancer, diabetes, ...) as well as economical status for the different community areas in Chicago ( <a href = "https://data.cityofchicago.org/Health-Human-Services/Public-Health-Statistics-Selected-public-health-in/iqnk-2tcu/data"> Public Health Statistics</a>). In order to merge our data, we will use another dataset of 2 MB that maps the different community areas according to their geographical location (<a href = "https://data.cityofchicago.org/dataset/Community-Areas/vrxf-vc4k/data?fbclid=IwAR2YiR_0kgW1s0iSrKFti5LXmy7zTqQDQqDpFGdaTQ92jS-TYA0gDsU5LzU" > Community Area Dataset </a>).
    
Finally, to enhance our data, we may use other public and small (< 5 MB) datasets available for the city of Chicago (<a href = "https://www.chicagohealthatlas.org"> Chicago Health Atlas</a>). These may include indicators like diabetes, obesity, alcoholism, wealth/income in the community.


## List of internal milestones up until project milestone 2

### Task 0 : Data wrangling and exploring (deadline = 30.10) 
  * Plot visual graphs in order to look for potential outliers, duplicates and missing values.
  * Explore the relationship between the risk factor and the inspection result of the facilities.

### Task 1 : Mapping food inspection indicators (deadline = 7.11)
  * Relationship between the health risk level and the localisation of the facilities.
  * Relationship between the inspection results and the localisation of the facilities. 
    

### Task 2 : Making sense of the additional datasets (deadline = 14.11)
  * Introducing other datasets regarding the health conditions throughout Chicago to the project. 
  * Explore correlations between the food safety of each community and their health indicators.


### Task 3 : Discussion and Conclusions (deadline = 28.11)
  * Proving statistically whether or not the food safety is causing health problems such as obesity, diabetes and alcoholism. 
  * Draw further conclusions with respect to the financial status of a given community. 


## Questions for TAs

- What librairies could be useful for the creation of a map?
- Is the project ambitious enough or too ambitious?
- Are the research questions relevant enough?
- There are empty columns in the provided data. Must we take further notice to this or simply delete the empty columns ?



