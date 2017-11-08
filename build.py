from pybuilder.core import use_plugin, init

use_plugin("python.core")
use_plugin("python.install_dependencies")
use_plugin("python.distutils")
use_plugin("copy_resources")


version = "1.0.0"
default_task = "publish"
summary = 'house Temp app - flask.'

@init
def set_properties(project):
    project.depends_on_requirements("requirements.txt")
    project.set_property("copy_resources_target", "$dir_dist")
    # Add templates
    project.get_property("copy_resources_glob").append("templates/*")
    project.include_file("houseTemperature", "templates/*")
    # Add static
    project.get_property("copy_resources_glob").append("static/*")
    project.include_file("houseTemperature", "static/*")
        # Add key
    project.get_property("copy_resources_glob").append("models/*")
    project.include_file("houseTemperature", "models/*")


