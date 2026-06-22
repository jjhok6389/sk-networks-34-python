import team_module as tm

print(f"안녕하세요 {tm.company} 입니다.")
print(tm.introduce_manager())
print(tm.introduce_developer())

print("-------------------------------------")


import attendance_module as am

print(am.record_attendance("카피바라","9:00"))
print(am.record_leave("카피바라","18:00"))

print("-------------------------------------")


import task_module as taskm

print(taskm.start_task("코드 리뷰"))
print(taskm.complete_task("코드 리뷰"))

print("-------------------------------------")

import math

works=[10, 12, 8, 15, 9]

#평균 업무량 (총 합 sum /갯수 len) 출력

aver_work = sum(works)/len(works)
print(aver_work)

#평균 업무량보다 많이 처리한 날짜 (비교: 평균업무량 vs 일일업무량)
count = 0
for work in works:
    if work > aver_work:
        count += 1
print(f"평균 업무량보다 많이 처리한 날 : {count}")

print("-------------------------------------")

from datetime import datetime as dt

print("[",dt.now().strftime("%Y-%m-%d %H:%M:%S"),"] 카피바라님이 작업 '코드리뷰'을(를) 완료했습니다.")
