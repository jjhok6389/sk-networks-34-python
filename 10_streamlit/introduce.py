import streamlit as st

st.title("안녕하세요, 김대호입니다 💻")
st.markdown("""
창업가가 되는게 목표입니다.
    """)
# 전자공학과 컴퓨터공학 지식을 바탕으로 하드웨어와 소프트웨어, \n
# 그리고 AI를 결합해 실질적인 가치를 창출하는 풀스택 및 모바일 개발자입니다.\n
# 팩트에 기반한 명료하고 효율적인 문제 해결을 지향합니다.\n
st.divider()


st.header("기본 정보 및 역량")
col1, col2 = st.columns(2)

with col1:
    st.subheader("👨‍💻 Profile")
    
    st.image("common.jpeg", width=140)
    st.write("**이름:** 김대호")
    st.write("**MBTI:** INFJ")
    st.write("**거주지:** 파주")
    st.balloons()
    st.divider()
    st.write("**포지션:** Full-Stack & Mobile Developer")
    st.divider()
    st.write("**취미:** 축구보기")
    st.write("**강점:** 끈기")
    st.write("**약점:** 공부")
    st.divider()
    st.write("**주요 이력:**")
    # st.write("- 2024 교내 창업 아이디어 경진대회 동상 수상")
    # st.write("- 2024 교내 IR 피칭 경진대회 동상 수상")
    # st.write("- 2025 학생 포트폴리오 경진대회 한국공학교육인증원장상 수상")
    # st.write("- 2025 산업체 수요특화형(IoT) 스마트홈 구축 아이디어 경진대회 금상 수상")
    # st.write("- 2026 교내 학습동아리 우수 동아리 선정 대상 수상")
    # st.write("- 공학페스티벌 심사위원 ")
    st.write("숨쉬기")
    st.write("밥먹기")
    st.write("잘자기")
with col2:
    st.subheader("💡 Interests & Tech")
  
    st.write("**관심 분야:**")  
    st.write("창업")
    st.write("AI")
    st.divider()
    st.write("**기술 스택:**")
    st.write("- **Mobile:** Flutter, React Native, Kotlin(Jetpack Compose)")
    st.write("- **Backend:** Java Spring Boot, Python, Firebase")
    st.write("- **Hardware:** Arduino, ESP32")
    st.divider()
st.divider()


st.header("오늘의 상태 체크 ✔️")

resolution = st.text_input("오늘의 한 줄 다짐을 적어주세요:")

if resolution:
    st.success(f"오늘의 다짐: **[{resolution}]** - 계획하신 바를 이룰 수 있도록 응원합니다.")
    st.balloons()
# import streamlit as st
# import random
# import pandas as pd
# import time

# # --- 페이지 설정 ---
# st.set_page_config(page_title="2026 월드컵 실시간 예측기", page_icon="🏆", layout="wide")

# # --- 세션 상태 초기화 ---
# if 'simulated' not in st.session_state:
#     st.session_state.simulated = False
#     st.session_state.results = {}

