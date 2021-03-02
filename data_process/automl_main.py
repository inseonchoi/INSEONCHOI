from helper.automl_import import AutoML_import

PROJECT_ID = "yunsu-stxengine-support-210105"
REGION = "us-central1"
display_name = "ORDER_2"
import_path = "bq://yunsu-stxengine-support-210105.IS_DATASET.ORDER"
GOOGLE_SERVICE_ACCOUNT_FILE = "/Users/mz02-inseonc/Downloads/yunsu-stxengine-support-210105-62cb94bf90b5.json"


if __name__ == "__main__":
    AutoML_import(
        PROJECT_ID,
        REGION,
        display_name,
        import_path,
        GOOGLE_SERVICE_ACCOUNT_FILE
    )
