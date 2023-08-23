export DEV_BUILD=1
set -e
# pip uninstall -y webgui_jupyter_widgets
rm -f dist/*.whl
# rm -rf webgui/node_modules
rm -f build/lib/webgui_jupyter_widgets/labextension/static/*
make -j4 -C em_ngs/dist/
python3 setup.py bdist_wheel
python3 -m pip install --force-reinstall dist/*.whl 
# jupyter nbextension install --user --py webgui_jupyter_widgets
# jupyter nbextension enable webgui_jupyter_widgets --user --py

