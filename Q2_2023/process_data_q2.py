import pandas as pd 

# Read CSV
q2_data = pd.read_csv('Q2_2023/q2_listings.csv')
q2_reviews = pd.read_csv('Q2_2023/q2_reviews.csv')

# Summary Information
print("Data Information:")
print(q2_data.describe())
print(q2_data.info())

# Count Null Values
null_counts = q2_data.isnull().sum()

print("Number of null values in each column:")
print(null_counts)

# Delete columns without any values
cleaned_columns = ['license', 'neighbourhood_group']
q2_data = q2_data.drop(columns = cleaned_columns)

print(q2_data)

# Fill specified columns with 0
columns_to_fill_with_zero = ['last_review', 'reviews_per_month']
q2_data[columns_to_fill_with_zero] = q2_data[columns_to_fill_with_zero].fillna(0)
null_counts = q2_data.isnull().sum()

print("Number of null values in each column:")
print(null_counts)

# Drop rows with null values
q2_data = q2_data.dropna()
null_counts = q2_data.isnull().sum()

print("Number of null values in each column:")
print(null_counts)

# Drop duplicate rows
q2_data = q2_data.drop_duplicates()

# Remove outliers from the 'price' column
q2_data = q2_data[(q2_data['price'] > 0) & (q2_data['price'] < 50000)]

# Find maximum and minimum values in column 'Price'
max_value = q2_data['price'].max()
min_value = q2_data['price'].min()

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
q2_data['price_category'] = q2_data['price'].apply(categorize_price)

# Convert the date column to datetime format
q2_reviews['date'] = pd.to_datetime(q2_reviews['date'])

# Extract year, month, and day from the 'date' column
q2_reviews['year'] = q2_reviews['date'].dt.year
q2_reviews['month'] = q2_reviews['date'].dt.month
q2_reviews['day'] = q2_reviews['date'].dt.day

# Merge q2_reviews with q2_data on 'host_id' and 'id'
q2_reviews = q2_reviews.merge(q2_data[['id', 'host_name']], left_on='listing_id', right_on='id', how='left')
# Drop the redundant 'id' column
q2_reviews.drop(columns=['id'], inplace=True)

# Calculate average price per neighborhood
average_price_per_neighborhood = q2_data.groupby('neighbourhood')['price'].mean()
top_ten_neighborhoods = average_price_per_neighborhood.nlargest(10)
print('Top Ten Neighborhoods by Price: ', top_ten_neighborhoods)

# Calculate price distribution by room type
price_distribution_by_room_type = q2_data.groupby('room_type')['price'].describe()
print('Price Distribution: ', price_distribution_by_room_type)

# Calculate room type distribution
room_type_distribution = q2_data['room_type'].value_counts()
print('Room Type Distribution: ', room_type_distribution)

# Calculate price range distribution
price_distribution = q2_data['price_category'].value_counts()
print('Price Distribution: ', price_distribution)

# Group by 'listing_id' and 'year', then count the number of reviews for each group
reviews_by_listing_year = q2_reviews.groupby(['listing_id', 'year', 'host_name']).size().reset_index(name='number_of_reviews')
total_records = len(reviews_by_listing_year)
print('Total records:', total_records)
print('Reviews by Host and Year: ', reviews_by_listing_year)

# Filter reviews from 2023
q2_reviews_2023 = q2_reviews[q2_reviews['year'] == 2023]
reviews_by_listing_year = q2_reviews_2023.groupby(['listing_id', 'year', 'host_name']).size().reset_index(name='number_of_reviews')
total_records = len(reviews_by_listing_year)
print('Total records:', total_records)
print('Reviews by Host and Year: ', reviews_by_listing_year)

# Group by 'neighbourhood' and 'room_type'
room_type_distribution = q2_data.groupby(['neighbourhood', 'room_type']).size().unstack(fill_value=0)
print('Room Type Distribution by Neighbourhood: ', room_type_distribution)

q2_data.to_csv('Q2_2023/Q2_Result_CSV/listing_result_q2.csv', index=False)
q2_reviews.to_csv('Q2_2023/Q2_Result_CSV/reviews_result_q2.csv', index=False)

print('Export to CSV ready')