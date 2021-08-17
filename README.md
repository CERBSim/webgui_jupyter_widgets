
# webgui_jupyter_widgets

[![Build Status](https://travis-ci.org/CERBSim/webgui_jupyter_widgets.svg?branch=master)](https://travis-ci.org/CERBSim/webgui_jupyter_widgets)
[![codecov](https://codecov.io/gh/CERBSim/webgui_jupyter_widgets/branch/master/graph/badge.svg)](https://codecov.io/gh/CERBSim/webgui_jupyter_widgets)


Jupyter widgetds library for webgui js visualization library'

## Installation

You can install using `pip`:

```bash
pip install webgui_jupyter_widgets
```

If you are using Jupyter Notebook 5.2 or earlier, you may also need to enable
the nbextension:
```bash
jupyter nbextension enable --py [--sys-prefix|--user|--system] webgui_jupyter_widgets
```

## Development Installation

Create a dev environment:
```bash
conda create -n webgui_jupyter_widgets-dev -c conda-forge nodejs yarn python jupyterlab
conda activate webgui_jupyter_widgets-dev
```

Install the python. This will also build the TS package.
```bash
pip install -e ".[test, examples]"
```

When developing your extensions, you need to manually enable your extensions with the
notebook / lab frontend. For lab, this is done by the command:

```
jupyter labextension develop --overwrite .
yarn run build
```

For classic notebook, you need to run:

```
jupyter nbextension install --sys-prefix --symlink --overwrite --py webgui_jupyter_widgets
jupyter nbextension enable --sys-prefix --py webgui_jupyter_widgets
```

Note that the `--symlink` flag doesn't work on Windows, so you will here have to run
the `install` command every time that you rebuild your extension. For certain installations
you might also need another flag instead of `--sys-prefix`, but we won't cover the meaning
of those flags here.

### How to see your changes
#### Typescript:
If you use JupyterLab to develop then you can watch the source directory and run JupyterLab at the same time in different
terminals to watch for changes in the extension's source and automatically rebuild the widget.

```bash
# Watch the source directory in one terminal, automatically rebuilding when needed
yarn run watch
# Run JupyterLab in another terminal
jupyter lab
```

After a change wait for the build to finish and then refresh your browser and the changes should take effect.

#### Python:
If you make a change to the python code then you will need to restart the notebook kernel to have it take effect.


# Build with development version of webgui
```code
# initial setup
git clone https://github.com/CERBSim/webgui_jupyter_widgets.git
cd webgui_jupyter_widgets
git submodule update --init --recursive
pip install --user .
jupyter nbextension install --user --py webgui_jupyter_widgets

# build dev version of webgui
cd webgui
git checkout main
git pull
cd ..
pip install --user .
```
