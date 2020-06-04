#   -*- coding: utf-8 -*-
from pybuilder.core import use_plugin, init
import glob
import os
import shutil
import logging

from pybuilder.core import use_plugin, init, Author, task
from pybuilder.utils import assert_can_execute

use_plugin("python.core")
use_plugin("python.unittest")
use_plugin("python.distutils")


name = "kubectl-podnode"
default_task = "publish"


@init
def set_properties(project):
    install_dependencies(project)

@task
def install_dependencies(project):
    project.depends_on('docopt')
    project.depends_on('kubernetes')
    project.depends_on('pydash')
    project.depends_on('jsonpickle')
    # project.depends_on('nrql-simple')
    # project.depends_on('text-to-image')
