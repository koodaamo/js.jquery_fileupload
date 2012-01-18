from fanstatic import Library, Resource, Group
from js.jquery import jquery
from js.jqueryui import jqueryui

library = Library("fileupload", "resource_library")

ui_css = Resource(library, "jquery.fileupload-ui.css")
js = Resource(library, "jquery.fileupload.js", depends=[jquery])
ui_js = Resource(library, "jquery.fileupload-ui.js", depends=[js, ui_css, jqueryui])
transport = Resource(library, "jquery.iframe-transport.js")

fileupload_resources = Group([ui_css, ui_js, js, transport])
