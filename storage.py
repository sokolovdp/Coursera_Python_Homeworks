import argparse
import os
import tempfile
import json


def put_value(file_path: "str", key_name: "str", value: "str"):
    with open(file_path, 'r') as jsonfile:
        json_data = json.load(jsonfile)
    if key_name in json_data:
        json_data[key_name].append(value)
    else:
        json_data[key_name] = [value, ]
    with open(file_path, 'w') as jsonfile:
        json.dump(json_data, jsonfile)


def get_value(file_path: "str", key_name: "str") -> "list":
    with open(file_path, 'r') as jsonfile:
        json_data = json.load(jsonfile)
    return json_data.get(key_name, [])


if __name__ == '__main__':
    ap = argparse.ArgumentParser("key:value storage")
    ap.add_argument('--key', dest='key_name', action='store', required=True)
    ap.add_argument('--val', dest='value', action='store')
    ap.add_argument('--clear', dest='clean', action='store_true')

    args = ap.parse_args()

    storage_path = os.path.join(tempfile.gettempdir(), 'storage.data')
    # storage_path = 'storage.txt'
    if not os.path.isfile(storage_path) or args.clean:
        with open(storage_path, 'w') as json_file:
            json.dump({}, json_file)

    if args.value:
        put_value(storage_path, args.key_name, args.value)
    else:
        print(", ".join(get_value(storage_path, args.key_name)))
