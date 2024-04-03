import pandas as pd 

# Read CSV
q1_data = pd.read_csv('Q1_2023/q1_listings.csv')
q1_reviews = pd.read_csv('Q1_2023/q1_reviews.csv')

# Summary Information
print("Data Information:")
print(q1_data.describe())
print(q1_data.info())

# Count Null Values
null_counts = q1_data.isnull().sum()

print("Number of null values in each column:")
print(null_counts)

# Delete columns without any values
cleaned_columns = ['license', 'neighbourhood_group']
q1_data = q1_data.drop(columns = cleaned_columns)

print(q1_data)

# Fill specified columns with 0
columns_to_fill_with_zero = ['last_review', 'reviews_per_month']
q1_data[columns_to_fill_with_zero] = q1_data[columns_to_fill_with_zero].fillna(0)
null_counts = q1_data.isnull().sum()

print("Number of null values in each column:")
print(null_counts)

# Drop rows with null values
q1_data = q1_data.dropna()
null_counts = q1_data.isnull().sum()

print("Number of null values in each column:")
print(null_counts)

# Drop duplicate rows
q1_data = q1_data.drop_duplicates()

# Remove outliers from the 'price' column
q1_data = q1_data[(q1_data['price'] > 0) & (q1_data['price'] < 50000)]

# Find maximum and minimum values in column 'Price'
max_value = q1_data['price'].max()
min_value = q1_data['price'].min()

print("Maximum value in column 'Price':", max_value)
print("Minimum value in column 'Price':", min_value)

# Function to categorize price range
def categorize_price(price):
    if price < 1000:
        return 'Economy'
    elif 1000 <= price < 5000:
        return 'Standard'
    elif 5000 <= price < 15000:
        return 'Premium'
    else:
        return 'Luxury'
    
# Apply the categorize_price function to the 'price' column
q1_data['price_category'] = q1_data['price'].apply(categorize_price)

# Convert the date column to datetime format
q1_reviews['date'] = pd.to_datetime(q1_reviews['date'])

# Extract year, month, and day from the 'date' column
q1_reviews['year'] = q1_reviews['date'].dt.year
q1_reviews['month'] = q1_reviews['date'].dt.month
q1_reviews['day'] = q1_reviews['date'].dt.day

# Merge q1_reviews with q1_data on 'host_id' and 'id'
q1_reviews = q1_reviews.merge(q1_data[['id', 'host_name']], left_on='listing_id', right_on='id', how='left')
# Drop the redundant 'id' column
q1_reviews.drop(columns=['id'], inplace=True)

# Calculate average price per neighborhood
average_price_per_neighborhood = q1_data.groupby('neighbourhood')['price'].mean()
top_ten_neighborhoods = average_price_per_neighborhood.nlargest(10)
print('Top Ten Neighborhoods by Price: ', top_ten_neighborhoods)

# Calculate price distribution by room type
price_distribution_by_room_type = q1_data.groupby('room_type')['price'].describe()
print('Price Distribution: ', price_distribution_by_room_type)

# Calculate room type distribution
room_type_distribution = q1_data['room_type'].value_counts()
print('Room Type Distribution: ', room_type_distribution)

# Calculate price range distribution
price_distribution = q1_data['price_category'].value_counts()
print('Price Distribution: ', price_distribution)

# Group by 'listing_id' and 'year', then count the number of reviews for each group
reviews_by_listing_year = q1_reviews.groupby(['listing_id', 'year', 'host_name']).size().reset_index(name='number_of_reviews')
total_records = len(reviews_by_listing_year)
print('Total records:', total_records)
print('Reviews by Host and Year: ', reviews_by_listing_year)

# Filter reviews from 2023
q1_reviews_2023 = q1_reviews[q1_reviews['year'] == 2023]
reviews_by_listing_year = q1_reviews_2023.groupby(['listing_id', 'year', 'host_name']).size().reset_index(name='number_of_reviews')
total_records = len(reviews_by_listing_year)
print('Total records:', total_records)
print('Reviews by Host and Year: ', reviews_by_listing_year)

# Group by 'neighbourhood' and 'room_type'
room_type_distribution = q1_data.groupby(['neighbourhood', 'room_type']).size().unstack(fill_value=0)
print('Room Type Distribution by Neighbourhood: ', room_type_distribution)

q1_data.to_csv('Q1_2023/Q1_Result_CSV/listing_result.csv', index=False)
q1_reviews.to_csv('Q1_2023/Q1_Result_CSV/reviews_result.csv', index=False)

print('Export to CSV ready')