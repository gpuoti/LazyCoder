from jinja2 import Template
import jsonpickle

template_sconscript = '''
#
# This describes the furious-cli's build process 
#


import pony_scons
import os
Import('env')

print('Starting build {{meta.NAME}}')
# setup the environment to use a particular compiler and target to a specific architecture
#env = Environment(MSVC_VERSION='{{meta.VC}}', TARGET_ARCH='{{meta.TARGET}}')

# details: setup a temporary build directory (can set this to a ramdisk to speedup compilation)
#env.VariantDir('build', 'source', duplicate=0)

# setup the compirer
# ------------------

output = ARGUMENTS.get('OUTPUT', 'output/{{meta.TARGET}}/Release')

env['CPPPATH'] =    [   'include','include-ext' ]

env['CXXFLAGS'] =   [   '-EHsc',                         
                        '-Od',
                        '-Gy', 
                        '-MD', 
                        
                        '-Yc{{meta.NAME}}_pch.h',   #this last option require the PCH builder set up. (does not work well with use option) 
                        '-MP' ]          #also require the compiler to use multiple processor!
        

env['CPPDEFINES'] = [   'UNICODE','_UNICODE','WIN32', 'WIN64','NDEBUG']
                  
env['LIBPATH'] = ['lib'] 
env['LIBS'] = [] 

# setup the librarian
# ----------------

# require the manifest embedded
env['WINDOWS_EMBED_MANIFEST'] = True

# setup the pch builder
env['PCHSTOP']='{{meta.NAME}}_pch.h'
pch_builder = env['PCH'] = env.PCH('{{meta.NAME}}_pch.cpp')[0]

# finally create the actual builder
builder = env.Program (   target=output+"/{{meta.NAME}}",
                          source=Glob("source/*.cpp" ) )

env.Alias('build', builder)

# the library builder depend on the precompiled header builder
env.Depends(builder, pch_builder)
'''

class project_descriptor:
    pass


def load_descriptor(meta_file):
    descriptor = project_descriptor    
    with open(meta_file) as metaf:
        descriptor = jsonpickle.decode(metaf.read())

    # setup required properties
    if 'VC' not in descriptor:
        descriptor['VC'] = '14.0'
    if 'TARGET' not in descriptor:
        descriptor['TARGET'] = 'x86'
    
    return descriptor
    

meta = load_descriptor('meta.json')

t = Template(template_sconscript)
print( t.render(meta=meta))
