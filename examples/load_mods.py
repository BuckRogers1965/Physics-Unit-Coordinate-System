import importlib.util
import os

def load_module(file_path, module_name):
    """
    Dynamically loads a module from a specified file path.
    
    Parameters:
        file_path (str): Path to the module file.
        module_name (str): Name to assign to the loaded module.
    
    Returns:
        module: Loaded module object.
    """

    spec = importlib.util.spec_from_file_location(module_name, file_path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)

    return module
