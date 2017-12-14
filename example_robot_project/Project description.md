## Robot control scenarios validation

### Project description

There're a robots on game field. 
Robot should move on specific trajectory and picks some objects.
The trajectory and points of picking-objects defined by users.
Users are not programmers and pretty simple language are created for them.
To control robot, user should specify list of actions that should be applied to robot in Excel file.

Commands to control robot specified in table below:

Command   | Parameter                  | Value                   | Description
---       | ---                        | ---                     | ---
MOVE      |	Forward/Backward	       | Integer >= 0            | Move robot in <Parameter> direction by <Value> length units
ROTATE	  |	Clockwise/Counterclockwise | Integer, 0..360         | Rotate robot in <Parameter> direction by <Value> angle
SET_STATE | Velocity                   | Integer >= 0            | Set robot velocity
SET_STATE | Battery                    | Integer 0.. 100, step=5 | Set robot battery level
TAKE      |	No parameters              | No value                | Picks object if it is located in cell with robot
COMMENT   | No parameters              | Any text                | Print comment text

User defined scenarios should follow rules:

- Should contain only one sheet with name "Scenario";
- First row shall contain column names: "Command", "Parameter", "Value";
- For every row, Command value should NOT be empty;
- For "MOVE" command Parameter could be "Forward" or "Backward", and Value should be Integer greater or equal to zero;
- For "ROTATE" command Parameter could be "Clockwise" or "Counterclockwise", and Value is Integer in range 0 .. 360 (including);
- For "SET_STATE" command Parameter could be "Velocity" or "Battery";
- For "SET_STATE" command with Parameter = "Velocity", Value should be Integer greater or equal to zero;
- For "SET_STATE" command with Parameter = "Battery", Value should be Integer in range 0 ..100 (including), with step 5;
- For "TAKE" command Parameter and Value should be empty;
- For "COMMENT" command Parameter should be empty, and Value could be any string.

### How it is implemented

Two modules should be updated with this project specific implementation:
1. `\customization\custom_utils.py`
- Function `is_script(root, full_file_name)` implements decision is found file a report using path to the file.
Robot scenario should be an Excel file (file with extension 'xls' 'xlsx') and starts with 'RobotScenario_' prefix.
- Function `get_configuration_parameters(config)` adds name of scenario sheet, required headers on scenario sheet and possible commands from config.ini file to kwargs parameter that could be used in rules. 
- Function `get_script(script_path)` returns Excel workbook object for analysis (openpyxl library is used).
And several utility functions that helps to check rules:
- Function `get_rows_list` gets list of rows for specified sheet in workbook.
- Function `get_scenario_header` gets header row (first line) for specified sheet in workbook.
- Function `get_scenario_data` gets list of rows without header for specified sheet in workbook.
- Function `is_int` checks if string is an integer value.  
2. `\customization\rules_definition.py`
- Implementation of required rules as functions:
    - Description added by decorator;
    - Name of function reflects rule.

### How to run this project

##### Dependency
To run this project `openpyxl` library should be installed:
`pip install openpyxl==2.4.8`

1. Replace directory `pyASSA\customization` with directory `pyASSA\example_robot_project\customization`. 
2. Replace `pyASSA\configuration\config.ini` file with `pyASSA\example_robot_project\config.ini` file.
3. Run `pyASSA\assa.py` module.
4. Find report in `pyASSA\reports` directory.


