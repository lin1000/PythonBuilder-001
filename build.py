from pybuilder.core import init,use_plugin

use_plugin("python.core")
use_plugin("python.unittest")
use_plugin("python.coverage")
use_plugin("python.install_dependencies")
use_plugin("python.distutils")
use_plugin("copy_resources")

default_task = "publish"

@init
def initialize(project):
    project.build_depends_on('mockito')
    project.version = "0.1.14"
    project.set_property("copy_resources_target","target/copy-to")
    copy_resources = []
    copy_resources.append("copy-from/copy.txt")
    project.set_property("copy_resources_glob",copy_resources)
