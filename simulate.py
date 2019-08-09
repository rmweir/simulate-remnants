import sys
import rancher
import random
import string

def random_str():
    return ''.join([random.choice(string.ascii_letters + string.digits) for n in range(8)])

cluster_id = sys.argv[1]
access = sys.argv[2]
secret = sys.argv[3]
url = sys.argv[4]

project_name = "p-" + random_str()

client = rancher.Client(url='https://bf57de7d.ngrok.io/v3',
                        access_key=access,
                        secret_key=secret)

p = client.create_project(name="testing", clusterId=cluster_id)
print('project id: ' + p.id)
client.delete(p)

