import fnmatch
import glob
import os
from importlib import import_module


def import_modules(base_path, base_package, module_name):
    for file in glob.glob(os.path.join(os.path.relpath(base_path), '**', module_name), recursive=True):
        filepath_with_package_name = file.replace(os.sep, '.')
        module_with_package_name = filepath_with_package_name[0: -3]
        # remove "." in front of module_with_package_name when you run unittest below
        # it makes "...app.resource.api.resource" to "app.resource.api.resource"
        count = range(len(module_with_package_name))
        for n in count:
            if module_with_package_name[n] == '.':
                continue
            else:
                break
        filtered_module_with_package_name = module_with_package_name[n:]
        import_module(filtered_module_with_package_name)
    pass


def as_dictionary(self):
    return {c.name: getattr(self, c.name) for c in self.__table__.columns}


def as_dictionary_except_for(self, fields):
    return {c.name: getattr(self, c.name) for c in self.__table__.columns}