# # --- 현재 순위 데이터 (2026.06.24 기준 2차전 완료 상태) ---
# # 각 팀의 현재 승점(pts), 득실차(gd), 득점(gf)을 기록
# def get_current_standings():
#     return {
#         "A조": [
#             {"team": "🇲🇽 멕시코", "pts": 6, "gd": 3, "gf": 3},
#             {"team": "🇰🇷 대한민국", "pts": 3, "gd": 0, "gf": 2},
#             {"team": "🇨🇿 체코", "pts": 1, "gd": -1, "gf": 2},
#             {"team": "🇿🇦 남아공", "pts": 1, "gd": -2, "gf": 1}
#         ],
#         "B조": [
#             {"team": "🇨🇦 캐나다", "pts": 4, "gd": 6, "gf": 7},
#             {"team": "🇨🇭 스위스", "pts": 4, "gd": 3, "gf": 5},
#             {"team": "🇧🇦 보스니아", "pts": 1, "gd": -3, "gf": 2},
#             {"team": "🇶🇦 카타르", "pts": 1, "gd": -6, "gf": 1}
#         ],
#         "C조": [
#             {"team": "🇧🇷 브라질", "pts": 4, "gd": 3, "gf": 4},
#             {"team": "🇲🇦 모로코", "pts": 4, "gd": 1, "gf": 2},
#             {"team": "🏴󠁧󠁢󠁳󠁣󠁴󠁿 스코틀랜드", "pts": 3, "gd": 0, "gf": 1},
#             {"team": "🇭🇹 아이티", "pts": 0, "gd": -4, "gf": 0}
#         ],
#         "D조": [
#             {"team": "🇺🇸 미국", "pts": 6, "gd": 5, "gf": 6},
#             {"team": "🇦🇺 호주", "pts": 3, "gd": 0, "gf": 2},
#             {"team": "🇵🇾 파라과이", "pts": 3, "gd": -2, "gf": 2},
#             {"team": "🇹🇷 튀르키예", "pts": 0, "gd": -3, "gf": 0}
#         ],
#         "E조": [
#             {"team": "🇩🇪 독일", "pts": 6, "gd": 7, "gf": 9},
#             {"team": "🇨🇮 코트디부아르", "pts": 3, "gd": 0, "gf": 2},
#             {"team": "🇪🇨 에콰도르", "pts": 1, "gd": -1, "gf": 0},
#             {"team": "🇨🇼 퀴라소", "pts": 1, "gd": -6, "gf": 1}
#         ],
#         "F조": [
#             {"team": "🇳🇱 네덜란드", "pts": 4, "gd": 4, "gf": 7},
#             {"team": "🇯🇵 일본", "pts": 4, "gd": 4, "gf": 6},
#             {"team": "🇸🇪 스웨덴", "pts": 3, "gd": 0, "gf": 6},
#             {"team": "🇹🇳 튀니지", "pts": 0, "gd": -8, "gf": 1}
#         ],
#         "G조": [
#             {"team": "🇪🇬 이집트", "pts": 4, "gd": 2, "gf": 4},
#             {"team": "🇮🇷 이란", "pts": 2, "gd": 0, "gf": 2},
#             {"team": "🇧🇪 벨기에", "pts": 2, "gd": 0, "gf": 1},
#             {"team": "🇳🇿 뉴질랜드", "pts": 1, "gd": -2, "gf": 3}
#         ],
#         "H조": [
#             {"team": "🇪🇸 스페인", "pts": 4, "gd": 4, "gf": 4},
#             {"team": "🇺🇾 우루과이", "pts": 2, "gd": 0, "gf": 3},
#             {"team": "🇨🇻 카보베르데", "pts": 2, "gd": 0, "gf": 2},
#             {"team": "🇸🇦 사우디", "pts": 1, "gd": -4, "gf": 1}
#         ],
#         "I조": [
#             {"team": "🇫🇷 프랑스", "pts": 6, "gd": 5, "gf": 6},
#             {"team": "🇳🇴 노르웨이", "pts": 6, "gd": 4, "gf": 7},
#             {"team": "🇸🇳 세네갈", "pts": 0, "gd": -3, "gf": 3},
#             {"team": "🇮🇶 이라크", "pts": 0, "gd": -6, "gf": 1}
#         ],
#         "J조": [
#             {"team": "🇦🇷 아르헨티나", "pts": 6, "gd": 5, "gf": 5},
#             {"team": "🇦🇹 오스트리아", "pts": 3, "gd": 0, "gf": 3},
#             {"team": "🇩🇿 알제리", "pts": 3, "gd": -2, "gf": 2},
#             {"team": "🇯🇴 요르단", "pts": 0, "gd": -3, "gf": 2}
#         ],
#         "K조": [
#             {"team": "🇨🇴 콜롬비아", "pts": 6, "gd": 3, "gf": 4},
#             {"team": "🇵🇹 포르투갈", "pts": 4, "gd": 5, "gf": 6},
#             {"team": "🇨🇩 DR 콩고", "pts": 1, "gd": -1, "gf": 1},
#             {"team": "🇺🇿 우즈베키스탄", "pts": 0, "gd": -7, "gf": 1}
#         ],
#         "L조": [
#             {"team": "🏴󠁧󠁢󠁥󠁮󠁧󠁿 잉글랜드", "pts": 4, "gd": 2, "gf": 4},
#             {"team": "🇬🇭 가나", "pts": 4, "gd": 1, "gf": 1},
#             {"team": "🇭🇷 크로아티아", "pts": 3, "gd": -1, "gf": 3},
#             {"team": "🇵🇦 파나마", "pts": 0, "gd": -2, "gf": 0}
#         ]
#     }

