#!/usr/bin/env python3
""" that provides some stats about Nginx logs stored in MongoDB
"""

from pymongo import MongoClient


if __name__ == '__main__':
    stats = MongoClient('mongodb://localhost:27017').logs.nginx
    print(f'{stats.count_documents({})} logs')
    print('Methods:')
    print(f'\tmethod GET: {stats.count_documents({"method": "GET"})}')
    print(f'\tmethod POST: {stats.count_documents({"method": "POST"})}')
    print(f'\tmethod PUT: {stats.count_documents({"method": "PUT"})}')
    print(f'\tmethod PATCH: {stats.count_documents({"method": "PATCH"})}')
    print(f'\tmethod DELETE: {stats.count_documents({"method": "DELETE"})}')
    print(f'{stats.count_documents({"path": "/status"})} status check')
