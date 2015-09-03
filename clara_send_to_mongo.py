__author__ = 'kurtosis'

import json
import pymongo
from datetime import datetime as dt
import argparse


def read_arguments():

    parser = argparse.ArgumentParser()

    parser.add_argument('clara_file', help='json file with clara clustering in the format of clara.py')
    parser.add_argument('clnames', default='clnames', help='json file with labeled cluster names to be showed in UI')
    parser.add_argument('-dev', '--dev', action='store_true', default=False)

    args = parser.parse_args()
    return args


if __name__ == '__main__':

    args = read_arguments()
    clnames = json.load(open(args.clnames, 'r'))
    clara_address = args.clara_file   # 'clara_json_version_110438_one'
    clara_clustering = json.load(open(clara_address, 'r'))[2]

    if args.dev:
        host = 'dmp-sandbox.dev.de.facetz.net'
    else:
        host = 'mongo.facetz.net'

    mongo = pymongo.MongoClient(host)
    col = mongo.dmp.domain_clusters
    date = dt.today().strftime('%Y-%m-%d')

    clusters_to_mongo = []
    for i, cl_medoid in enumerate(clnames):
        clusters_to_mongo.append({'domains': clara_clustering[cl_medoid],
                                  'name': clnames[cl_medoid],
                                  'number': i})

    col.update_one({'date': date},
                   {'$set': {'clusters': clusters_to_mongo}},
                   upsert=True)
