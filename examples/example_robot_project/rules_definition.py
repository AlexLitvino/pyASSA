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
# This file will contain customization for specific project.
# Here only rule_*(**kwargs) should be implemented,
# or helper functions _function_name().
# -----------------------------------------------------------------------------

from pyassa.logger import result_logger
from pyassa.utils import add_description
from custom_utils import get_scenario_header, get_scenario_data, is_int

# TODO: Suggest testing command parameters and values based on command rule table (separate file - xsl, json, xml - ...
# TODO: ... that describes rules for specific command)


@add_description(" - [WARNING]: Scenario file should contain only one sheet.")
def rule_warning_extra_sheets(**kwargs):
    wb = kwargs["script"]
    scenario_sheet_name = kwargs["scenario_sheet"]
    WARNING_MESSAGE = "[WARNING] Script contains {sheets_number} sheet(s) instead of one sheet: {unexpected_sheets}"
    sheets = wb.get_sheet_names()
    if len(sheets) > 1:
        unexpected_sheets = set(sheets) - set(scenario_sheet_name)
        result_logger.info(WARNING_MESSAGE.format(sheets_number=len(sheets), unexpected_sheets=unexpected_sheets))


@add_description(" - [ERROR]: Scenario file should contain sheet with name 'Scenario'.")
def rule_error_missing_scenario_sheet(**kwargs):
    wb = kwargs["script"]
    scenario_sheet_name = kwargs["scenario_sheet"]
    ERROR_MESSAGE = "[ERROR] Scenario file doesn't contain 'Scenario' sheet."
    sheets = wb.get_sheet_names()
    if scenario_sheet_name not in sheets:
        result_logger.info(ERROR_MESSAGE)


@add_description(" - [ERROR]: First row should contain column names: 'Command', 'Parameter', 'Value'.")
def rule_error_incorrect_scenario_headers(**kwargs):
    wb = kwargs["script"]
    scenario_sheet_name = kwargs["scenario_sheet"]
    expected_headers = kwargs["expected_headers"]
    ERROR_MESSAGE = "[ERROR] Header is not " + str(expected_headers) + " row."
    scenario_sheet = wb.get_sheet_by_name(scenario_sheet_name)
    header = get_scenario_header(scenario_sheet)
    if header[0] != expected_headers[0] or header[1] != expected_headers[1] or header[2] != expected_headers[2]:
        result_logger.info(ERROR_MESSAGE)


@add_description(" - [ERROR]: For every scenario row, Command value should NOT be empty.")
def rule_error_empty_command(**kwargs):
    wb = kwargs["script"]
    scenario_sheet_name = kwargs["scenario_sheet"]
    ERROR_MESSAGE = "[ERROR] In rows {rows_with_empty_command} Command field is empty."
    scenario_sheet = wb.get_sheet_by_name(scenario_sheet_name)
    rows = get_scenario_data(scenario_sheet)
    rows_with_empty_command = []
    for i, row in enumerate(rows, start=2):
        if row[0] == 'None':
            rows_with_empty_command.append(i)
    if rows_with_empty_command:
        result_logger.info(ERROR_MESSAGE.format(rows_with_empty_command=rows_with_empty_command))


@add_description(" - [ERROR]: Unknown command.")
def rule_error_unknown_command(**kwargs):
    wb = kwargs["script"]
    commands = kwargs["commands"]
    scenario_sheet_name = kwargs["scenario_sheet"]
    ERROR_MESSAGE = "[ERROR] Steps {row_number} contains unknown command '{unknown_command}'."
    scenario_sheet = wb.get_sheet_by_name(scenario_sheet_name)
    rows = get_scenario_data(scenario_sheet)
    for row_number, row in enumerate(rows, start=2):
        if row[0] not in commands:
            result_logger.info(ERROR_MESSAGE.format(row_number=row_number, unknown_command=row[0]))


