#!/bin/env python

import subprocess, json, sys

pipe = subprocess.Popen(['getent', 'hosts'], stdout=subprocess.PIPE)

result = {'all': {'hosts': [], 'vars': {}}}

for line in pipe.stdout.readlines():
    splitted = line.decode('utf-8').split()
    hostname = splitted[1]
    # if that's localhost, prevent this from adding
    if 'localhost' in hostname:
        continue
    # if there is a short name, prefer it
    for othername in splitted[2:]:
        if '.' not in othername:
            hostname = othername
            break
    result['all']['hosts'].append(hostname)

if len(sys.argv) == 2 and sys.argv[1] == '--list':
    print(json.dumps(result))
elif len(sys.argv) == 3 and sys.argv[1] == '--host':
    print(json.dumps({}))
else:
    print(f"use:\n\t{sys.argv[0]} --list\n\t{sys.argv[0]} --host <host>")
