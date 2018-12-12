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
import inspect
from pyassa.logger import result_logger


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


def get_script_files(directory, is_script):
    """
    Function recursively walk directory and finds files that satisfies custom is_script() function
    :param directory: path of directory that contains scripts (inside it or inside included directories)
    :param is_script: function that takes file root and full_file_name as parameters and returns boolean if file is script
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
    rules_parameters = config["RULES"]
    errors_condition = rules_parameters.getboolean("Errors")
    warnings_condition = rules_parameters.getboolean("Warnings")
    other_condition = rules_parameters.getboolean("Other")
    skip_file_path = rules_parameters["SkipRulesFilePath"]
    skip_condition = bool(skip_file_path)
    exclusive_file_path = rules_parameters["ExclusiveRulesFilePath"]
    exclusive_condition = bool(exclusive_file_path)
    filter_exclusive_rules = rules_parameters.getboolean("FilterExclusiveRules")

    selected_rules = []

    def _filter_rules(rules_to_filter):
        filtered_rules = []
        error_rules = [rule for rule in rules_to_filter if rule.__name__.startswith("rule_error")]
        warning_rules = [rule for rule in rules_to_filter if rule.__name__.startswith("rule_warning")]
        other_rules = [rule for rule in rules_to_filter if ((rule.__name__.startswith("rule")) and
                                                            (not rule.__name__.startswith("rule_error")) and
                                                            (not rule.__name__.startswith("rule_warning")))]

        skipped_rules_names = []
        if skip_condition:
            with open(skip_file_path, 'r') as skip_file:
                for line in skip_file:
                    skipped_rule_name = line[:-1] if line.endswith('\n') else line
                    skipped_rules_names.append(skipped_rule_name)
        skipped_rules = [rule for rule in rules_to_filter if rule.__name__ in skipped_rules_names]

        if errors_condition:
            filtered_rules.extend(error_rules)
        if warnings_condition:
            filtered_rules.extend(warning_rules)
        if other_condition:
            filtered_rules.extend(other_rules)
        if skip_condition:
            filtered_rules = list(set(filtered_rules) - set(skipped_rules))

        return filtered_rules

    if exclusive_condition:
        exclusive_rules_names = []
        with open(exclusive_file_path, 'r') as exclusive_file:
            for line in exclusive_file:
                exclusive_rule_name = line[:-1] if line.endswith('\n') else line
                exclusive_rules_names.append(exclusive_rule_name)
            exclusive_rules = [rule for rule in rules if rule.__name__ in exclusive_rules_names]
            if filter_exclusive_rules:
                selected_rules = _filter_rules(exclusive_rules)
            else:
                selected_rules = exclusive_rules
    else:
        selected_rules = _filter_rules(rules)
    return selected_rules


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
            rule_description = rule.__description__
        else:
            rule_description = rule.__name__
        if "raise NotImplementedError" in inspect.getsource(rule):
            rule_description = " - [NOT IMPLEMENTED RULE]" + rule_description
        result_logger.info(rule_description)
    result_logger.info("")
