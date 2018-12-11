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

import re


# <CUSTOMIZATION>
def is_script(root, full_file_name):
    """
    Function decides if current file a script according to its root and full name
    :param root: path to the file
    :param full_file_name: name of file with extension (if present)
    :return: boolean value, if file is a script
    """
    pattern = r"Issue_\d+\.txt"
    is_script_result = re.match(pattern, full_file_name)
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
    kwargs["features"] = [feature.strip() for feature in config["CUSTOM_PARAMETERS"]["Features"].split(',')]
    kwargs["priorities"] = [feature.strip() for feature in config["CUSTOM_PARAMETERS"]["Priority_levels"].split(',')]

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
    with open(script_path, 'r') as script_file:
        script_lines = script_file.readlines()
    return script_lines
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


def report_parser(report):
    report_lines = report
    headers = ["Summary", "Type", "Feature", "Build Number", "Priority", "Reported By", "Reported On", "Environment",
               "Description", "Steps To Reproduce"]
    parsed_report = {}
    not_completed_section_flag = False
    header_id = 0
    for line in report_lines:
        if line.startswith(headers[header_id]):
            not_completed_section_flag = True
            parsed_report[headers[header_id]] = line[len(headers[header_id]) + 1:]
        elif not_completed_section_flag and line != '\n':  # TODO: should be if line_not_empty (spaces, tabs, new lines)
            parsed_report[headers[header_id]] += line
        elif line == '\n':
            if not_completed_section_flag:
                header_id += 1
            not_completed_section_flag = False

    parsed_report = {header: parsed_report[header].strip() for header in parsed_report}

    return parsed_report