@add_description(" - [ERROR]: For 'MOVE' command Parameter could be 'Forward' or 'Backward', and Value should be Integer greater or equal to zero.")
def rule_error_incorrect_move_command(**kwargs):
    wb = kwargs["script"]
    scenario_sheet_name = kwargs["scenario_sheet"]
    ERROR_MESSAGE_INCORRECT_PARAMETER = "[ERROR] Step {row_number} with 'MOVE' command has '{move_parameter}' Parameter value instead of 'Forward' or 'Backward' values."
    ERROR_MESSAGE_VALUE_NOT_INTEGER = "[ERROR] Step {row_number} with 'MOVE' has Value value '{value}' that is not integer."
    ERROR_MESSAGE_VALUE_LESS_THAN_ZERO = "[ERROR] Step {row_number} with 'MOVE' has Value value '{value}' less than zero."
    scenario_sheet = wb.get_sheet_by_name(scenario_sheet_name)
    rows = get_scenario_data(scenario_sheet)
    for row_number, row in enumerate(rows, start=2):
        command = row[0]
        parameter = row[1]
        value = row[2]
        if command == 'MOVE':
            if parameter not in ["Forward", "Backward"]:
                result_logger.info(ERROR_MESSAGE_INCORRECT_PARAMETER.format(row_number=row_number, move_parameter=parameter))
            if value != 'None':
                if not is_int(value):
                    result_logger.info(ERROR_MESSAGE_VALUE_NOT_INTEGER.format(row_number=row_number, value=value))
                elif int(value) < 0:
                    result_logger.info(ERROR_MESSAGE_VALUE_LESS_THAN_ZERO.format(row_number=row_number, value=value))


@add_description(" - [ERROR]: For 'ROTATE' command Parameter could be 'Clockwise' or 'Counterclockwise', and Value should be Integer in range 0 .. 360 inclusevily.")
def rule_error_incorrect_rotate_command(**kwargs):
    wb = kwargs["script"]
    scenario_sheet_name = kwargs["scenario_sheet"]
    ERROR_MESSAGE_INCORRECT_PARAMETER = "[ERROR] Step {row_number} with 'ROTATE' command has '{move_parameter}' Parameter value instead of 'Clockwise' or 'Counterclockwise' values."
    ERROR_MESSAGE_VALUE_NOT_INTEGER = "[ERROR] Step {row_number} with 'ROTATE' has Value value '{value}' that is not integer."
    ERROR_MESSAGE_VALUE_OUT_OF_RANGE_0_360_DEGREES = "[ERROR] Step {row_number} with 'ROTATE' has Value value '{value}' out of range [0 .. 360] degrees."
    scenario_sheet = wb.get_sheet_by_name(scenario_sheet_name)
    rows = get_scenario_data(scenario_sheet)
    for row_number, row in enumerate(rows, start=2):
        command = row[0]
        parameter = row[1]
        value = row[2]
        if command == 'ROTATE':
            if parameter not in ["Clockwise", "Counterclockwise"]:
                result_logger.info(ERROR_MESSAGE_INCORRECT_PARAMETER.format(row_number=row_number, move_parameter=parameter))
            if value != 'None':
                if not is_int(value):
                    result_logger.info(ERROR_MESSAGE_VALUE_NOT_INTEGER.format(row_number=row_number, value=value))
                elif int(value) < 0 or int(value) > 360:
                    result_logger.info(ERROR_MESSAGE_VALUE_OUT_OF_RANGE_0_360_DEGREES.format(row_number=row_number, value=value))


