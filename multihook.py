#!/usr/bin/env python

import sys
import subprocess

HOOKS = [
    #['/path/to/hook-script'], 
    #['/path/to/hook-script', 'arg1', 'arg2'],
]

if __name__ == '__main__':
    data = sys.stdin.read()
    
    for hook in HOOKS:
        p = subprocess.Popen(hook, stdin=subprocess.PIPE,
                             stdout=subprocess.PIPE)
        p.stdin.write(data)
        p.stdin.close()

        sys.stdout.write(p.stdout.read())
