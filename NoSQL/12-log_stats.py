#!/usr/bin/env python3
"""function that provides stats about Nginx logs stored in MongoDB"""
from pymongo import MongoClient


if __name__ == "__main__":
    CL = MongoClient("mongodb://localhost:27017")
    DB = CL.logs
    NS = DB.nginx
    METS = ["GET", "POST", "PUT", "PATCH", "DELETE"]
    TL = NS.count_documents({})
    
    print(f"{TL} logs")
    print("Methods:")
    for MET in METS:
        method_count = NS.count_documents({"method": MET})
        print(f"\tmethod {MET}: {method_count}")

    SCC = NS.count_documents({"method": "GET", "path": "/status"})
    print(f"{SCC} status check")
