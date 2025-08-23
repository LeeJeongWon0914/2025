import streamlit as st
import pandas as pd

st.title("🌱 나만의 건강 체크리스트")

# 사용자 입력
water = st.slider("💧 물 섭취 (ml, 목표 2000ml)", 0, 2000, 1000, step=100)
exercise = st.slider("🏃 운동 (분, 목표 120분)", 0, 120, 30, step=5)
sleep = st.slider("🛌 수면 시간 (시간, 목표 8시간)", 0.0, 12.0, 7.0, step=0.5)
stress = st.slider("😰 스트레스 (0=낮음, 10=높음)", 0, 10, 5)
fruits = st.slider("🍎 과일/채소 섭취 (횟수, 목표 5회)", 0, 5, 2)

# 점수 계산 (100점 만점)
water_score = (water / 2000) * 100
exercise_score = (exercise / 120) * 100
sleep_score = (sleep / 8) * 100
stress_score = ((10 - stress) / 10) * 100
fruits_score = (fruits / 5) * 100

scores = {
    "물": water_score,
    "운동": exercise_score,
    "수면": sleep_score,
    "스트레스": stress_score,
    "과일/채소": fruits_score,
}

total_score = sum(scores.values()) / len(scores)

# 점수 색/이모지 피드백
if total_score <= 40:
    status = "🔴 주의! 생활습관을 개선해보세요."
elif total_score <= 70:
    status = "🟡 보통! 조금만 더 노력해봐요."
else:
    status = "🟢 좋음! 건강한 생활을 유지하세요."

st.subheader(f"오늘의 건강 점수: {total_score:.1f}/100")
st.write(status)

# 그래프 표시
df = pd.DataFrame(list(scores.items()), columns=["항목", "점수"]).set_index("항목")
st.bar_chart(df)
