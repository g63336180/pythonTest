#!/usr/local/bin/python3

from string import Template
s = Template('$x, glorious $x!')
s.substitute(x='slurm')
s.render()