import fnmatch
import glob
import os
from importlib import import_module


def import_modules(base_path, base_package, module_name):
    for file in glob.glob(os.path.join(os.path.relpath(base_path), '**', module_name), recursive=True):
        filepath_with_package_name = file.replace(os.sep, '.')
        module_with_package_name = filepath_with_package_name[0: -3]
        import_module(module_with_package_name)
    pass
