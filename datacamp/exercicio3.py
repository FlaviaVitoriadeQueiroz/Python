def load(data_frame, file_name):
    # Save the DataFrame to a CSV
    data_frame.to_csv(file_name, index=False)
    print(f"Successfully loaded data to {file_name}")

extracted_data = extract(file_name="raw_data.csv")

# Transform extracted_data using transform() function
transformed_data = transform(data_frame=extracted_data)

# Load transformed_data to the file transformed_data.csv
load(data_frame=transformed_data, file_name="transformed_data.csv")
