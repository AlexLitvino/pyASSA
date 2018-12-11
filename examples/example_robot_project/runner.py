from pyassa import assa
import rules_definition
import custom_utils

assa.runner("config.ini",
            rules_module=rules_definition,
            is_script=custom_utils.is_script,
            get_configuration_parameters=custom_utils.get_configuration_parameters,
            get_script=custom_utils.get_script,
            close_script=custom_utils.close_script)
