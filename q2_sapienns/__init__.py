# ----------------------------------------------------------------------------
# Copyright (c) 2022, QIIME 2 development team.
#
# Distributed under the terms of the Modified BSD License.
#
# The full license is in the file LICENSE, distributed with this software.
# ----------------------------------------------------------------------------

# flake8: noqa

try:
    from ._version import __version__
except ModuleNotFoundError:
    __version__ = '0.0.0+notfound'

from .plugin_setup import (
    HumannGeneFamilyDirectoryFormat, HumannGeneFamilyFormat,
    HumannPathAbundanceDirectoryFormat, HumannPathAbundanceFormat,
    MetaphlanMergedAbundanceDirectoryFormat, MetaphlanMergedAbundanceFormat,
    MetaphlanMergedAbundanceTable, HumannPathAbundanceTable,
    HumannGeneFamilyTable
)
