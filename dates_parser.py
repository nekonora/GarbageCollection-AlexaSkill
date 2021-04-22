# CVS date parser

import csv

def get_garbage_at_date(provided_date):
    with open('calendar.csv', mode='r') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            # date is column 0, garbage is column 1
            if row['date'] == provided_date:
                return row['garbage']
        return "Nessuna spazzatura!"