@add_description(" - [ERROR]: For 'SET_STATE' command Parameter could be 'Velocity' or 'Battery' with valid values.")
def rule_error_incorrect_set_state_command(**kwargs):
    wb = kwargs["script"]
    scenario_sheet_name = kwargs["scenario_sheet"]
    ERROR_MESSAGE_INCORRECT_PARAMETER = "[ERROR] Step {row_number} with 'SET_STATE' command has '{set_state_parameter}' Parameter value instead of 'Velocity' or 'Battery' values."
    ERROR_MESSAGE_VALUE_NOT_INTEGER = "[ERROR] Step {row_number} with 'SET_STATE' has Value value '{value}' that is not integer."
    ERROR_MESSAGE_VALUE_FOR_VELOCITY_LESS_THAN_ZERO = "[ERROR] Step {row_number} with 'SET_STATE' and Parameter = 'Velocity' has Value value '{value}' less than zero."
    ERROR_MESSAGE_VALUE_FOR_BATTERY_INCORRECT = "[ERROR] Step {row_number} with 'SET_STATE' and Parameter = 'Battery' has Value value '{value}' out of range [0 .. 100] or not multiple to 5."
    scenario_sheet = wb.get_sheet_by_name(scenario_sheet_name)
    rows = get_scenario_data(scenario_sheet)
    for row_number, row in enumerate(rows, start=2):
        command = row[0]
        parameter = row[1]
        value = row[2]
        if command == 'SET_STATE':
            if parameter not in ["Velocity", "Battery"]:
                result_logger.info(ERROR_MESSAGE_INCORRECT_PARAMETER.format(row_number=row_number, set_state_parameter=parameter))
            if parameter == "Velocity":
                if not is_int(value):
                    result_logger.info(ERROR_MESSAGE_VALUE_NOT_INTEGER.format(row_number=row_number, value=value))
                elif int(value) < 0:
                    result_logger.info(ERROR_MESSAGE_VALUE_FOR_VELOCITY_LESS_THAN_ZERO.format(row_number=row_number, value=value))
            elif parameter == "Battery":
                if not is_int(value):
                    result_logger.info(ERROR_MESSAGE_VALUE_NOT_INTEGER.format(row_number=row_number, value=value))
                elif int(value) < 0 or int(value) > 100 or int(value) % 5 != 0:
                    result_logger.info(ERROR_MESSAGE_VALUE_FOR_BATTERY_INCORRECT.format(row_number=row_number, value=value))


@add_description(" - [ERROR]: For 'TAKE' command Parameter and Value should be empty.")
def rule_error_not_empty_parameter_and_value_for_take_command(**kwargs):
    wb = kwargs["script"]
    scenario_sheet_name = kwargs["scenario_sheet"]
    ERROR_MESSAGE_NOT_EMPTY_PARAMETER = "[ERROR] Step {row_number} with 'TAKE' command has not empty Parameter value."
    ERROR_MESSAGE_NOT_EMPTY_VALUE = "[ERROR] Step {row_number} with 'TAKE' command has not empty Value value."
    scenario_sheet = wb.get_sheet_by_name(scenario_sheet_name)
    rows = get_scenario_data(scenario_sheet)
    for row_number, row in enumerate(rows, start=2):
        if row[0] == 'TAKE':
            if row[1] != 'None':
                result_logger.info(ERROR_MESSAGE_NOT_EMPTY_PARAMETER.format(row_number=row_number))
            if row[2] != 'None':
                result_logger.info(ERROR_MESSAGE_NOT_EMPTY_VALUE.format(row_number=row_number))


@add_description(" - [ERROR]: For 'COMMENT' command Parameter should be empty.")
def rule_error_not_empty_parameter_for_comment_command(**kwargs):
    wb = kwargs["script"]
    scenario_sheet_name = kwargs["scenario_sheet"]
    ERROR_MESSAGE = "[ERROR] Step {row_number} with 'COMMENT' command has not empty Parameter value."
    scenario_sheet = wb.get_sheet_by_name(scenario_sheet_name)
    rows = get_scenario_data(scenario_sheet)
    for row_number, row in enumerate(rows, start=2):
        if row[0] == 'COMMENT' and row[1] != 'None':
            result_logger.info(ERROR_MESSAGE.format(row_number=row_number))


@add_description(" - [WARNING]: For 'COMMENT' command Value shouldn't be empty string.")
def rule_warning_empty_value_for_comment_command(**kwargs):
    wb = kwargs["script"]
    scenario_sheet_name = kwargs["scenario_sheet"]
    WARNING_MESSAGE = "[WARNING] Step {row_number} with 'COMMENT' command has empty Value parameter."
    scenario_sheet = wb.get_sheet_by_name(scenario_sheet_name)
    rows = get_scenario_data(scenario_sheet)
    for row_number, row in enumerate(rows, start=2):
        if row[0] == 'COMMENT' and row[2] == 'None':
            result_logger.info(WARNING_MESSAGE.format(row_number=row_number))
