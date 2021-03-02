from helper.schema_rename import schema_renamed

GOOGLE_SERVICE_ACCOUNT_FILE = "/Users/mz02-inseonc/Downloads/yunsu-stxengine-support-210105-62cb94bf90b5.json"
file_path = "./ORDER.csv"
bucket_name = "inseon-test"
destination_blob_name = "ORDER.csv"
table_id = "sampling.ORDER"



if __name__ == "__main__":
    schema_renamed(
        GOOGLE_SERVICE_ACCOUNT_FILE, 
        file_path, 
        bucket_name, 
        destination_blob_name, 
        table_id)



# 터미널 설치
#   pip install --upgrade google-cloud-storage
#   pip install --upgrade google-cloud-bigquery

# 수주.tsv의 경우 utf-16으로 연 후 utf-8로 저장하니 안깨졌음... (ㅠㅠ)

# Config 정보
# 1. Service Account
# 2. UTF-8로 인코딩된 로컬 CSV 파일 (-> 스카미 수정된 파일은 기존 파일명 끝에 new가 붙어서 생성됨)
# 3. 버킷 이름
# 4. 버킷에 저장할 이름 
# 5. 빅쿼리 데이터셋, 테이블 이름
