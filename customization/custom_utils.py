# -----------------------------------------------------------------------------
# Copyright 2017 Aleksey Litvinov litvinov.aleks@gmail.com
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
# -----------------------------------------------------------------------------

# -----------------------------------------------------------------------------
# This file will contain utilities function for specific project.
# -----------------------------------------------------------------------------


# <CUSTOMIZATION>
def is_script(root, full_file_name):
    """
    Function decides if current file a script according to its root and full name
    :param root: path to the file
    :param full_file_name: name of file with extension (if present)
    :return: boolean value, if file is a script
    """
    is_script_result = full_file_name.endswith("py")
    return is_script_result
# </CUSTOMIZATION>


# <CUSTOMIZATION>
def get_configuration_parameters(config):
    """
    Creates dictionary with parameters taken from/based on configuration file object
    :param config: object for configuration file
    :return: dictionary with custom parameters taken from/based on configuration file object
    """
    kwargs = {}

    return kwargs
# </CUSTOMIZATION>


# <CUSTOMIZATION>
def get_script(script_path):
    """
    Returns script object by its path (for example for file-like object call open(script_path)).
    File preprocessing could be implemented here.
    :param script_path: path to script file
    :return: script object
    """
    return None
# </CUSTOMIZATION>


# <CUSTOMIZATION>
def close_script(script):
    """
    Perform action on script object close (for example, if script is file-like object call script.close())
    :param script: script object
    :return: None
    """
    pass
# </CUSTOMIZATION>
