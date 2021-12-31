#!/usr/bin/env python3

import glob
import random

from os.path import isfile


file_list = [
    file for file in glob.glob("output/*.txt")
    if isfile(file)
]

contents = ['', 
'All work and no play makes Jack a dull boy',
'''All work and no play makes Jack a dull boy
All work and no play makes Jack a dull boy''',
'''All work and no play makes Jack a dull boy
All work and no play makes Jack a dull boy
All work and no play makes Jack a dull boy''',
'''All work and no play makes Jack a dull boy

All work and no play makes Jack a dull boy

All work and no play makes Jack a dull boy''',

'''All work and no play makes Jack a dull boy
All work and no play makes Jack a dull boy

All work and no play makes Jack a dull boy

All work and no play makes Jack a dull boy
All work and no play makes Jack a dull boy''',
'''All work and no play makes Jack a dull boy

All work and no play makes Jack a dull boy
All work and no play makes Jack a dull boy
All work and no play makes Jack a dull boy

All work and no play makes Jack a dull boy''',
            ] 


file_list.sort()
random.shuffle(file_list)

for file in file_list:
    print(file)
    with open(file) as _input:
        contents.append(_input.read())

output_path = '/Users/alans/workshop/jacktorrance.dev/components/Pages.js'

with open(output_path, 'w') as _output:
    _output.write('export const pages = [`')
    _output.write("`\n,`".join(contents))
    _output.write('`]')

