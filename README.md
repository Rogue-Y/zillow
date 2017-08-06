# kaggle-zillow

May the Randomness be with us
====================

Data dictionary exploration: on Google sheet
https://docs.google.com/spreadsheets/d/1_EHvgdIrkDVPs4p98cPQ26inMz349SIioesTD6B7oHw/edit#gid=1497391001

Asana task list
https://app.asana.com/0/389439275300204/board

The jupyter notebooks are in the notebooks folder. To import our modules correctly in the
notebooks, add the following code at the beginning:
<code>
import os
import sys
module_path = os.path.abspath(os.path.join('..'))
if module_path not in sys.path:
    sys.path.append(module_path)
</code>
Also, pass '../data' as data folder to the <code>utils</code>'s load data functions.

Some caveat in the code:
1. please use keyword argument;
2. please do not alter the config JSON object, so that the auto change detection
in main.py works properly
3. when change data processing code without change steps in config file, please set
force_process_data in config to true, or the processing training data step will
be skipped, since there's no change in processing steps;
4. please use single-quote(') for string object, except python doc, use
triple-quote(""") for that;
5. need everyone's Ok before merge to master;
