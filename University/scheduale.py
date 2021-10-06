from operator import itemgetter
from itertools import groupby

exams = [

    {'profession': 'macro_eco', 'date': '02/09'},
    {'profession': 'macro_eco', 'date': '18/10'},
    {'profession': 'macro_eco', 'date': '25/11'},
    {'profession': 'research_methods', 'date' : '23/08'},
    {'profession': 'org_macro', 'date': '04/10'},
    {'profession': 'org_macro', 'date': '21/10'},
    {'profession': 'org_macro', 'date': '25/10'},
    {'profession': 'tech_inovation', 'date': '04/10-11/10'},
    {'profession': 'tech_inovation', 'date': '22/10-29/10'},
    {'profession': 'statistics_b', 'date': '11/10'},
    {'profession': 'statistics_b', 'date': '25/11'},
]

# sort by the desired field first
exams.sort(key=itemgetter('date'))

for date, items in groupby(exams, key=itemgetter('date')):
 print(date)
 for i in items:
    print('     ', i)


