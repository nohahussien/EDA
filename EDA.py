import pandas as pd
import numpy as np
import matplotlib as plt
import seaborn as sns

# A prelimenary heatmap
df = pd.read_csv(r"StudentsPerformance.csv")

sns.heatmap(data = df.corr(numeric_only= True),annot = True, cmap = "seismic", vmin = -1)
# to convert other variables to binary/numeric to do a heatmap that includes all variables
# gender
df["gender_bi"] = df["gender"].map({"male": 0, "female": 1})

# test preparation course
df["test_prep_bi"] = df["test preparation course"].map({"none": 0, "completed": 1})

# lunch
df["lunch_bi"] = df["lunch"].map({"free/reduced": 0, "standard": 1})

#parental level of education
education_map = {"some high school": 1, "high school": 2, "some college": 3, "associate's degree": 4, "bachelor's degree": 5, "master's degree": 6}
df["parental_ed"] = df["parental level of education"].map(education_map)
# to delete the old columns
df.drop(["gender", "test preparation course","lunch", "parental level of education"], axis = 1, inplace = True)

# to combine reading and writing tests into one language test
df["language score"] = df["reading score"] + df["writing score"]
df.drop(["reading score", "writing score"], axis = 1, inplace = True)

#the extensive heatmap
sns.heatmap(data = df.corr(numeric_only= True),annot = True, cmap = "seismic", vmin = -1)


df1 = pd.read_csv(r"StudentsPerformance.csv")
df1["language score"] = df1["reading score"] + df1["writing score"]
df1.drop(["reading score", "writing score"], axis = 1, inplace = True)

# H1 (gender)
df_gender = df1.groupby("gender")
means1 = df_gender[[ "math score", 'language score']].mean()
ax = means1.plot(kind="bar", figsize=(10, 6), rot = 0, ylabel = "Scores", title = "Scores among males and females")
plt.legend(loc="upper right")
plt.grid(True, axis='y')
ax.set_axisbelow(True)

# H2 (ethnic groups)
df_race = df1.groupby("race/ethnicity")
means2 = df_race[[ "math score", 'language score']].mean()
ax = means2.plot(kind="bar", figsize=(10, 6), rot = 0, ylabel = "Scores", title = "Scores among ethnic groups")
plt.legend(loc="upper left")
plt.grid(True, axis='y')
ax.set_axisbelow(True)

# H3 (parental level of education)
# Parents' education in an ascending order
education_order = ['some high school','high school','some college',
                "associate's degree","bachelor's degree","master's degree"]

# Get unique values from your data and sort them according to your defined order
existing_levels = [level for level in education_order if level in df1['parental level of education'].unique()]

# Convert to categorical and sort
df1['parental level of education'] = pd.Categorical(df1['parental level of education'], categories=existing_levels, ordered=True)
df_sorted = df1.sort_values('parental level of education')
df_ed = df1.groupby("parental level of education")
means3 = df_ed[[ "math score", 'language score']].mean()
ax = means3.plot(kind="bar", figsize=(10, 6), rot = 45, ylabel = "Scores", title = "Student scores and Parents' education")
plt.legend(loc="upper left")
plt.grid(True, axis='y')
ax.set_axisbelow(True)

# H4 (lunch)
df_lunch = df1.groupby("lunch")
means4 = df_lunch[[ "math score", 'language score']].mean()
ax = means4.plot(kind="bar", figsize=(10, 6), rot = 45, ylabel = "Scores", title = "Lunch")
plt.grid(True, axis='y')
ax.set_axisbelow(True)
ax.legend(loc="upper left")

# H5 (test preparation course)
df_test = df1.groupby("test preparation course")

means5 = df_test[[ "math score", 'language score']].mean()
ax = means5.plot(kind="bar", figsize=(10, 6), rot = 45, ylabel = "Scores", title = "Test preparation course")
plt.grid(True, axis='y')
ax.set_axisbelow(True)
ax.legend(loc="upper right")


