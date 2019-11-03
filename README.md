# Cron Expression Parser
### Parser for scheduling jobs on a Unix system

#### Dependencies

This Expression Parser has been built using Python 3: Version 3.6.8 (default, Oct  7 2019, 12:59:55)

To get the last distribution of Python run:

    sudo apt install python3

#### Run

To run the application, simply execute:

    python3 cron_parser_py3.py <minute> <hour> <day> <month> <dayOfWeek> <command>

'Every' notation "`*/`" is included for each parameter.

#### Testing

Testing is conducted using a separate file and assertions: this one does not accept any tests now.

One mention here: You have a testing variable in the file `cron_parser_optimised.py`. In order to run the tests just change it to `True`.
Otherwise if you want to run the command without testing, change it to `False`.

Testing variable is `False` by default.

    python3 tests.py
