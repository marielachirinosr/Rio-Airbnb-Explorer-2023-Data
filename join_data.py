import pandas as pd

q1_data = pd.read_csv('Q1_2023/Q1_Result_CSV/listing_result_q1.csv')
q1_reviews = pd.read_csv('Q1_2023/Q1_Result_CSV/reviews_result_q1.csv')

q2_data = pd.read_csv('Q2_2023/Q2_Result_CSV/listing_result_q2.csv')
q2_reviews = pd.read_csv('Q2_2023/Q2_Result_CSV/reviews_result_q2.csv')

q3_data = pd.read_csv('Q3_2023/Q3_Result_CSV/listing_result_q3.csv')
q3_reviews = pd.read_csv('Q3_2023/Q3_Result_CSV/reviews_result_q3.csv')

q4_data = pd.read_csv('Q4_2023/Q4_Result_CSV/listing_result_q4.csv')
q4_reviews = pd.read_csv('Q4_2023/Q4_Result_CSV/reviews_result_q4.csv')

concatenated_df = pd.concat([q1_data, q2_data, q3_data, q4_data])
concatenated_df_2 = pd.concat([q1_reviews, q2_reviews, q3_reviews, q4_reviews])

concatenated_df.to_csv('./listing_result.csv', index=False)
concatenated_df_2.to_csv('./reviews_result.csv', index=False)