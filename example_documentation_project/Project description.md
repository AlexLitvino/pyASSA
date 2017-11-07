## Reports validation

### Project description

Example not so real, but just to show what could be done.

Almost all companies are using bug tracking systems.
But imagine, that not all:)

Company WeDontUseBugtracker.com uses emails for notifying about found defects.
Before release all emails should be saved in special location,
**AND**
these email should be correct from the special point of view.

When testers create defect reports, they know rules they should follow.
But human factor plays some role and not all reports are correct.

So we need to go through each report and check if it is correct.
For example, several hundreds of reports((

Reports should follow special format:
- Summary: Not empty string and not more than 20 words.
- Feature: Feature_1, Feature2, Feature_3 - if Type=Defect, N/A - if Type=Enhancement
- Type: Defect or Enhancement
- Build Number: Number.Number.Number if Type=Defect or N/A if Type=Enhancement
- Priority: Low, Medium, High
- Reported By: Not empty string
- Reported On: Date in format MM-DD-YYYY
- Environment: Not empty string if Type=Defect, string if Type=Enhancement
- Description: Not empty string
- Steps To Reproduce: String
All fields should be in the order above and separated by at least one empty string.

### How it is implemented

Two modules should be updated with this project specific implementation:
1. `\customization\custom_utils.py`
- Function `is_script(root, full_file_name)` implements decision is found file a report using path to the file.
Report should follow Issue_<IssueNumber>.txt name convention to be a report.
- Function `get_configuration_parameters(config)` adds project specific parameters features and priorities from config.ini file to kwargs parameter that could be used in rules. 
- Function `get_script(script_path)` return list of lines from report file for further analysis.
- Function `report_parser(report)` is this project specific function that parses list of reports lines into dictionary {section_name: section_value}.
2. `\customization\rules_definition.py`
- Implementation of required rules as functions:
    - Description added by decorator;
    - Name of function reflects rule;
    - At first parsed_report is taken from report lines:
    ```
    report = kwargs["script"]
    parsed_report = report_parser(report)
     ```
    *NOTE: this operation could be made in `get_script(script_path)` function and parsed data will be sent to every rule - kind of optimization. Why I send not parsed data to every rule is because we could have a rule that will check structure of report - all required sections, their orders. But for this case we also could add to kwargs parsed data as "script" variable  because it is used more often - and other variable with not parsed data. Here the place where you could make optimization for analysis running - perform most general evaluation before sending data to rules functions.*

### How to run this project
1. Replace directory `pyASSA\customization` with directory `pyASSA\example_documentation_project\customization`. 
2. Replace `pyASSA\configuration\config.ini` file with `pyASSA\example_documentation_project\config.ini` file.
3. Run `pyASSA\assa.py` module.
4. Find report in `pyASSA\reports` directory.

##### P.S. It is example. Everything could be improved :)

