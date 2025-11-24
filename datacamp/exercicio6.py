def extract(file_name):
  return pd.read_csv(file_name)

def transform(data_frame):
  # Filter the data_frame to only incude a subset of columns
  return data_frame.loc[:, ["industry_name", "number_of_firms"]]
