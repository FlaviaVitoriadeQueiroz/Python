# Extract data from the raw_data.csv file
extracted_data = extract(file_name="raw_data.csv")

# Transform the extracted_data
transformed_data = transform(data_frame=extracted_data)

# Load the transformed_data to cleaned_data.csv
load(data_frame=transformed_data, target_table="cleaned_data")