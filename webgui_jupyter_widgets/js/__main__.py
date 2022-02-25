import sys
from os.path import join, dirname

output_path = sys.argv[1]
current_path = dirname(__file__)

for f in 'webgui.js', 'webgui_jupyter_widgets.js':
    open(join(output_path, f), 'w').write( open(join(current_path, f)).read() )

