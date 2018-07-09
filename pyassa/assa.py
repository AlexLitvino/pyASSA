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

import configparser
import traceback
from time import clock
from utils import get_rules, select_rules
from utils import get_script_files, select_scripts
from utils import print_log_header
from logger import result_logger, error_logger
import customization.rules_definition
from customization.custom_utils import get_configuration_parameters
from customization.custom_utils import get_script, close_script


def script_analyser(script_path, rules, **kwargs):  # TODO: calculate how many rules PASS/FAIL
    """
    Applies rules to specific script and performs result logging
    :param script_path: path to specific script
    :param rules: list of rules to be applied for script analysis
    :param kwargs: dictionary for any additional parameters
    :return: None
    """

    result_logger.info("{script} analysis:".format(script=script_path))
    error_logger.info("{script} analysis:".format(script=script_path))
    error_logger.info("")
    script = get_script(script_path)
    try:
        # TODO: create function that will return file-like object based on path and will use context manager
        kwargs["script"] = script
        for rule in rules:
            try:
                rule(**kwargs)
            except NotImplementedError:
                pass
            except Exception:  # catch ANY rule exception
                result_logger.info("Error was occurred when applied {rule}.".format(rule=rule.__name__))
                error_logger.error(traceback.format_exc())
    except Exception:  # catch ANY file exception
        result_logger.info("{script} wasn't opened".format(script=script_path))
        error_logger.error(traceback.format_exc())
    finally:
        close_script(script)
        result_logger.info("Script analysis completed.")
        result_logger.info("")
        error_logger.info("*"*80)
        error_logger.info("")


def runner(configuration_file):
    """
    Entry point for static analyzer
    :param configuration_file: Path to configuration file
    :return: None
    """

    # Get data from configuration file
    config = configparser.ConfigParser()
    config.read(configuration_file)

    scripts_directory = config["LOCATIONS"]["ScriptsDirectory"]

    kwargs = get_configuration_parameters(config)

    # Get script which should be analysed
    scripts = get_script_files(scripts_directory)
    selected_scripts = select_scripts(scripts, config)

    # Get rules for script analysis
    rules = get_rules(customization.rules_definition)
    selected_rules = select_rules(rules, config)

    # Print header to result log
    print_log_header(scripts_directory, selected_rules)

    # Perform script analysis
    start_time = clock()

    for script_path in selected_scripts:
        script_analyser(script_path, selected_rules, **kwargs)

    finish_time = clock()
    runtime = finish_time - start_time
    result_logger.info("Analysis completed in {runtime:.2f} seconds.".format(runtime=runtime))


if __name__ == "__main__":
    configuration_file = "..\\configuration\\config.ini"  # TODO: or take argument from command line?
    runner(configuration_file)
