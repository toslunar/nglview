#!/usr/bin/env python
# coding: utf-8

import warnings

from .example import ExampleWidget
from ._version import __version__, version_info
# for doc
from . import adaptor, datafiles, show, widget
from .adaptor import *
from .base_adaptor import *
# TODO: do not use import *
# interface
from .config import BACKENDS
from .data_source import DatasourceRegistry
from .show import *
# utils
from .utils import js_utils, widget_utils
from .widget import NGLWidget, write_html

with warnings.catch_warnings():
    warnings.simplefilter("ignore")

# Register nbextension


def _jupyter_labextension_paths():
    """Called by Jupyter Lab Server to detect if it is a valid labextension and
    to install the widget
    Returns
    =======
    src: Source directory name to copy files from. Webpack outputs generated files
        into this directory and Jupyter Lab copies from this directory during
        widget installation
    dest: Destination directory name to install widget files to. Jupyter Lab copies
        from `src` directory into <jupyter path>/labextensions/<dest> directory
        during widget installation
    """
    return [{
        'src': 'labextension',
        'dest': 'nglview-js-widgets',
    }]


def _jupyter_nbextension_paths():
    """Called by Jupyter Notebook Server to detect if it is a valid nbextension and
    to install the widget
    Returns
    =======
    section: The section of the Jupyter Notebook Server to change.
        Must be 'notebook' for widget extensions
    src: Source directory name to copy files from. Webpack outputs generated files
        into this directory and Jupyter Notebook copies from this directory during
        widget installation
    dest: Destination directory name to install widget files to. Jupyter Notebook copies
        from `src` directory into <jupyter path>/nbextensions/<dest> directory
        during widget installation
    require: Path to importable AMD Javascript module inside the
        <jupyter path>/nbextensions/<dest> directory
    """
    return [{
        'section': 'notebook',
        'src': 'nbextension',
        'dest': 'nglview',
        'require': 'nglview/extension'
    }]


__all__ = ['NGLWidget', 'write_html'
           ] + widget.__all__ + adaptor.__all__ + show.__all__
