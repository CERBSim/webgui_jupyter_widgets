# export DEV_BUILD=1
set -e
# pip uninstall -y webgui_jupyter_widgets
rm -f dist/*.whl
# rm -rf webgui/node_modules
python setup.py bdist_wheel
pip install dist/*.whl 
jupyter nbextension install --user --py webgui_jupyter_widgets
jupyter nbextension enable webgui_jupyter_widgets --user --py