# # --- 시뮬레이션 함수 ---
# def simulate_match(t1, t2, is_knockout=False):
#     """두 팀 간의 랜덤 경기 결과를 반환"""
#     s1 = random.choices([0, 1, 2, 3, 4], weights=[20, 30, 25, 15, 10])[0]
#     s2 = random.choices([0, 1, 2, 3, 4], weights=[20, 30, 25, 15, 10])[0]
    
#     if is_knockout and s1 == s2:
#         s1 += 1  # 토너먼트는 무승부 시 한 팀이 연장/승부차기로 승리
        
#     return {"team1": t1, "team2": t2, "score": f"{s1} : {s2}", "s1": s1, "s2": s2}

# def run_simulation():
#     current_standings = get_current_standings()
#     final_standings = {}
#     advanced_teams = []
#     third_places = []
    
#     # 1. 조별리그 3차전 시뮬레이션 및 최종 순위 결정
#     for group, teams in current_standings.items():
#         # 임의의 3차전 대진 (1위 vs 4위, 2위 vs 3위로 가정)
#         m1 = simulate_match(teams[0]["team"], teams[3]["team"])
#         m2 = simulate_match(teams[1]["team"], teams[2]["team"])
        
#         # 경기 결과를 기존 데이터에 합산
#         def update_stats(match):
#             t1, t2, s1, s2 = match["team1"], match["team2"], match["s1"], match["s2"]
#             for t in teams:
#                 if t["team"] == t1:
#                     t["gf"] += s1
#                     t["gd"] += (s1 - s2)
#                     if s1 > s2: t["pts"] += 3
#                     elif s1 == s2: t["pts"] += 1
#                 elif t["team"] == t2:
#                     t["gf"] += s2
#                     t["gd"] += (s2 - s1)
#                     if s2 > s1: t["pts"] += 3
#                     elif s2 == s1: t["pts"] += 1
                    
#         update_stats(m1)
#         update_stats(m2)
        
#         # 최종 순위 정렬 (승점 > 득실차 > 다득점 순)
#         sorted_teams = sorted(teams, key=lambda x: (x["pts"], x["gd"], x["gf"]), reverse=True)
#         final_standings[group] = sorted_teams
        
#         # 1, 2위 진출
#         advanced_teams.extend([sorted_teams[0]["team"], sorted_teams[1]["team"]])
#         # 3위 팀 별도 보관 (와일드카드 경쟁)
#         third_places.append(sorted_teams[2])

#     # 3위 팀 중 상위 8팀을 와일드카드로 선발
#     third_places = sorted(third_places, key=lambda x: (x["pts"], x["gd"], x["gf"]), reverse=True)
#     lucky_thirds = [t["team"] for t in third_places[:8]]
#     advanced_teams.extend(lucky_thirds)
    
#     # 대진표 섞기
#     random.shuffle(advanced_teams)
    
#     # 2. 32강 토너먼트 진행
#     rounds = {"32강": advanced_teams}
#     stage_names = ["32강", "16강", "8강", "4강", "결승"]
#     match_history = {}
    
