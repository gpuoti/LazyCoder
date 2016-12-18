#!/usr/bin/env python

from setuptools import setup

setup(	name='LazyCoder',
        version='0.0.1',
        description='Simple tools for lazy programmers. This set of scripts simplify projects setup and manteinence.',
        author='Giuseppe Puoti',
        author_email='giuseppe.puoti@gmail.com',
        url='',
        
        py_modules=[
             'lazycreate_cpp_project',
             'lazycreate_sconscript_4_cpp',
             'lazycreate_sconstruct'
            # list them here when you add any other modules!
            ],
            
        scripts = ['lazycreate_cpp_project.py', 
                    'lazycreate_sconscript_4_cpp.py',
                    'lazycreate_sconstruct.py']  
)