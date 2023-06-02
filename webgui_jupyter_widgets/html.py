
def encodeData( data, dtype=None, encoding='b64' ):
    import numpy as np
    from base64 import b64encode
    dtype = dtype or data.dtype
    values = np.array(data.flatten(), dtype=dtype)
    if encoding=='b64':
        return b64encode(values).decode("ascii")
    elif encoding=='binary':
        return values.tobytes()
    else:
        raise RuntimeError("unknown encoding" + str(encoding))

_html_template = None

def getHTML():
    from os.path import dirname, join
    global _html_template;
    if _html_template is None:
        code = open(join(dirname(__file__), "js", "webgui.js")).read()
        _html_template = """
<!DOCTYPE html>
<html>
    <head>
        <title>NGSolve WebGUI</title>
        <meta name='viewport' content='width=device-width, user-scalable=no'/>
        <style>
            body{
                margin:0;
                overflow:hidden;
            }
            canvas{
                cursor:grab;
                cursor:-webkit-grab;
                cursor:-moz-grab;
            }
            canvas:active{
                cursor:grabbing;
                cursor:-webkit-grabbing;
                cursor:-moz-grabbing;
            }
        </style>
    </head>
    <body>
          <script>
            {{webgui_code}}
          </script>
          <script>
            {render}
            const scene = new webgui.Scene();
            scene.init(document.body, render_data, {preserveDrawingBuffer: false});
          </script>
    </body>
</html>
""".replace("{{webgui_code}}", code)
    return _html_template

def getScreenshotHTML():
    return getHTML().replace("preserveDrawingBuffer: false", "preserveDrawingBuffer: true")

def GenerateHTML(data, filename=None, template=None):
    if template is None:
        template = getHTML()
    import json
    data = json.dumps(data)

    html = template.replace('{data}', data )
    jscode = "var render_data = {}\n".format(data)
    html = html.replace('{render}', jscode )

    if filename is not None:
        open(filename,'w').write( html )
    return html

def MakeScreenshot(data, filename, width=1200, height=600):
    import os, time
    html_file = filename+".html"
    GenerateHTML(data, filename=html_file, template=getScreenshotHTML())

    # start headless browser to render html
    from selenium import webdriver
    from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

    options = webdriver.ChromeOptions()
    options.add_argument('--headless')
    options.add_argument('--no-sandbox')
    # https://stackoverflow.com/questions/54297559/getting-cannot-activate-web-view
    options.add_argument("--disable-infobars")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--disable-browser-side-navigation")
    #options.add_argument("--disable-gpu")
    options.add_argument("--disable-features=VizDisplayCompositor")

    options.add_argument('window-size=1200x600')


    driver = webdriver.Chrome(options=options)
    fpath = 'file://'+os.path.join(os.path.abspath('.'), html_file)
    driver.get(fpath)
    driver.implicitly_wait(10)

    time.sleep(2)
    driver.get_screenshot_as_file(filename)
    os.remove(html_file)


