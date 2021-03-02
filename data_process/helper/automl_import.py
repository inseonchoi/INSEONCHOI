def AutoML_import(PROJECT_ID, REGION, display_name, import_path, GOOGLE_SERVICE_ACCOUNT_FILE):
    from google.cloud import automl_v1p1beta
    from google.api_core import exceptions
    import google.api_core.operation

    import logging
    from google.cloud import bigquery
    from google.cloud import storage
    from google.cloud import automl_v1p1beta
    from google.cloud.automl_v1p1beta.proto import dataset_pb2
    from google.cloud.automl_v1p1beta.proto import operations_pb2 as proto_operations_pb2
    from google.api_core import exceptions
    import google.api_core.operation

    AUTOML_CLIENT = automl_v1p1beta.AutoMlClient.from_service_account_file(GOOGLE_SERVICE_ACCOUNT_FILE)
    AUTOML_LOCATION_PATH = AUTOML_CLIENT.location_path(PROJECT_ID, REGION)
    create_dataset_operation = AUTOML_CLIENT.create_dataset(
        AUTOML_LOCATION_PATH,
        {
            "display_name": display_name,
            "tables_dataset_metadata": {"tables_dataset_type": "FORECASTING"}
        }
    )
    create_dataset_api_operation = google.api_core.operation.from_gapic(
            create_dataset_operation,
            AUTOML_CLIENT.transport._operations_client,
            dataset_pb2.Dataset,
            metadata_type=proto_operations_pb2.OperationMetadata,
        )

    dataset = create_dataset_api_operation.result()
    dataset_name = dataset.name
    logging.info("creating dataset ({}) is completed\n({})".format(display_name, dataset_name))

    logging.info("importing dataset ({}) is started".format(display_name))

    input_config = {
        'bigquery_source': {
            'input_uri': import_path
        }
    }
    import_data_response = AUTOML_CLIENT.import_data(dataset_name, input_config)
    logging.info("Dataset import operation: {}".format(import_data_response.operation))
    import_data_result = import_data_response.result()

    logging.info("importing dataset ({}) is completed".format(display_name))
