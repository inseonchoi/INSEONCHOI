def schema_renamed(GOOGLE_SERVICE_ACCOUNT_FILE, file_path, bucket_name, destination_blob_name, table_id):
    import pandas as pd
    df = pd.DataFrame(pd.read_csv(file_path))
    new_columns=[]
    new_schema_info = []
    for i, column in enumerate(list(df.columns.values)):    
        if column.upper() == column.lower():
            new_columns.append("column"+str(i))  
            new_schema_info.append(str(column)+" renamed "+" column"+str(i))
        else:
            # new_column = "_".join(column.lower().split())
            new_column = "_".join(column.split())
            new_columns.append(new_column)   
    df.columns = new_columns
    new_file_path = file_path[:-len('.csv')]+"_new"+file_path[-4:]
    df.to_csv(new_file_path, index=False, mode='w')
    new_schema_info
    print("Changed schema info : {}".format(new_schema_info))
    print("----------------------------------------------------")

    from google.cloud import storage
    storage_client = storage.Client.from_service_account_json(GOOGLE_SERVICE_ACCOUNT_FILE)
    storage_client.bucket(bucket_name).blob(destination_blob_name).upload_from_filename(new_file_path)
    print(
        "File {} uploaded to {}.".format(
            new_file_path, destination_blob_name
        )
    )   
    print("----------------------------------------------------") 
    
    from google.cloud import bigquery
    client = bigquery.Client.from_service_account_json(GOOGLE_SERVICE_ACCOUNT_FILE)
    load_job = client.load_table_from_uri(
        "gs://{}/{}".format(bucket_name, destination_blob_name), table_id, 
            job_config=bigquery.LoadJobConfig(
            schema=[bigquery.SchemaField(columns, "STRING") for columns in new_columns],
            skip_leading_rows=1,
            source_format=bigquery.SourceFormat.CSV,
            write_disposition="WRITE_TRUNCATE"
        )    
    )  
    load_job.result()  
    destination_table = client.get_table(table_id)  
    print("BigQuery Loaded {} rows.".format(destination_table.num_rows))    
