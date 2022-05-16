from fileinput import filename
from unicodedata import name
import requests
from zipfile import ZipFile
import pandas

def download(file_path, local_path):
    response = requests.get(file_path, local_path)
    with open(local_path, "wb") as f:
        f.write(response.content)

def zip_file(file_path):
    with ZipFile(file_path, mode="r") as f:
        file_names = f.namelist()
        csv_file_paths = []
        for filename in file_names:
            csv_file_paths.append(f.extract(filename))
            print(csv_file_paths)
            return csv_file_paths

    

if __name__ == "__main__":
    #file_path ='https://assets.datacamp.com/production/repositories/5899/datasets/19d6cf619d6a771314f0eb489262a31f89c424c2/ppr-all.zip'
    local_path = f"/Users/yanan/Desktop/ETL/data/PPR-ALL.zip"
    
    download(file_path, local_path)
    csv_file_paths = zip_file(file_path=local_path)


    
