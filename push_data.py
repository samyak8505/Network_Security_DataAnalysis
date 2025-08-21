import os
import sys
import json
import certifi
import pandas as pd
import numpy as np
import pymongo

from dotenv import load_dotenv
from networksecurity.exception.exception import NetworkSecurityException
from networksecurity.logging.logger import logging

# Load environment variables
load_dotenv()
MONGO_DB_URL = os.getenv("MONGO_DB_URL")
print("MongoDB URL Loaded ✅")

# TLS certificate
ca = certifi.where()


class NetworkDataExtract:
    def __init__(self):
        try:
            pass
        except Exception as e:
            raise NetworkSecurityException(e, sys)

    def csv_to_json_convertor(self, file_path):
        """Reads CSV and converts to list of JSON records"""
        try:
            data = pd.read_csv(file_path)
            data.reset_index(drop=True, inplace=True)
            records = list(json.loads(data.T.to_json()).values())
            return records
        except Exception as e:
            raise NetworkSecurityException(e, sys)

    def insert_data_mongodb(self, records, database, collection):
        """Inserts records into MongoDB Atlas"""
        try:
            self.database = database
            self.collection = collection
            self.records = records

            # Connect with TLS + certifi
            self.mongo_client = pymongo.MongoClient(
                MONGO_DB_URL,
                tls=True,
                tlsCAFile=ca
            )

            self.database = self.mongo_client[self.database]
            self.collection = self.database[self.collection]

            self.collection.insert_many(self.records)
            return len(self.records)

        except Exception as e:
            raise NetworkSecurityException(e, sys)


if __name__ == "__main__":
    FILE_PATH = "Network_Data/phisingData.csv"  # use forward slash for cross-platform
    DATABASE = "NETWORK_DB"
    COLLECTION = "SAM"

    networkobj = NetworkDataExtract()

    # Convert CSV to JSON
    records = networkobj.csv_to_json_convertor(file_path=FILE_PATH)

    # Insert into MongoDB
    no_of_records = networkobj.insert_data_mongodb(records, DATABASE, COLLECTION)
    print(f"✅ Inserted {no_of_records} records into {DATABASE}.{COLLECTION}")
