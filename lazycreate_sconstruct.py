from jinja2 import Template
import jsonpickle

template_sconstruct = '''
env = Environment(MSVC_VERSION='{{meta.VC}}', TARGET_ARCH='{{meta.TARGET}}')
test_env = Environment(MSVC_VERSION='{{meta.VC}}', TARGET_ARCH='{{meta.TARGET}}')
# details: setup a temporary build directory (can set this to a ramdisk to speedup compilation)
env.VariantDir('build', 'source', duplicate=True)

SConscript(['Sconscript'], exports='env')
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

t = Template(template_sconstruct)
print( t.render(meta=meta))