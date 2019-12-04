from pymongo import MongoClient
from os import environ


def main():
    try:
        client = MongoClient(environ.get('MONGO_URI', 'mongodb://localhost:27017/'))
        print('Successfully connected to mongo')
        print('Database names:', client.list_database_names())
    except:
        print('Error while connecting to mongo')


if __name__ == '__main__':
    main()
