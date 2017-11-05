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

from logger import result_logger
from utils import add_description
from customization.custom_utils import report_parser
import re


@add_description(" - [ERROR] Summary field should not be empty string.")
def rule_error_incorrect_summary(**kwargs):
    report = kwargs["script"]
    parsed_report = report_parser(report)
    ERROR_MESSAGE_EMPTY_SUMMARY = "[ERROR] Summary is empty."

    if parsed_report["Summary"] == '':
        result_logger.info(ERROR_MESSAGE_EMPTY_SUMMARY)


@add_description(" - [WARNING] Summary field should not contain more than 20 words.")
def rule_warning_summary_longer_than_20_words(**kwargs):
    report = kwargs["script"]
    parsed_report = report_parser(report)
    ERROR_MESSAGE_SUMMARY_LONGER_THAN_20_WORDS = "[WARNING] Summary is {summary_length} words long."
    summary_length = len(parsed_report["Summary"].split())

    if summary_length > 20:
        result_logger.info(ERROR_MESSAGE_SUMMARY_LONGER_THAN_20_WORDS.format(summary_length=summary_length))


@add_description(" - [ERROR] Feature field should have predefined value - if Type=Defect or N/A - if Type=Enhancement.")
def rule_error_incorrect_feature(**kwargs):
    report = kwargs["script"]
    features = kwargs["features"]
    parsed_report = report_parser(report)
    type_field = parsed_report["Type"]
    feature_field = parsed_report["Feature"]
    ERROR_MESSAGE_INCORRECT_FEATURE_FOR_DEFECT = "[ERROR] Feature is '{actual_feature}' instead of value from list " + str(features) + " for Defect issue."
    ERROR_MESSAGE_INCORRECT_FEATURE_FOR_ENHANCEMENT = "[ERROR] Feature is not N/A for Enhancement issue."

    if type_field == "Defect":
        if feature_field not in features:
            result_logger.info(ERROR_MESSAGE_INCORRECT_FEATURE_FOR_DEFECT.format(actual_feature=feature_field))
    elif type_field == "Enhancement":
        if feature_field != "N/A":
            result_logger.info(ERROR_MESSAGE_INCORRECT_FEATURE_FOR_ENHANCEMENT)
    else:
        pass  # TODO: error handling should be here, unknown type


@add_description(" - [ERROR] Type field should be Defect or Enhancement.")
def rule_error_incorrect_type(**kwargs):
    report = kwargs["script"]
    parsed_report = report_parser(report)
    type_field = parsed_report["Type"]
    ERROR_MESSAGE_INCORRECT_TYPE = "[ERROR] Type is '{actual_type}' instead of Defect or Enhancement."

    if type_field not in ["Defect", "Enhancement"]:
        result_logger.info(ERROR_MESSAGE_INCORRECT_TYPE.format(actual_type=type_field))


@add_description(" - [ERROR] Build number field should be in format Number.Number.Number - if Type=Defect or "
                 "N/A - if Type=Enhancement.")
def rule_error_incorrect_build_number(**kwargs):
    report = kwargs["script"]
    parsed_report = report_parser(report)
    type_field = parsed_report["Type"]
    build_number_field = parsed_report["Build Number"]
    ERROR_MESSAGE_INCORRECT_BUILD_NUMBER_FOR_DEFECT = "[ERROR] Build Number is {actual_build_number} instead of " \
                                                      "to be in format Number.Number.Number for Defect issue."
    ERROR_MESSAGE_INCORRECT_BUILD_NUMBER_FOR_ENHANCEMENT = "[ERROR] Build Number is {actual_build_number} instead of " \
                                                           "N/A for Enhancement issue."

    if type_field == "Defect":
        pattern = r"\d+\.\d+\.\d+"
        if not re.match(pattern, build_number_field):
            result_logger.info(ERROR_MESSAGE_INCORRECT_BUILD_NUMBER_FOR_DEFECT.format(actual_build_number=build_number_field))
    elif type_field == "Enhancement":
        if build_number_field != "N/A":
            result_logger.info(ERROR_MESSAGE_INCORRECT_BUILD_NUMBER_FOR_ENHANCEMENT.format(actual_build_number=build_number_field))
    else:
        pass  # TODO: error handling should be here, unknown type


@add_description(" - [ERROR] Priority field should be one of the predefined values.")
def rule_error_incorrect_priority(**kwargs):
    report = kwargs["script"]
    priorities = kwargs["priorities"]
    parsed_report = report_parser(report)
    priority_field = parsed_report["Priority"]
    ERROR_MESSAGE_INCORRECT_PRIORITY = "[ERROR] Priority is '{actual_priority}' instead of value from list: " + str(priorities) + "."

    if priority_field not in priorities:
        result_logger.info(ERROR_MESSAGE_INCORRECT_PRIORITY.format(actual_priority=priority_field))


@add_description(" - [ERROR] Reported By field should not be empty string.")
def rule_error_empty_reported_by(**kwargs):
    report = kwargs["script"]
    parsed_report = report_parser(report)
    ERROR_MESSAGE_EMPTY_REPORTED_BY = "[ERROR] Reported By is empty."

    if parsed_report["Reported By"] == '':
        result_logger.info(ERROR_MESSAGE_EMPTY_REPORTED_BY)


@add_description(" - [ERROR] Date field should be in format MM-DD-YYYY.")
def rule_error_incorrect_date_format(**kwargs):
    report = kwargs["script"]
    parsed_report = report_parser(report)
    date_field = parsed_report["Reported On"]
    ERROR_MESSAGE_INCORRECT_DATE_FORMAT = "[ERROR] Date field '{date_field}' is not in format MM-DD-YYYY."
    # TODO: date validation is very primitive, suggest updating
    # it checks fromat MM-DD-YYYY, and 1 <= MM <= 12, 1 <= DD <= 31 - for any moonth
    pattern = r"[01]\d-[0123]\d-\d{4}"
    is_date_valid = False
    if re.match(pattern, date_field):
        mm, dd, yyyy = date_field.split('-')
        if 1 <= int(mm) <= 12 and 1 <= int(dd) <= 31:
            is_date_valid = True

    if not is_date_valid:
        result_logger.info(ERROR_MESSAGE_INCORRECT_DATE_FORMAT.format(date_field=date_field))


@add_description(" - [ERROR] Environment field shouldn't be empty if Type=Defect.")
def rule_error_environment_empty_for_defect_issue(**kwargs):
    report = kwargs["script"]
    parsed_report = report_parser(report)
    type_field = parsed_report["Type"]
    environment_field = parsed_report["Environment"]
    ERROR_MESSAGE_EMPTY_ENVIRONMENT_FOR_DEFECT = "[ERROR] Environment is empty when Type=Defect."

    if type_field == "Defect":
        if environment_field == '':
            result_logger.info(ERROR_MESSAGE_EMPTY_ENVIRONMENT_FOR_DEFECT)


@add_description(" - [ERROR] Description field shouldn't be empty string.")
def rule_error_empty_description(**kwargs):
    report = kwargs["script"]
    parsed_report = report_parser(report)
    description_field = parsed_report["Description"]
    ERROR_MESSAGE_EMPTY_DESCRIPTION = "[ERROR] Description is empty."

    if description_field == '':
        result_logger.info(ERROR_MESSAGE_EMPTY_DESCRIPTION)
