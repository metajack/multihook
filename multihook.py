#!/usr/bin/env python

import sys
import subprocess

HOOKS = [
    #['/path/to/hook-script'], 
    #['/path/to/hook-script', 'arg1', 'arg2'],
]

if __name__ == '__main__':
    data = sys.stdin.read()
    
    procs=[]
    for hook in HOOKS:
        p = subprocess.Popen(hook, stdin=subprocess.PIPE,
                             stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        p.stdin.write(data)
        p.stdin.close()

        sys.stderr.write(p.stderr.read())
        sys.stdout.write(p.stdout.read())
        procs.append(p)

    rv = 0
    for p in procs:
        p.wait()
        if p.returncode != 0:
            rv = p.returncode

    exit(rv)
