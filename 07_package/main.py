import team_management.developers as td
import team_management.managers as tm

print(tm.managers())
print(td.developers())



import work_management.reporting as wme
import work_management.task_tracking as wmt

task = "코드리뷰"

print(wmt.start_task(task))
print(wmt.end_task(task))
print(wme.generate_report(task))

#for i, work in enumerate([st, et, gr]):
#print(work('코드리뷰'))

#for work in [st, et, gr]:
#print(work('코드리뷰'))


import schedule_management.calander as smc
from datetime import datetime as dt

event = "회의"
date = dt.now().strftime("%Y-%m-%d")

print(smc.add_event(event, date))
print(smc.remove_event(event))

#from schedule_management.calander import add_event as ae, remove_event as re
#print(ae('회의', '2015-09-30'))
#print(re('회의'))

import numpy

x = [10,4,7,8,9]

averg = numpy.mean(x)
print(averg)

#import numpy as np

#numbers = [10, 20, 30, 40, 50]
#print(np.mean(numbers))