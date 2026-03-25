# Extract data from the raw_data.csv file
raw_data = extract(file_name="raw_data.csv")

# Load the extracted_data to the raw_data table
load(data_frame=raw_data, table_name="raw_data")

# Transform data in the raw_data table
transform(
  source_table="raw_data", 
  target_table="cleaned_data"
)