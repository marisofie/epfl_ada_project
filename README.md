# Food Insecurity in Chicago with Respect to Public Health



# Abstract

In this project, our interest is focused on the access to nutritionally adequate and safe food in different parts of Chicago and the impact on the local's health. A dataset providing information on the food inspections made from 01.01.2010 to the present, will be carefully studied. Our first goal is to quantify the availability of safe food in each community based on the results from the food inspections. 
Once this data has been illustrated onto a map, we may study the distribution of sicknesses such as obesity, diabetes and alcoholism throughout Chicago (given by the Chicago Health Atlas website). These health issues are known to be particularly influenced by unhealthy diets, and so possibly linked to the food insecurity of the community. 
We may also be attentive to the financial status of the communities and check if there is a relationship with respect to the food insecurity mentioned previously.


# Research questions

- Is there a direct link between the inspection results and the risk factor of the facility ? 
- What factors should we take into account to judge the food quality from a certain facility ? 
- Are the facilities with the lowest risk factors concentrated in certain areas ? 


# Dataset

The main dataset that we will use is an open dataset hosted by the city of chicago (https://kaggle.com/chicago/chicago-food-inspections). The file has a size of 220 MB and contains the results of several food inspections conducted by the city within different food facilities (restaurants, groceries, and others) between January 1, 2010 and today. Other informations includes institution-specific data (Legal name, license number, address), their risk of altering public health from a nutritional point of view, or the type of violation(s) committed during the different inspections.

Another dataset of interest that we plan to use contains 27 different health indicators (cancer, diabetes,..) as well as some economic status for the different community areas in Chicago (https://data.cityofchicago.org/Health-Human-Services/Public-Health-Statistics-Selected-public-health-in/iqnk-2tcu/data). In order to merge the different datasets, we will use another dataset of 2 MB (<a href = "https://data.cityofchicago.org/dataset/Community-Areas/vrxf-vc4k/data?fbclid=IwAR2YiR_0kgW1s0iSrKFti5LXmy7zTqQDQqDpFGdaTQ92jS-TYA0gDsU5LzU" > community area dataset <\a>) that maps the different community areas according to their geographical location.
    
Finally, to enrich our data, we may use other public and small (< 5 MB) datasets available for the city of Chicago (https://www.chicagohealthatlas.org): 
    -> Diabetes 
    -> Obesity 
    -> Alcoholism
    -> Wealth/ Income of the community


# A list of internal milestones up until project milestone 2
Add here a sketch of your planning for the next project milestone.

Task 0 : Data wrangling and exploring. Plot visual graphs in order to look for potential outliers, duplicates and missing values. (deadline = 30.10)

Task 1 : Analyzing the following : 
    - relationship between the health risk level and the localisation of the facilities
    - relationship between the inspection results and the localisation of the facilities 
    (deadline = 7.11)

Task 2 : Introducing other datasets regarding the health conditions throughout Chicago to the project. Finding correlations between the food insecurity of each community and the sickness rates.
(deadline = 14.11)

Task 3 : Proving statistically whether or not the food insecurity is causing health problems such as obesity, diabetes and alcoholism. Draw further conclusions with respect to the financial status of a given community. (deadline = 28.11)

# Questions for TAa
Add here some questions you have for us, in general or project-specific.

- What librairies could be useful for the creation of a map ?
- Are the problematics ambitious enough / too ambitious ?