#     for i in range(len(stage_names)):
#         current_stage = stage_names[i]
#         current_teams = rounds[current_stage]
#         next_teams = []
#         match_history[current_stage] = []
        
#         for j in range(0, len(current_teams), 2):
#             if j+1 < len(current_teams):
#                 t1, t2 = current_teams[j], current_teams[j+1]
#                 res = simulate_match(t1, t2, is_knockout=True)
#                 winner = res["team1"] if res["s1"] > res["s2"] else res["team2"]
#                 next_teams.append(winner)
#                 match_history[current_stage].append({
#                     "match": f"{t1} vs {t2}", 
#                     "score": res["score"], 
#                     "winner": winner
#                 })
        
#         if i + 1 < len(stage_names):
#             rounds[stage_names[i+1]] = next_teams
#         else:
#             champion = next_teams[0]

#     st.session_state.results = {
#         "groups": final_standings,
#         "lucky_thirds": lucky_thirds,
#         "history": match_history,
#         "champion": champion
#     }
#     st.session_state.simulated = True


# # --- UI 레이아웃 ---
# st.title("⚽ 2026 실시간 월드컵 예측기")
# st.markdown("현재(2차전 완료 기준) 실제 순위표의 **승점과 득실차**를 바탕으로 남은 3차전과 토너먼트를 시뮬레이션합니다.")

# if st.button("🎲 3차전 및 토너먼트 시뮬레이션 돌리기", use_container_width=True, type="primary"):
#     with st.spinner('남은 경기 결과를 계산하고 있습니다...'):
#         time.sleep(1.5)
#         run_simulation()

# if st.session_state.simulated:
#     res = st.session_state.results
    
#     tab1, tab2, tab3 = st.tabs(["🏆 최종 우승국", "⚔️ 토너먼트 결과", "📊 조별리그 최종 순위표"])
    
#     with tab1:
#         st.subheader("🎉 2026 월드컵 시뮬레이션 챔피언")
#         st.success(f"### 🏆 우승: {res['champion']}")
#         st.balloons()
        
#         st.subheader("결승전 스코어")
#         final_match = res["history"]["결승"][0]
#         st.info(f"**{final_match['match']}** ➡️ {final_match['winner']} 승리! (스코어 {final_match['score']})")

#     with tab2:
#         st.subheader("🔥 넉아웃 스테이지 대진")
#         stages = ["4강", "8강", "16강", "32강"]
        
#         for stage in stages:
#             with st.expander(f"{stage} 경기 결과", expanded=(stage=="4강")):
#                 cols = st.columns(2)
#                 for idx, match in enumerate(res["history"][stage]):
#                     col = cols[idx % 2]
#                     col.markdown(f"**{match['match']}**")
#                     col.caption(f"스코어: {match['score']} 👉 **{match['winner']}** 진출")
#                     col.divider()

#     with tab3:
#         st.subheader("📋 시뮬레이션 반영 조별리그 최종 순위")
#         st.caption("실제 2차전 데이터 + 가상의 3차전 결과가 합산된 순위입니다. (1위, 2위 및 🎟️와일드카드 진출)")
        
#         group_names = list(res["groups"].keys())
#         for i in range(0, 12, 3):
#             cols = st.columns(3)
#             for j in range(3):
#                 g_name = group_names[i+j]
#                 teams = res["groups"][g_name]
#                 with cols[j]:
#                     st.markdown(f"**{g_name}**")
#                     for rank, t in enumerate(teams):
#                         medal = ["🥇", "🥈", "🥉", "4️⃣"][rank]
#                         wc_icon = " 🎟️" if rank == 2 and t["team"] in res["lucky_thirds"] else ""
#                         st.write(f"{medal} {t['team']} (승점 {t['pts']} / 득실 {t['gd']}){wc_icon}")
#                     st.divider()
