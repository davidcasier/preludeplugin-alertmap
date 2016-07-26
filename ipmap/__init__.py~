from prewikka import view, pluginmanager, env
from pkg_resources import resource_filename
import pygeoipmap
from . import templates
import os


class IpMapParameters(view.Parameters):

    def register(self):
        self.optional("carte_monde",str)
        pluginmanager.PluginBase.__init__(self)



class IpMap(view.View): 
    plugin_name = "IpMap" 
    plugin_description = "A plugin that display an IpMap" 
    plugin_version = "1.0.0" 
    view_name = "IpMap" 
    view_section = "IpMap"
    view_template = templates.ipmap
    view_parameters = IpMapParameters

    def __init__(self):
        view.View.__init__(self)
        self._config = getattr(env.config, "images",{})

    plugin_htdocs = (("ipmap", resource_filename(__name__, "htdocs")),)


    def render(self):
        params = self.parameters
 
