import streamlit as st
import matplotlib.pyplot as plt

st.set_page_config(page_title="🩺 나만의 건강 체크리스트", layout="centered")
st.title("🩺 나만의 건강 체크리스트 (100점 만점)")

st.markdown("오늘의 건강 상태를 체크하고 100점 만점 기준으로 점수를 확인해보세요!")

# 1. 사용자 입력
water = st.slider("💧 물 섭취량 (ml, 최대 2L)", 0, 2000, 100, step=100)
exercise = st.slider("🏃‍♂️ 운동 시간 (분, 최대 120분)", 0, 120, 30, step=5)
sleep = st.slider("🛌 수면 시간 (시간, 최대 10시간)", 0, 10, 7, step=0.5)
stress = st.slider("😰 스트레스 수준 (0=낮음, 10=높음)", 0, 10, 5)
fruits = st.slider("🍎 과일/채소 섭취 횟수 (0~5회)", 0, 5, 2)

# 2. 점수 계산 (각 항목 최대 20점)
water_score = (water / 2000) * 20
exercise_score = (exercise / 120) * 20
sleep_score = (sleep / 10) * 20
stress_score = ((10 - stress) / 10) * 20
fruits_score = (fruits / 5) * 20

total_score = water_score + exercise_score + sleep_score + stress_score + fruits_score

# 3. 건강 상태 이모티콘
if total_score <= 40:
    emoji = "🛑⚠️😰 건강 주의"
elif total_score <= 70:
    emoji = "🟡🙂⚖️ 건강 보통"
else:
    emoji = "✅😄🌟 건강 양호"

# 4. 결과 출력
st.markdown(f"### 오늘 건강 점수: {total_score:.1f}/100")
st.markdown(f"<h2>{emoji}</h2>", unsafe_allow_html=True)

# 5. 시각화 - 막대 그래프
categories = ["💧 물", "🏃‍♂️ 운동", "🛌 수면", "😰 스트레스", "🍎 과일/채소"]
scores = [water_score, exercise_score, sleep_score, stress_score, fruits_score]

# 그래프 색상 설정 (총점 기준)
if total_score <= 40:
    color = 'red'
elif total_score <= 70:
    color = 'yellow'
else:
    color = 'green'

plt.figure(figsize=(6,4))
plt.bar(categories, scores, color=[color]*5)
plt.ylim(0, 20)
plt.ylabel("점수 (0~20)")
plt.title("오늘 건강 체크 항목 점수")
st.pyplot(plt)
