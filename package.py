name = 'nuke_colortools'

version='21.7.13.0'

authors = ['jed smith']

help = 'github.com/jedypod/nuke-colortools'

requires = [
    'nuke-9+',
]

def commands():
    env.NUKE_PATH.append('{root}/nuke')
    env.PYTHONPATH.append('{root}/nuke/Python')

build_command = """
prefix=$REZ_BUILD_INSTALL_PATH/nuke
mkdir -p $prefix
cp -a {root}/blink $prefix
cp -a {root}/python $prefix/Python
cp -a {root}/toolsets $prefix/ToolSets
cp {root}/*.md $prefix
cp {root}/LICENSE.md $prefix
"""
