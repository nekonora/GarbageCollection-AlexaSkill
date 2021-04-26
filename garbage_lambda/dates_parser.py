# CVS date parser

import csv
import data_models
import os

def get_garbage_at_date(provided_date):
    """Return a `list` of `GarbageType` for the provided date in format 'YYYY-MM-DD'

    Args:
        `provided_date`: the date to inspect
    Returns:
        `[GarbageType]`
    
    """

    this_folder = os.path.dirname(os.path.abspath(__file__))
    calendar_file = os.path.join(this_folder, 'calendar.csv')

    with open(calendar_file, mode='r') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            # date is column 0, garbage is column 1
            if row['date'] == provided_date:
                gargbageIds = list(map(int,row['garbage'].split(";")))
                garbageList = list(map(data_models.GarbageType, gargbageIds))
                
                return garbageList
        return []