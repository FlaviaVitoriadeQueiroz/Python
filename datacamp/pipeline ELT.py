def transform (source_table, target_table):
    data_warehouse.run_sql("""
        CREATE TABLE {target_table} AS
            SELECT
                <field-name>, <field-name>,
            FROM {source_table};
    """)
#Semelhante aos pipelines ETL, chame as funções de extração, carregamento e transformação.

extracted_data = extract(file_name="raw_data.csv")
load(data_frame=extracted_data, table_name="raw_data")
transform (source_table="raw_data", target_table="cleaned_data")