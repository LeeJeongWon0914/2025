import streamlit as st
import pandas as pd
import altair as alt

st.set_page_config(page_title="나만의 건강 체크리스트", page_icon="🩺", layout="centered")

# 초기 세션 상태 설정
if "step" not in st.session_state:
    st.session_state.step = 0
if "answers" not in st.session_state:
    st.session_state.answers = {}

def next_step():
    st.session_state.step += 1

# 단계별 화면
st.title("🩺 나만의 건강 체크리스트")

# 0단계: 시작 화면
if st.session_state.step == 0:
    st.write("당신의 오늘 하루 건강 상태를 간단하게 체크해보세요!")
    if st.button("시작하기 🚀"):
        next_step()

# 1단계: 물 섭취량
elif st.session_state.step == 1:
    st.session_state.answers["water"] = st.slider("💧 물 섭취 (ml, 목표 2000ml)", 0, 2000, 1000, step=100)
    if st.button("다음 ➡️"):
        next_step()

# 2단계: 운동
elif st.session_state.step == 2:
    st.session_state.answers["exercise"] = st.slider("🏃 운동 시간 (분, 목표 30분)", 0, 120, 30, step=10)
    if st.button("다음 ➡️"):
        next_step()

# 3단계: 수면
elif st.session_state.step == 3:
    st.session_state.answers["sleep"] = st.slider("🛌 수면 시간 (시간, 목표 8시간)", 0.0, 12.0, 7.0, step=0.5)
    if st.button("다음 ➡️"):
        next_step()

# 4단계: 스트레스
elif st.session_state.step == 4:
    st.session_state.answers["stress"] = st.slider("😫 스트레스 정도 (0=전혀 없음, 10=매우 심함)", 0, 10, 5)
    if st.button("다음 ➡️"):
        next_step()

# 5단계: 과일/채소 섭취
elif st.session_state.step == 5:
    st.session_state.answers["veggie"] = st.slider("🥦 과일/채소 섭취 (회/일, 목표 5회)", 0, 10, 3)
    if st.button("결과 보기 🎉"):
        next_step()

# 6단계: 결과
elif st.session_state.step == 6:
    st.subheader("📊 오늘의 건강 점수")

    # 점수 계산 (각 항목 20점 만점)
    water_score = min(st.session_state.answers["water"] / 2000 * 20, 20)
    exercise_score = min(st.session_state.answers["exercise"] / 30 * 20, 20)
    sleep_score = min(st.session_state.answers["sleep"] / 8 * 20, 20)
    stress_score = (10 - st.session_state.answers["stress"]) / 10 * 20
    veggie_score = min(st.session_state.answers["veggie"] / 5 * 20, 20)

    total_score = round(water_score + exercise_score + sleep_score + stress_score + veggie_score)

    # 점수별 이모지 피드백
    if total_score <= 40:
        status = "🔴 주의! 오늘은 건강 관리가 필요해요."
    elif total_score <= 70:
        status = "🟡 보통! 조금 더 신경쓰면 좋아요."
    else:
        status = "🟢 아주 좋아요! 건강 습관을 잘 지키고 있어요."

    st.metric("오늘의 점수", f"{total_s_
