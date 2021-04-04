// Copyright (c) CERBSim
// Distributed under the terms of the LGPLv2.1 License.

import {
  DOMWidgetModel,
  DOMWidgetView,
  ISerializers,
} from '@jupyter-widgets/base';

import {
  Scene
} from 'webgui';


import { MODULE_NAME, MODULE_VERSION } from './version';

// Import the CSS
import '../css/widget.css';

export class WebguiModel extends DOMWidgetModel {
  defaults() {
    return {
      ...super.defaults(),
      _model_name: WebguiModel.model_name,
      _model_module: WebguiModel.model_module,
      _model_module_version: WebguiModel.model_module_version,
      _view_name: WebguiModel.view_name,
      _view_module: WebguiModel.view_module,
      _view_module_version: WebguiModel.view_module_version,
      value: 'Hello World',
    };
  }

  static serializers: ISerializers = {
    ...DOMWidgetModel.serializers,
    // Add any extra serializers here
  };

  static model_name = 'WebguiModel';
  static model_module = MODULE_NAME;
  static model_module_version = MODULE_VERSION;
  static view_name = 'WebguiView'; // Set to null if no view
  static view_module = MODULE_NAME; // Set to null if no view
  static view_module_version = MODULE_VERSION;
}

export class WebguiView extends DOMWidgetView {
  scene: Scene;

  render() {
    this.el.classList.add('webgui-widget');

    console.log("Render NGSView");
    let render_data = this.model.get("value");
    console.log("render data", render_data);
    this.scene = new Scene();
    let container = document.createElement( 'div' );
    container.setAttribute("style", "height: 50vw; width: 100vw;");
    this.el.appendChild(container);
    setTimeout(()=> {
      this.scene.init(container, render_data);
      this.scene.render();
    } , 0);
    this.model.on('change:value', this.value_changed, this);
  }

  value_changed() {
    let render_data = this.model.get("value");
    this.scene.updateRenderData(render_data);
  }
}
