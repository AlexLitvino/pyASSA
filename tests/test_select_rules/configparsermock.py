class ConfigparserMock:
    """
    Class that mocks configuration file for testing select_rules function
    >>> configparser = ConfigparserMock()
    >>> config = configparser.ConfigParser()
    >>> configuration_file = {
    ...        "Other": False,
    ...        "Errors": False,
    ...        "Warnings": False,
    ...        "SkipRulesFilePath": "real_skip_file.txt",
    ...        "ExclusiveRulesFilePath": "real_exclusive_file.txt",
    ...        "FilterExclusiveRules": True
    ... }
    >>> config.read(configuration_file)
    >>> config["RULES"].getboolean("Errors")
    False
    >>> config["RULES"]["SkipRulesFilePath"]
    'real_skip_file.txt'
    """
    class ConfigParser(dict):
        def read(self, configuration_file):
            class RulesImplementation(dict):
                def __init__(self, **kwargs):
                    super().__init__(**kwargs)
                    self["SkipRulesFilePath"] = configuration_file["SkipRulesFilePath"]
                    self["ExclusiveRulesFilePath"] = configuration_file["ExclusiveRulesFilePath"]

                @staticmethod
                def getboolean(item):
                    return configuration_file[item]
            self["RULES"] = RulesImplementation()

if __name__ == "__main__":
    import doctest
    doctest.testmod()
