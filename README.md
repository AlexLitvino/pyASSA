# pyASSA

## Description
pyASSA is a framework for static analysis.
When you writing code on Java, C# or Python, IDE could help you with finding issues.
But if your results are not supported by existing tool?
Or existing tool doesn't support finding specific issue?
Usually you should perform review of such documents.
You have a checklist and go across the document checking it against checklist.

For example, you have a set of text documents that was created manually and later should be imported to special tool.
There's a formal rule on your project - some field shouldn't be empty or should have value from predefined list.
Data from text documents could be uploaded to tool "as is".
Or tool could raise exception if imported data is not supported.
Wouldn't it be better to correct all text documents before importing?
(See example #1)

Another example.
You are writing system to control kind of a robot.
End-users don't have programming skills.
So you prepare parser for spreadsheets, where end-users could write simple command sequence.
Finally, you have a library of such command sequences, but not sure if they valid.
You don't want to run every sequence and check if robot will act.
So you could write several rules that will find some simple errors.
(See example #2)

NOTE: Below by "script" term, I will mean any document with specific structure that should follow some formal rules.


## Features:
- Static analysis of scripts from selected directory (recursively) against user defined rules;
- Presenting results as a text file.


## Environment and Dependencies
Project is written on pure Python. No additional libs are required.
But additional libs cold be needed for implementation project specific rules.
Tested on Python 3.5.2, Windows 7.


## Hello, World!
Just to make sure that project is doing something, you could run `assa.py` module from the project root directory.
`path_to_pyASSA_directory_on_your_machine\pyASSA> python assa.py`
What it will do?
- It takes project working directory as a directory that contains scripts to be checked.
- It finds all scripts that have file extension `.py`
- It runs rules stubs against all found `*.py` scripts.
- It creates directory `report` with result log, named `assa_\*.log`.
 
 
## Examples

#### Example #1
[Report validation project](example_documentation_project/Project%20description.md)  
Example located at `pyASSA\example_documentation_project` directory

#### Example #2
[Robot scenario validation project](example_robot_project/Project%20description.md)  
Example located at `pyASSA\example_robot_project` directory


## Project structure
Project divided into core part and customization part.

Core part consists of
`assa.py` - entry point, functions that collect data from configuration file and run script check against rules.
`logger.py` - module that configures result an error loggers.
`utils.py` - helper-functions, get/select scripts/rules and other utilities.
`configuration package` - contains files for project configuration:
 - `config.ini` - main parameters
 - all other files (will be defined)
 
 Customization part is taken out to a separate package:
`customization package` - contains modules that should be modified for specific project.
`custom_utils.py` - module contains functions that should be updated for current project (getting configuration data, decision is current file a script, getting/closing script object) and definition of other project needed function could be made here.
`rules_definition.py` - module for rule functions definition. Here `rule_*` functions and private helper-function should be defined.

`/pyASSA/`  
&nbsp;|  
&nbsp;|&mdash;&mdash;&mdash;&mdash;`/pyassa`  
&nbsp;|&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;|  
&nbsp;|&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;|&mdash;`__init__.py`  
&nbsp;|&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;|&mdash;`assa.py`  
&nbsp;|&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;|&mdash;`logger.py`  
&nbsp;|&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;|&mdash;`utils.py`  
&nbsp;|  
&nbsp;|&mdash;&mdash;&mdash;&mdash;`/customization`  
&nbsp;|&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;|  
&nbsp;|&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;|&mdash;`__init__.py`  
&nbsp;|&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;|&mdash;`custom_utils.py`  
&nbsp;|&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;|&mdash;`rules_definition.py`  
&nbsp;|  
&nbsp;|&mdash;&mdash;&mdash;&mdash;`/configuration`  
&nbsp;|&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;|  
&nbsp;|&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;|&mdash;`config.ini`  
&nbsp;|&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;|&mdash;`skipped_rules.txt`  
&nbsp;|  
&nbsp;|&mdash;&mdash;&mdash;&mdash;`/tests`  
&nbsp;|  
&nbsp;|&mdash;&mdash;&mdash;&mdash;`/examples`  
&nbsp;|&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;|  
&nbsp;|&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;|&mdash;`/example_documentation_project`  
&nbsp;|&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;|&mdash;`/example_robot_project`  
&nbsp;|  
&nbsp;|&mdash;&mdash;&mdash;&mdash;`/docs`  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;|  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;|&mdash;`index.md`  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;|&mdash;`selecting_rules.md`  


## How to use:
**<< TODO >>**


## TODO:
Ooh, many things to improve and add enhancements.
Some TODO comments thrown about modules.
Try to collect them here.
- [ ] Nice HTML report
- [ ] Analysis statistics
- [x] Error handling
- [x] Error logging
- [ ] Take reports path from configuration file
- [x] Implement `select_rules` function
- [ ] Implement `select_scripts` function 
- [ ] Change `get_script` and `close_script` to context manager
- [ ] Add specifying configuration file as command line argument
- [ ] Add possibility to run project check against mapping file <script, rule>
- [ ] Mapping file <script, rule> autocreation
- [ ] Add tests
- [ ] Add interactive report with issue status check
- [ ] Improve performance
- [ ] Adding metrics
- [ ] Heatmap (colored mapping <script, rule>) 
