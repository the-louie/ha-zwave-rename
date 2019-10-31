from requests import get, post
import sys
import json

def usage():
    print("Usage: {} <node id> <new name>".format(sys.argv[0]))
    sys.exit(1)
def conf(key):
    print("Missing {} in config.json".format(key))
    sys.exit(1)

def rename(node_id, name):
    print("Renameing node {} to '{}'".format(node_id, name))
    url = '{}/api/services/zwave/rename_node'.format(HOST)
    headers = {
                'Authorization': 'Bearer {}'.format(TOKEN),
                'content-type': 'application/json'}

    data = {
        "node_id": node_id,
        "name": name,
        "update_ids": True
    }
    response = post(url, data=json.dumps(data), headers=headers)
    if response.status_code != 200:
        raise ValueError("Unable to pull the data from: %s" % url, response.text)



with open('config.json') as json_data_file:
    data = json.load(json_data_file)

TOKEN = data.get('token')
HOST = data.get('host')
if TOKEN is None:
    conf("token")
if HOST is None:
    conf("host")

if len(sys.argv) < 2:
    usage()

try:
    node_id = int(sys.argv[1])
except (TypeError, ValueError):
    usage()


name = sys.argv[2]

rename(node_id, name)
