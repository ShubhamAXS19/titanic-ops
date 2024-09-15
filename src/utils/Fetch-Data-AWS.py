import os
import boto3

def download_from_s3(bucket_name, s3_key, local_dir):
    # Create an S3 client
    s3 = boto3.client('s3')
    
    # Local file path where the data will be saved
    local_file_path = os.path.join(local_dir, s3_key.split('/')[-1])
    
    # Download file from S3 bucket
    print(f"Downloading {s3_key} from S3 bucket {bucket_name} to {local_file_path}")
    s3.download_file(bucket_name, s3_key, local_file_path)
    
    print(f"Download completed: {local_file_path}")
    return local_file_path


if __name__ == "__main__":
    # Define bucket, S3 path, and local directory
    BUCKET_NAME = "titanic-ops"
    S3_KEY = "path/to/your/dataset.csv"  # Change to your actual key
    LOCAL_DIR = "./data/raw"  # Change to your desired local directory
    
    # Ensure local directory exists
    if not os.path.exists(LOCAL_DIR):
        os.makedirs(LOCAL_DIR)
    
    # Download data
    download_from_s3(BUCKET_NAME, S3_KEY, LOCAL_DIR)
