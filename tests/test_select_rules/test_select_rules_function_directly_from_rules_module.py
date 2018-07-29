import unittest
from tests.test_select_rules.rules_to_test_select_rules_function import *
import tests.test_select_rules.rules_to_test_select_rules_function
from pyassa.utils import select_rules
from pyassa.utils import get_rules
from tests.test_select_rules.configparsermock import ConfigparserMock


class TestSelectRulesDirectlyFromRulesModule(unittest.TestCase):

    def setUp(self):
        configparser = ConfigparserMock()
        self.config = configparser.ConfigParser()
        self.rules = get_rules(tests.test_select_rules.rules_to_test_select_rules_function)

    def test_FFFF_00(self):
        #00|F  |F  |F   |F   |No rules
        configuration_file = {
                "Other": False,
                "Errors": False,
                "Warnings": False,
                "SkipRulesFilePath": "",
                "ExclusiveRulesFilePath": "",
                "FilterExclusiveRules": True
        }
        self.config.read(configuration_file)
        selected_rules = select_rules(self.rules, self.config)
        self.assertCountEqual([], selected_rules)

    def test_FFFT_01(self):
        #01|F  |F  |F   |T   |No rules
        configuration_file = {
                "Other": False,
                "Errors": False,
                "Warnings": False,
                "SkipRulesFilePath": "skipped_rules.txt",
                "ExclusiveRulesFilePath": "",
                "FilterExclusiveRules": False
        }
        self.config.read(configuration_file)
        selected_rules = select_rules(self.rules, self.config)
        self.assertCountEqual([], selected_rules)

    def test_FFTF_02(self):
        #02|F  |F  |T   |F   |Only warnings
        configuration_file = {
                "Other": False,
                "Errors": False,
                "Warnings": True,
                "SkipRulesFilePath": "",
                "ExclusiveRulesFilePath": "",
                "FilterExclusiveRules": True
        }
        self.config.read(configuration_file)
        selected_rules = select_rules(self.rules, self.config)
        self.assertCountEqual([rule_warning_test1,
                              rule_warning_test2,
                              rule_warning_test3], selected_rules)

    def test_FFTT_03(self):
        #03|F  |F  |T   |T   |Only warnings, except skipped
        configuration_file = {
                "Other": False,
                "Errors": False,
                "Warnings": True,
                "SkipRulesFilePath": "skipped_rules.txt",
                "ExclusiveRulesFilePath": "",
                "FilterExclusiveRules": False
        }
        self.config.read(configuration_file)
        selected_rules = select_rules(self.rules, self.config)
        self.assertCountEqual([rule_warning_test1,
                              rule_warning_test3], selected_rules)

    def test_FTFF_04(self):
        #04|F  |T  |F   |F   |Only errors
        configuration_file = {
                "Other": False,
                "Errors": True,
                "Warnings": False,
                "SkipRulesFilePath": "",
                "ExclusiveRulesFilePath": "",
                "FilterExclusiveRules": True
        }
        self.config.read(configuration_file)
        selected_rules = select_rules(self.rules, self.config)
        self.assertCountEqual([rule_error_test1,
                              rule_error_test2,
                              rule_error_test3], selected_rules)

    def test_FTFT_05(self):
        #05|F  |T  |F   |T   |Only errors, except skipped
        configuration_file = {
                "Other": False,
                "Errors": True,
                "Warnings": False,
                "SkipRulesFilePath": "skipped_rules.txt",
                "ExclusiveRulesFilePath": "",
                "FilterExclusiveRules": False
        }
        self.config.read(configuration_file)
        selected_rules = select_rules(self.rules, self.config)
        self.assertCountEqual([rule_error_test2,
                              rule_error_test3], selected_rules)

    def test_FTTF_06(self):
        #06|F  |T  |T   |F   |All errors and warnings
        configuration_file = {
                "Other": False,
                "Errors": True,
                "Warnings": True,
                "SkipRulesFilePath": "",
                "ExclusiveRulesFilePath": "",
                "FilterExclusiveRules": True
        }
        self.config.read(configuration_file)
        selected_rules = select_rules(self.rules, self.config)
        self.assertCountEqual([rule_error_test1,
                              rule_error_test2,
                              rule_error_test3,
                              rule_warning_test1,
                              rule_warning_test2,
                              rule_warning_test3], selected_rules)

    def test_FTTT_07(self):
        #07|F  |T  |T   |T   |Only errors and warnings, except skipped
        configuration_file = {
                "Other": False,
                "Errors": True,
                "Warnings": True,
                "SkipRulesFilePath": "skipped_rules.txt",
                "ExclusiveRulesFilePath": "",
                "FilterExclusiveRules": False
        }
        self.config.read(configuration_file)
        selected_rules = select_rules(self.rules, self.config)
        self.assertCountEqual([rule_error_test2,
                              rule_error_test3,
                              rule_warning_test1,
                              rule_warning_test3], selected_rules)

    def test_TFFF_08(self):
        #08|T  |F  |F   |F   |All not errors and not warnings
        configuration_file = {
                "Other": True,
                "Errors": False,
                "Warnings": False,
                "SkipRulesFilePath": "",
                "ExclusiveRulesFilePath": "",
                "FilterExclusiveRules": True
        }
        self.config.read(configuration_file)
        selected_rules = select_rules(self.rules, self.config)
        self.assertCountEqual([rule_notcategorized_test1,
                              rule_notcategorized_test2,
                              rule_notcategorized_test3], selected_rules)

    def test_TFFT_09(self):
        #09|T  |F  |F   |T   |All, not errors and not warnings except skipped
        configuration_file = {
                "Other": True,
                "Errors": False,
                "Warnings": False,
                "SkipRulesFilePath": "skipped_rules.txt",
                "ExclusiveRulesFilePath": "",
                "FilterExclusiveRules": False
        }
        self.config.read(configuration_file)
        selected_rules = select_rules(self.rules, self.config)
        self.assertCountEqual([rule_notcategorized_test1,
                              rule_notcategorized_test2], selected_rules)

    def test_TFTF_10(self):
        #10|T  |F  |T   |F   |All, not errors
        configuration_file = {
                "Other": True,
                "Errors": False,
                "Warnings": True,
                "SkipRulesFilePath": "",
                "ExclusiveRulesFilePath": "",
                "FilterExclusiveRules": True
        }
        self.config.read(configuration_file)
        selected_rules = select_rules(self.rules, self.config)
        self.assertCountEqual([rule_warning_test1,
                              rule_warning_test2,
                              rule_warning_test3,
                              rule_notcategorized_test1,
                              rule_notcategorized_test2,
                              rule_notcategorized_test3], selected_rules)

    def test_TFTT_11(self):
        #11|T  |F  |T   |T   |All, not errors, except skipped
        configuration_file = {
                "Other": True,
                "Errors": False,
                "Warnings": True,
                "SkipRulesFilePath": "skipped_rules.txt",
                "ExclusiveRulesFilePath": "",
                "FilterExclusiveRules": False
        }
        self.config.read(configuration_file)
        selected_rules = select_rules(self.rules, self.config)
        self.assertCountEqual([rule_warning_test1,
                              rule_warning_test3,
                              rule_notcategorized_test1,
                              rule_notcategorized_test2], selected_rules)

    def test_TTFF_12(self):
        #12|T  |T  |F   |F   |All, not warnings
        configuration_file = {
                "Other": True,
                "Errors": True,
                "Warnings": False,
                "SkipRulesFilePath": "",
                "ExclusiveRulesFilePath": "",
                "FilterExclusiveRules": True
        }
        self.config.read(configuration_file)
        selected_rules = select_rules(self.rules, self.config)
        self.assertCountEqual([rule_error_test1,
                              rule_error_test2,
                              rule_error_test3,
                              rule_notcategorized_test1,
                              rule_notcategorized_test2,
                              rule_notcategorized_test3], selected_rules)

    def test_TTFT_13(self):
        #13|T  |T  |F   |T   |All, not warnings, except skipped
        configuration_file = {
                "Other": True,
                "Errors": True,
                "Warnings": False,
                "SkipRulesFilePath": "skipped_rules.txt",
                "ExclusiveRulesFilePath": "",
                "FilterExclusiveRules": False
        }
        self.config.read(configuration_file)
        selected_rules = select_rules(self.rules, self.config)
        self.assertCountEqual([rule_error_test2,
                              rule_error_test3,
                              rule_notcategorized_test1,
                              rule_notcategorized_test2], selected_rules)

    def test_TTTF_14(self):
        #14|T  |T  |T   |F   |All
        configuration_file = {
                "Other": True,
                "Errors": True,
                "Warnings": True,
                "SkipRulesFilePath": "",
                "ExclusiveRulesFilePath": "",
                "FilterExclusiveRules": True
        }
        self.config.read(configuration_file)
        selected_rules = select_rules(self.rules, self.config)
        self.assertCountEqual([rule_error_test1,
                              rule_error_test2,
                              rule_error_test3,
                              rule_warning_test1,
                              rule_warning_test2,
                              rule_warning_test3,
                              rule_notcategorized_test1,
                              rule_notcategorized_test2,
                              rule_notcategorized_test3], selected_rules)

    def test_TTTT_15(self):
        #15|T  |T  |T   |T   |All, except skipped
        configuration_file = {
                "Other": True,
                "Errors": True,
                "Warnings": True,
                "SkipRulesFilePath": "skipped_rules.txt",
                "ExclusiveRulesFilePath": "",
                "FilterExclusiveRules": False
        }
        self.config.read(configuration_file)
        selected_rules = select_rules(self.rules, self.config)
        self.assertCountEqual([rule_error_test2,
                              rule_error_test3,
                              rule_warning_test1,
                              rule_warning_test3,
                              rule_notcategorized_test1,
                              rule_notcategorized_test2], selected_rules)

if __name__ == "__main__":
    #unittest.main()

    suite = unittest.TestLoader().loadTestsFromTestCase(TestSelectRulesDirectlyFromRulesModule)
    unittest.TextTestRunner(verbosity=2).run(suite)
