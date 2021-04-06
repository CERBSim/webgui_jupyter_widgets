// Copyright (c) CERBSim
// Distributed under the terms of the LGPLv2.1 License.

import { Application, IPlugin } from '@phosphor/application';

import { Widget } from '@phosphor/widgets';

import { IJupyterWidgetRegistry } from '@jupyter-widgets/base';

import * as widgetExports from './widget';

import { MODULE_NAME, MODULE_VERSION } from './version';

const EXTENSION_ID = 'webgui_jupyter_widgets:plugin';

/**
 * The Webgui plugin.
 */
const webguiPlugin: IPlugin<Application<Widget>, void> = ({
  id: EXTENSION_ID,
  requires: [IJupyterWidgetRegistry],
  activate: activateWidgetExtension,
  autoStart: true,
} as unknown) as IPlugin<Application<Widget>, void>;
// the "as unknown as ..." typecast above is solely to support JupyterLab 1
// and 2 in the same codebase and should be removed when we migrate to Lumino.

export default webguiPlugin;

/**
 * Activate the widget extension.
 */
function activateWidgetExtension(
  app: Application<Widget>,
  registry: IJupyterWidgetRegistry
): void {
  registry.registerWidget({
    name: MODULE_NAME,
    version: MODULE_VERSION,
    exports: widgetExports,
  });
}
