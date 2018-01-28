import pandas as pd
import json
import os
import sys
import datetime
import time
import string

def clean_json(item_json):
    valid_chars = string.ascii_letters + string.digits + "_"

    def replace(key):
        return ''.join([x if x in valid_chars else '_' for x in key]).lower()

    def valid_key(key):
        return key == replace(key)

    for key in item_json:
        if not valid_key(key):
            item_json[replace(key)] = item_json[key]
            item_json.pop(key, None)

    return item_json

def get_timestamp():
    return datetime.datetime.now().isoformat()

def save_json(response_json, fileName, args):
    with open(fileName, 'w') as file:
        for item_json in response_json:
            if args.timestamp:
                item_json['_timestamp'] = get_timestamp()

            if args.clean:
                item_json = clean_json(item_json)

            json.dump(item_json, file)
            file.write(os.linesep)

def save_csv(response_json, fileName, args):
    df = pd.DataFrame(response_json)
    if args.timestamp:
        df = df.assign(_timestamp = timestamp_str)

    df.to_csv(fileName, index=False, header=not args.header, decimal='.', sep= args.sep, encoding='utf-8')
