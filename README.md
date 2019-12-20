                                        
                                                            --- MILESTONE 3 ---
                                        
[<b>Datastory:</b>](https://marisofie.github.io/epfl_ada_project/)
[Main file milestone 3](main_file_milestone3.ipynb)

# Abstract
*One of our previous goals was to predict food poisoning with the use of Machine Learning algorithms. However, we have found that the precision of these predictions is quite poor. The amount of information on food poisoning inspection type is very low compared to the other inspection types, so it is difficult to obtain good statistical results for the predictions.
The aim of our work is now orientated towards proving that facility inspections and food poisonings are not always correlated. We have found that in some cases, factors unrelated to the facility's hygiene like the proximity to the sea and the proximity to the city center are correlated with the rate of food poisoning per zip code area.
Also, the webscraping will enable the analysis of the posts written in reports of food poisoning on iwaspoisoned.com. Text handling allows the identification of topics and of specific foods that have caused sicknesses.*

*Food poisoning is a health issue, and it is important to classify where they happen and take the right actions to ensure that it does not happen in the future. Even though this project cannot predict the likelyhood of a specific facility to cause food poisoning, it can still help people to choose more wisely where to eat or shop for food.* 

# Questions
- What kinds of food cause food poisoning ? 
- Are the facility inspections correlated with food poisoning ? 
- Does the location of the facility impact the food poisoning likelyhood ?
- To which extent can we predict food poisoning ?
- What must we look out for to avoid the sickness ?


# Different chapters of the notebook
- Context (Mariam)
  - Visualization of the number of outbreaks per state
  - Types of food that are more likely to cause food poisoning are given 
- Spatial visualization (Mariam)
  - Inspection results and risk levels of facilities in chicago are mapped with respect to the zip code area
- Relationships investigation (Mariam and Mari Sofie)
  - Correlation between inspection results and food poisoning
  - Correlation between the risk level and the food poisoning
  - Correlation between the violation type and the food poisoning
- Sea exploration (Mariam and Jasmine)
  - Ecoli from the beaches
  - Is the distance to the city center more correlated to food poisoning than the distance to the sea ? 
- Natural Langage processing of post from iwaspoisonned.com (Jasmine)
  - Identification of these most frequent words in the posts
  - Finding of topics 
  - Investigation on the use of health related terms and food related terms with respect to the distance to the sea
- Applied marching learning (Ahmed)
  - Building and testing models for predicting cases of food poisoning
  - Proof that the food poisonings are hard to predict
  
  
  ### Other tasks
  - Data Cleaning (Mariam, Ahmed, Mari Sofie and Jasmine)
  - Code cleaning and representation/visualizations (Mari Sofie)
  
  Realisation of data story by Mari Sofie and Mariam
  
  
  Presentation by Jasmine and Mari Sofie 
  
  Poster by Ahmed
  
# Dataframes 

The first dataset used is US Chicago (https://wwwn.cdc.gov/norsdashboard/)(950 ko) which gives information on multiple outbreaks in America from 1998 to 2017. The columns of interest are 'Etiology','Illnesses','Hospitalizations','Food Vehicle' and 'Food Contaminated Ingredient'. It is a very useful dataset to find the types of food that often cause foodborne illnesses.

Our main dataset hosted by the city of Chicago ([Food inspections Chicago]( https://kaggle.com/chicago/chicago-food-inspections)) is worked on in the second chapter. The file has a size of 220 MB and contains the results of several food inspections conducted by the city within different food facilities (restaurants, groceries, and others) from the 1st of  January 2010. More information from the dataset includes institution-specific data (legal name, license number, address), their risk of altering public health (depending on how difficult it is to conserve the food that is served) and the type of violation(s) committed during the different inspections. It is useful for the visualization of the risk and results of the inspections per zip code.

We have found a dataset "beach-e.-coli-predictions.csv" (373.53 KB) providing information on the presence of the bacteria Ecoli on beaches in Chicago. The given information are the dates, the beach names, the locations of the beaches and the predicted levels of Ecoli. It is important because the most frequent cases of food poisoning occurs near the seaside. 

Another data of interest ([I was poisoned](https://iwaspoisoned.com/location/united-states/illinois/chicago#botpress)) is a collection of complaints from various people that have experienced food sickness after going to a restaurant. Webscraping this website allows us to obtain a dataset of the specific restaurants that caused the complaints.


                                        
                                                          --- MILESTONE 2 ---
                                        


# Food Inspections in Chicago with Respect to Food Poisoning


*While exploring the data, we realised that the violations are linked to the hygiene of the facility rather than to the quality of the food (nutriment wise). It is therefore difficult to relate the food inspection results with long-term health issues (diabetes, obesity, etc...). From now on, we shall focus on the food poisoning since it is likely to be linked to the violations described in our main dataset.*

## Data Structuring : 

- [main_file](main_file_milestone2.ipynb): We regrouped all the important information in this file for **milestone 2**. This file is a merged version of the files below ( excepted the [Cleaning data](data_cleaning.ipynb) file and the [Webscraping_website](Webscraping_website.ipynb)).

- [Cleaning data](data_cleaning.ipynb): Cleansing the data frame and exporting the data in a csv file : clean_data.csv

- [mapping_data](mapping_data.ipynb): Creating maps that illustrate the values of different caracteristics per zip code.  

- class [violation_preprocessing](violation_preprocessing.py) : based on the official website [Code Violations](https://webapps1.chicago.gov/healthinspection/Code_Violations.jsp) we decided to translate the *violations* column into a more conveniant form. The values were categorised according to the gravity of the violation.

- [poisoning_violations_factors](poisoning_violations_factors.ipynb): The violation factors that are most likely to provoque food poisoning have been found. The frequency of different violation between all inspection types (not necessarily related to food poisoning) were compared to the inspection in food poisoning cases.

- [machine_learning](machine_learning.ipynb) : Predicting inspection results for further analysis of food poisoning, predicting the inspection types (food poisoning based on the violations, inspection results, zip code of the facility and the risk level). 

- [Webscraping_website](Webscraping_website.ipynb): Takes in the information from [I was poisoned](https://iwaspoisoned.com/location/united-states/illinois/chicago#botpress) and stores a data in a csv file (Foodpoisoning.csv).


## Abstract

In this project, the aim would be to identify the factors that contribute the most to food poisoning, so to establish the importance of the facilities' committed violations, location, risk factor and inspection results. 

Each of our datasets give insight on what could potentially contribute to food poisoning. The original one ('Food_Inspection.csv') regroups the inspections results made from 01.01.2010 to the present, locations and violations of different facilities. This will be particularly useful to obtain the types of violations that often cause food poisoning. Also, with the given locations, we are able to place each facility on a map and see if the most risky facilities are clustered in certain areas.

It has been noticed that many risky facilities are located by the seaside, which coincides with the presence of Ecoli coming from beaches. We shall furtherly investigate the correlation between Ecoli on the beaches and the food safety in facilities near the beaches thanks to another dataset that was found.

Another dataset including reports of food poisoning in Chicaco by citizens :
([I was poisoned](https://iwaspoisoned.com/location/united-states/illinois/chicago#botpress)) will be used to target the facilities that cause complaints. 

Once all the factors that contribute to food poisoning are found, we may consider using machine learning. Machine Learning enables us to provide a predictive method to know which facility is more likely to cause a sickness by establishing the corresponding coefficients (that illustrates how important the factor is) mathematically.

Food poisoning is a health issue, and it is important to classify where they happen and take the right actions to ensure that it does not happen in the future. This project could help predict the likelyhood of a specific facility to cause food poisoning so that one may choose more wisely where to eat or shop for food.

## Research Questions
- Is there a direct link between the violations noticed during the inspections and the food poisoning of the facility ? 
- Are the facilities with the highest food poisoning risks concentrated in certain areas? 
- What factors should we take into account to evaluate the food safety coming from a specific facility? 
- Is there a correlation between financial status/sanitation of an area and the reports of food safety?
- Are the inspection types predictable with enough accuracy ? Could this help us predict food poisoning ? 

## Dataset
The main dataset that will be used is open-sourced and hosted by the city of Chicago ([Food inspections Chicago]( https://kaggle.com/chicago/chicago-food-inspections)). The file has a size of 220 MB and contains the results of several food inspections conducted by the city within different food facilities (restaurants, groceries, and others) from the 1st of  January 2010. More information from the dataset includes institution-specific data (legal name, license number, address), their risk of altering public health (depending on how difficult it is to conserve the food that is served) and the type of violation(s) committed during the different inspections.

Another data of interest ([I was poisoned](https://iwaspoisoned.com/location/united-states/illinois/chicago#botpress)) is a collection of complaints from various people that have experienced food sickness after going to a restaurant. Webscraping this website allows us to obtain a dataset of the specific restaurants that caused the complaints.

It has been observed that the most frequent cases of food poisoning occurs near the seaside. To broaden our research, we have chosen to study another dataset "beach-e.-coli-predictions.csv" (373.53 KB). It shows predicted E. coli levels based on an experimental analytical modeling approach.

Sanitation in the streets could also have an impact on the restaurant's hygiene. To explore this hypothesis, a dataset called sanitation.csv (from the website ([City Of Chicago](https://data.cityofchicago.org/Service-Requests/311-Service-Requests-Sanitation-Code-Complaints-Hi/me59-5fac), 34.4 Mo) has been introduced. Hopefully, this could give an extra explanation on why some facilities are less hygienic than others.



## List of internal milestones up until project milestone 3 
- Establish the statistical relations to mathematically prove the impact of the main factors on food poisoning.
- Find the features that could help predict the food poisoning in the most accurate way.
- Obtaining more information on the complaints made by civilians on the restaurants that caused food poisoning and comparing them with our previous results.
- Create a score that takes into account all the factors that contribute to food safety and test its workability on real poisoning complaint from [I was poisoned](https://iwaspoisoned.com/location/united-states/illinois/chicago#botpress).
- Clean and homogenise the code
- Write a report that combines the previous analysis on the food inspections in Chicago.
- Write a data story


## Questions for TAs

- Is the research broad enough ? Should we try to find more data sets that could be of use in analysing the food poisoning ?
- Is there a more efficient way to perform webscraping ? 
- Are the statistical methods applied in the Machine Learning part enough for the predictions?







                                             ---  MILESTONE 1 ---

### *Abstract*

*In this project, our interest is focused on the access to nutritionally adequate and safe food in different parts of Chicago and the impact on the local population's health. A dataset providing information on the food inspections made from 01.01.2010 to the present, will be carefully studied. Our first goal is to quantify the availability of safe food in each community based on the results from the food inspections.* 
*After illustrating this data, we may study the distribution of health indicators throughout Chicago (given by the Chicago Health Atlas website). These health issues are known to be particularly influenced by unhealthy diets, and so possibly linked to the food safety of the community.* 
*We may also be attentive to the economical status of the communities and check if there is a relationship with respect to the food safety concerns mentioned previously.*


### *Research questions*

- *Is there a direct link between the inspection result and the risk factor of the facility given in the food inspection dataset?* 
- *Are the facilities with the lowest risk factors concentrated in certain areas?* 
- *What factors should we take into account to evaluate the food safety/quality coming from a specific facility?* 


### Dataset

*The main dataset that we will use is open-sourced and hosted by the city of Chicago (<a href = "https://kaggle.com/chicago/chicago-food-inspections"> Food inspections Chicago</a>). The file has a size of 220 MB and contains the results of several food inspections conducted by the city within different food facilities (restaurants, groceries, and others) between January 1, 2010 and today. Other information that can be found includes institution-specific data (legal name, license number, address), their risk of altering public health from a nutritional point of view, and the type of violation(s) committed during the different inspections.*

*Another dataset of interest that we plan to use contains different health indicators (cancer, diabetes, ...) as well as economical status for the different community areas in Chicago ( <a href = "https://data.cityofchicago.org/Health-Human-Services/Public-Health-Statistics-Selected-public-health-in/iqnk-2tcu/data"> Public Health Statistics</a>). In order to merge our data, we will use another dataset of 2 MB that maps the different community areas according to their geographical location (<a href = "https://data.cityofchicago.org/dataset/Community-Areas/vrxf-vc4k/data?fbclid=IwAR2YiR_0kgW1s0iSrKFti5LXmy7zTqQDQqDpFGdaTQ92jS-TYA0gDsU5LzU" > Community Area Dataset </a>).*
    
*Finally, to enhance our data, we may use other public and small (< 5 MB) datasets available for the city of Chicago (<a href = "https://www.chicagohealthatlas.org"> Chicago Health Atlas</a>). These may include indicators like diabetes, obesity, alcoholism, wealth/income in the community.*


### *List of internal milestones up until project milestone 2*

#### *Task 0 : Data wrangling and exploring (deadline = 30.10)* 
  * *Plot visual graphs in order to look for potential outliers, duplicates and missing values.*
  * *Explore the relationship between the risk factor and the inspection result of the facilities.*

#### *Task 1 : Mapping food inspection indicators (deadline = 7.11)*
  * *Relationship between the health risk level and the localisation of the facilities.*
  * *Relationship between the inspection results and the localisation of the facilities.* 
    

#### *Task 2 : Making sense of the additional datasets (deadline = 14.11)*
  * *Introducing other datasets regarding the health conditions throughout Chicago to the project.* 
  * *Explore correlations between the food safety of each community and their health indicators.*


#### *Task 3 : Discussion and Conclusions (deadline = 28.11)*
  * *Proving statistically whether or not the food safety is causing health problems such as obesity, diabetes and alcoholism.* 
  * *Draw further conclusions with respect to the financial status of a given community.* 


### *Questions for TAs*

- *What librairies could be useful for the creation of a map?*
- *Is the project ambitious enough or too ambitious?*
- *Are the research questions relevant enough?*
- *There are empty columns in the provided data. Must we take further notice to this or simply delete the empty columns ?*

