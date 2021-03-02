name = 'nuke_colourtools'

version='1.0.4'

authors = ['jed smith']

help = 'github.com/jedypod'

requires = [
    'nuke-9+',
]

def commands():
    env.NUKE_PATH.append('{root}/nuke')
    env.PYTHONPATH.append('{root}/nuke/Python')
    env.NUKE_COLOURTOOLS_IMAGES.set('{root}/images')

build_command = """
prefix=$REZ_BUILD_INSTALL_PATH/nuke
mkdir -p $prefix
cp -a {root}/blink $prefix
cp -a {root}/python $prefix/Python
cp -a {root}/toolsets $prefix/ToolSets
cp -a {root}/images $prefix
cp {root}/*.md $prefix
"""
