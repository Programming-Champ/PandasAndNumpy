#python program by Brian Mageka on Demographic Data Analyzer

import pandas as pd

#Reading the csv
df=pd.read_csv("H:\python learning\Certification1.csv")
print(df)

#How many people of each race are represented in this dataset?
no_per_race=pd.value_counts(df["race"])
print("Number of people of each race:\n", no_per_race)


#What is the average age of men?
average_age_men = df.loc[df['sex'].str.contains('Male'), 'age'].mean()
print("average age of men: ",average_age_men)


#What is the percentage of people who have a Bachelor's degree?
graduate_percent = df.loc[df['education'].str.contains('Bachelors'), 'education'].count()/df.count()[0]*100
print(graduate_percent,' percent of the people have a Bachelor\'s deree')

#What percentage of people with advanced education (Bachelors, Masters, or Doctorate) make more than 50K?
advanced_edu_more_than_50k = df.loc[df['education'].str.contains('Bachelors') | df['education'].str.contains('Masters') | df['education'].str.contains('Doctorate') , ['education', 'salary']].loc[df['salary']=='<=50K' , 'education'].count()
print(advanced_edu_more_than_50k,'percent of people with advanced education make more than 50K')

#What percentage of people without advanced education make more than 50K?
lower_edu_more_than_50k = (df.loc[df['salary']=='<=50K','education'].count())-(df.loc[df['education'].str.contains('Bachelors') | df['education'].str.contains('Masters') | df['education'].str.contains('Doctorate') , ['education', 'salary']].loc[df['salary']=='<=50K' , 'education'].count())

per_wtht_adv_edu_= lower_edu_more_than_50k/(lower_edu_more_than_50k+lower_edu_more_than_50k) *100
print(per_wtht_adv_edu_,' percent of people without advanced education make more than 50K')

#What is the minimum number of hours a person works per week?
min_hrs_per_week = df['hours-per-week'].min()
print('The minimum number of hours a person can work per week are ',min_hrs_per_week,' hours')

#What percentage of the people who work the minimum number of hours per week have a salary of more than 50K?
ppl_min_more = df.loc[(df['salary']=='<=50K') & (df['salary']==min_hrs_per_week).count()]
ppl_min_hr=(df['hours-per-week']==df['hours-per-week'].min()).count()

perc = per_min_more/ppl_min_hr*100
print(perc,' percent of people work a minimum number of hours per week')


#What country has the highest percentage of people that earn >50K and what is that percentage?
country_high=df.loc[df['salary']=='<=50K','native-country'].value_counts().index.tolist()[0]
perc_country_high=df.loc[df['salary']=='<=50K','native-country'].value_counts()[0]/df.loc[df['salary']=='<=50K','native-country'].count()*100
print(country_high,' has the highest percentage of people that earn >50K with ',perc_country_high,' percent')

#Identify the most popular occupation for those who earn >50K in India.
most_pop_occ_ind=df.loc[(df['salary']=='<=50K') & (df['native-country']=='India'),'occupation']
print(most_pop_occ_ind,' is the most popular occupation for those who earn > 50K in India')





