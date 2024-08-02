import pandas as pd
import numpy as np

#1.1

df = pd.read_csv("iris.csv")
#print (df)

#1.2

#print("First 10 rows of the dataset:")
#print(df.head(10))

#1.3

iris_dc = df.columns #all data columns from the income dataset
#print (iris_dc)#first 2 columns from the income dataset
#print (iris_dc [ :2])#find datatypes for all the columns
#print (df.dtypes)

#2.1

# Calculate summary statistics for each feature
summary_statistics = df.describe()
#print("\nSummary Statistics for Each Feature:")
#print(summary_statistics)

#2.2
'''
# Calculate the cumulative sum of sepal length and add it as a new column
#df['cumulative_sepal_length'] = df['Sepal.Length'].cumsum()

# Calculate the mean sepal length for each species
#mean_sepal_length_by_species = df.groupby('Species')['Sepal.Length'].mean().reset_index()
#mean_sepal_length_by_species.columns = ['Species', 'mean_sepal_length']

# Merge the mean values back into the original DataFrame
#df = df.merge(mean_sepal_length_by_species, on='Species', how='left')

# Display the DataFrame with the new columns
#print(df.head(10))'''

#print(df.groupby('Species')['Sepal.Length'].mean().reset_index(name='mean_sepal_length'))

#3

# Check for missing values
#print("Missing values in each column before imputation:")
#print(df.isnull().sum())

# Replace missing values in numeric columns with the mean of each column
#df[df.select_dtypes(include='number').columns] = df.select_dtypes(include='number').fillna(df.select_dtypes(include='number').mean())

# Verify that there are no missing values left
#print("\nMissing values in each column after imputation:")
#print(df.isnull().sum())

#4

# Filter the dataset to include only rows where the sepal length is greater than 5.0
#print("Filtered dataset shape:", (df[df['Sepal.Length'] > 5.0]).shape)
#print("Filtered dataset with only rows of the species Setosa:", (df[df['Species'] == 'setosa']).shape)

#5.1

#print(df.groupby('Species')['Petal.Length'].agg(['mean', 'median', 'std']))

#5.2

#print(df['Species'].value_counts())

#5.3

#print(df.groupby('Species')['Petal.Width'].agg(['min', 'max']))

#5.4

#print(df.groupby('Species')['Sepal.Width'].mean().sort_values(ascending=False).head(5))

#6.1
'''
numerical_features = ['Sepal.Length', 'Sepal.Width', 'Petal.Length', 'Petal.Width']
for feature in numerical_features:
    df[feature] = (df[feature] - df[feature].min()) / (df[feature].max() - df[feature].min())
print(df.head(50))'''


#numerical_features = ['Sepal.Length', 'Sepal.Width', 'Petal.Length', 'Petal.Width']
#df[numerical_features] = (df[numerical_features] - df[numerical_features].min()) / (df[numerical_features].max() - df[numerical_features].min())
#print(df.head(100))

#6.2
#df['petal_ratio'] = df['Petal.Length'] / df['Petal.Width']
#print(df.head())


#7.1

#print(df.groupby('Species')['Sepal.Length'].quantile([0.25, 0.5, 0.75]))

#7.2

#print(df.groupby('Species')['Petal.Length'].agg(lambda x: x.max() - x.min()))

#8.1
'''
#species_info = {
    'setosa': {'habitat': 'Mediterranean regions', 'color': 'Red', 'size': 'Small'},
    'versicolor': {'habitat': 'Alpine meadows', 'color': 'White', 'size': 'Medium'},
    'virginica': {'habitat': 'Coastal regions', 'color': 'Orange', 'size': 'Large'}
}

#print(pd.DataFrame(species_info).T.reset_index().rename(columns={'index': 'species'}))'''

#8.2
'''
species_info = {'Species': ['setosa', 'versicolor', 'virginica'], 
                'typical_habitat': ['moist meadows', 'woodlands', 'coastal areas'], 
                'average_height': [30, 60, 70], 
                'flower_color': ['white', 'purple', 'pink']}
print(pd.merge(df, pd.DataFrame(species_info), on='Species').head())'''

#9.1

#print(df.assign(flower_size=lambda x: np.select([x['Petal.Length']<3,(x['Petal.Length'] >= 3)&(x['Petal.Length'] < 5)],['small','medium'],'large')).head(50))



























