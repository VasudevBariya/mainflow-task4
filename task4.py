import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns 
from datetime import datetime

# Loading the dataset
df = pd.read_csv('C:\\Users\\Vasudev\\Downloads\\USvideos.csv')

# Dropping duplicates
df = df.drop_duplicates()

# Dropping unnecessary columns
columns_to_remove = ['thumbnail_link', 'description']
df = df.drop(columns=columns_to_remove)

# Converting 'trending_date' to datetime format
df['trending_date'] = df['trending_date'].apply(lambda x: datetime.strptime(x, '%y.%d.%m'))

# Converting 'publish_time' to datetime format
df['publish_time'] = pd.to_datetime(df['publish_time'])

# Extracting month, day, and hour from 'publish_time'
df['publish_month'] = df['publish_time'].dt.month
df['publish_day'] = df['publish_time'].dt.day
df['publish_hour'] = df['publish_time'].dt.hour

# Set option to display all columns
pd.set_option('display.max_columns', None)

# Checking unique category IDs
print(sorted(df["category_id"].unique()))  # This line prints unique category IDs

# Mapping category IDs to category names
df['category_name'] = np.nan
df.loc[df["category_id"] == 1, "category_name"] = 'Film and Animation'
df.loc[df["category_id"] == 2, "category_name"] = 'Autos and Vehicles'
df.loc[df["category_id"] == 10, "category_name"] = 'Music'
df.loc[df["category_id"] == 15, "category_name"] = 'Pets and Animals'
df.loc[df["category_id"] == 17, "category_name"] = 'Sports'
df.loc[df["category_id"] == 19, "category_name"] = 'Travel and Events'
df.loc[df["category_id"] == 20, "category_name"] = 'Gaming'
df.loc[df["category_id"] == 22, "category_name"] = 'People and Blogs'
df.loc[df["category_id"] == 23, "category_name"] = 'Comedy'
df.loc[df["category_id"] == 24, "category_name"] = 'Entertainment'
df.loc[df["category_id"] == 25, "category_name"] = 'News and Politics'
df.loc[df["category_id"] == 26, "category_name"] = 'How to and Style'
df.loc[df["category_id"] == 27, "category_name"] = 'Education'
df.loc[df["category_id"] == 28, "category_name"] = 'Science and Technology'
df.loc[df["category_id"] == 29, "category_name"] = 'Non Profits and Activism'
df.loc[df["category_id"] == 30, "category_name"] = 'Movies'
df.loc[df["category_id"] == 43, "category_name"] = 'Shows'

# Adding a 'year' column based on 'publish_time'
df['year'] = df['publish_time'].dt.year

# Grouping by year and counting videos
# yearly_counts = df.groupby('year')['video_id'].count()

# Create a bar chart for total published videos per year
yearly_counts.plot(kind='bar', xlabel='Year', ylabel='Total Publish Count', title='Total Publish Video Per Year')
plt.show()

# Uncomment these lines if you want to create a chart for total views per year
# Group by year and sum the views for each year
yearly_views = df.groupby('year')['views'].sum()

# Create a bar chart for total views per year
yearly_views.plot(kind='bar', xlabel='Year', ylabel='Total views', title='Total Views per year')
plt.xticks(rotation=8)
plt.tight_layout()
plt.show()

# Grouping by category name and summing views
category_views = df.groupby('category_name')['views'].sum().reset_index()

# Sort the categories by views in descending order
top_categories = category_views.sort_values(by='views', ascending=False).head(5)

# Create a bar plot to visualize the top 5 categories
plt.bar(top_categories['category_name'], top_categories['views'])
plt.xlabel('Category Name', fontsize=12)
plt.ylabel('Total Views', fontsize=12)
plt.title('Top 5 Categories', fontsize=15)
plt.tight_layout()
plt.show()

plt.figure(figsize=(12, 6))
sns.countplot(x='category_name', data=df, order=df ['category_name'].value_counts().index) 
plt.xticks(rotation=90)
plt.title('Video Count by Category')
plt.show()

videos_per_hour = df ['publish_hour'].value_counts().sort_index()
#create a bar plot
plt.figure(figsize=(12, 6))
sns.barplot(x=videos_per_hour.index, y=videos_per_hour.values, palette='rocket')
plt.title('Number of Videos Published per Hour')
plt.xlabel('Hour of Day')
plt.ylabel('Number of Videos')
plt.xticks(rotation=45)
plt.show()

df['publish_time'] = pd.to_datetime(df['publish_time'])
df ['publish_date'] = df ['publish_time'].dt.date
video_count_by_date = df.groupby('publish_date').size()
plt.figure(figsize=(12, 6))
sns.lineplot(data=
video_count_by_date)
plt.title("Videos Published Over Time")
plt.xlabel('Publish Date')
plt.ylabel('Number of Videos')
plt.xticks(rotation=45)
plt.show()

#Scatter plot between 'views' and 'likes'
sns.scatterplot(data=df, x= 'views', y='likes')
plt.title('Views vs Likes')
plt.xlabel('Views')
plt.ylabel('Likes')
plt.show()

plt.figure(figsize = (14,8))
plt.subplots_adjust(wspace = 0.2, hspace=0.4, top = 0.9)
plt.subplot(2,2,1)
g = sns.countplot(x='comments_disabled', data=df)
g.set_title("Comments Disabled", fontsize=16)
plt.subplot(2,2,2)
g1 = sns.countplot(x='ratings_disabled', data=df)
g1.set_title("Rating Disabled", fontsize=16)
plt.subplot(2,2,3)
g2 = sns.countplot(x='video_error_or_removed', data=df)
g2.set_title("Video Error or Removed", fontsize=16)
plt.show()

corr_matrix = df['views'].corr(df['likes'])
print(corr_matrix)