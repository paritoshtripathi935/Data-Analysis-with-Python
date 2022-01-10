import pandas as pd
import numpy as np


def calculate_demographic_data(print_data=True):
    # Read data from file
    df = pd.read_csv('adult.data.csv')

    # How many of each race are represented in this dataset? This should be a Pandas series with race names as the index labels.    
    race_count = df.race.value_counts()


    # What is the average age of men?
    agecount = []
    for i in range(0,len(df)):
      if df.sex[i] == "Male":
        agecount.append(df.age[i])

    average_age_men = round(np.mean(agecount),1)

    # What is the percentage of people who have a Bachelor's degree?
    count = 0
    for i in range(0,len(df)):
      if df.education[i] == "Bachelors":
        count = count + 1
    
    percentage_bachelors = round((count/len(df.education))*100,1)

    # What percentage of people with advanced education (`Bachelors`, `Masters`, or `Doctorate`) make more than 50K?
    # What percentage of people without advanced education make more than 50K?
    # with and without `Bachelors`, `Masters`, or `Doctorate`
    
    educated_groups=[df[df["education"]=="Bachelors"],df[df["education"]=="Masters"],df[df["education"]=="Doctorate"]]

    educated_groups=pd.concat(educated_groups)

    higher_education = (len(educated_groups[educated_groups["salary"]==">50K"])/len(educated_groups))*100

    uneducated_groups = df[df["education"] != "Bachelors"]
    uneducated_groups = uneducated_groups[uneducated_groups["education"] != "Masters"]
    uneducated_groups = uneducated_groups[uneducated_groups["education"] != "Doctorate"]

    # percentage with salary >50K
    higher_education_rich = round(higher_education,1)

    lower_education_rich = round((len(uneducated_groups[uneducated_groups["salary"] == ">50K"]) / len(uneducated_groups)) * 100, 1)

    # What is the minimum number of hours a person works per week (hours-per-week feature)?
    min_work_hours = df['hours-per-week'].min()

    # What percentage of the people who work the minimum number of hours per week have a salary of >50K?
    less_groups = df[df["hours-per-week"] == min_work_hours]
    
    num_min_workers = round((len(less_groups[less_groups["salary"] == ">50K"]) / len(less_groups)) * 100, 1)

    rich_percentage = num_min_workers

    # What country has the highest percentage of people that earn >50K?
    
    wealth_percentages = (df[df["salary"] == ">50K"]["native-country"].value_counts() / df["native-country"].value_counts())*100

    highest_earning_country = wealth_percentages.idxmax()

    highest_earning_country_percentage = round(wealth_percentages.max(), 1)

    # Identify the most popular occupation for those who earn >50K in India.
    rich_indians = df[df["native-country"] == "India"]
    rich_indians = rich_indians[rich_indians["salary"] == ">50K"]
    top_IN_occupation = rich_indians['occupation'].value_counts().idxmax()


    # DO NOT MODIFY BELOW THIS LINE

    if print_data:
        print("Number of each race:\n", race_count) 
        print("Average age of men:", average_age_men)
        print(f"Percentage with Bachelors degrees: {percentage_bachelors}%")
        print(f"Percentage with higher education that earn >50K: {higher_education_rich}%")
        print(f"Percentage without higher education that earn >50K: {lower_education_rich}%")
        print(f"Min work time: {min_work_hours} hours/week")
        print(f"Percentage of rich among those who work fewest hours: {rich_percentage}%")
        print("Country with highest percentage of rich:", highest_earning_country)
        print(f"Highest percentage of rich people in country: {highest_earning_country_percentage}%")
        print("Top occupations in India:", top_IN_occupation)

    return {
        'race_count': race_count,
        'average_age_men': average_age_men,
        'percentage_bachelors': percentage_bachelors,
        'higher_education_rich': higher_education_rich,
        'lower_education_rich': lower_education_rich,
        'min_work_hours': min_work_hours,
        'rich_percentage': rich_percentage,
        'highest_earning_country': highest_earning_country,
        'highest_earning_country_percentage':
        highest_earning_country_percentage,
        'top_IN_occupation': top_IN_occupation
    }
