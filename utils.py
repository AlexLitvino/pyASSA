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
# This file contains general utilities functions
# Utilities function related for specific project should be implemented in custom_utils.py
# -----------------------------------------------------------------------------

import os
from logger import result_logger
from customization.custom_utils import is_script


def get_rules(rules_module):
    """
    Get rule functions from module
    :param rules_module: module with rules implementations
    :return: rule functions
    """
    rules = []
    for item in dir(rules_module):
        if item.startswith("rule"):
            rules.append(getattr(rules_module, item))
    return rules


def get_script_files(directory):
    """
    Function recursively walk directory and finds files that satisfies custom is_script() function
    :param directory: path of directory that contains scripts (inside it or inside included directories)
    :return: list of scripts
    """
    script_files = []
    for root, dirs, files in os.walk(directory, topdown=True):
        for full_file_name in files:
            if is_script(root, full_file_name):
                script_files.append(os.path.join(root, full_file_name))
    return script_files


def add_description(description):
    """
    Decorator for adding value for __description__ attribute of decorated function
    :param description: value for __description__ attribute
    :return: decorated function, with added __description__ attribute
    """
    def decorator(func):
        func.__description__ = description
        return func
    return decorator


def select_rules(rules, config):
    """
    Select rules according conditions specified in configuration file
    :param rules: all discovered rules from rules_definition.py module
    :param config: object for configuration file
    :return: rules that satisfies condition in configuration file
    """
    # TODO: implement
    return rules


def select_scripts(scripts, config):
    """
    Selects scripts according conditions specified in configuration file
    :param scripts: all discovered scripts
    :param config: object for configuration file
    :return: scripts that satisfies condition in configuration file
    """
    # TODO: implement
    return scripts


def print_log_header(scripts_directory, selected_rules):
    """
    Helper function for putting header data into results logger
    :param scripts_directory: directory where scripts are located
    :param selected_rules: rules that will be applied to scripts
    :return: None
    """
    result_logger.info("Performing analysis of scripts from directory:")
    result_logger.info(scripts_directory)
    result_logger.info("")
    result_logger.info("{number_of_rules} rules are found:".format(number_of_rules=len(selected_rules)))
    for rule in selected_rules:
        if hasattr(rule, "__description__"):
            result_logger.info(rule.__description__)
        else:
            result_logger.info(rule.__name__)
    result_logger.info("")
