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


@add_description(" - TEMPLATE RULE: Error condition shouldn't happened.")
def rule_error_example(**kwargs):
    ERROR_MESSAGE = "[ERROR] Error occurred."
    if True:
        result_logger.info(ERROR_MESSAGE)


@add_description(" - TEMPLATE RULE: Warning condition shouldn't happened.")
def rule_warning_example(**kwargs):
    WARNING_MESSAGE = "[WARNING] Warning occurred."
    if True:
        result_logger.info(WARNING_MESSAGE)


@add_description(" - TEMPLATE RULE: Custom issue condition shouldn't occurred.")
def rule_custom_type_example(**kwargs):
    MESSAGE = "[CUSTOM TYPE] Custom issue occurred."
    if True:
        result_logger.info(MESSAGE)


@add_description(" - TEMPLATE RULE: Rule that should be skipped.")
def rule_skip_me(**kwargs):
    MESSAGE = "[TYPE] This rule should be skipped if SkipRulesFile parameter is specified in config file."
    if True:
        result_logger.info(MESSAGE)
