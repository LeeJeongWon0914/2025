import streamlit as st
import matplotlib.pyplot as plt

st.title("🩺 나만의 건강 체크리스트")

# 1. 사용자 입력
water = st.radio("물 섭취량", [0, 1, 2], format_func=lambda x: ["0~1컵", "2~4컵", "5컵 이상"][x])
exercise = st.radio("운동 시간", [0, 1, 2], format_func=lambda x: ["안함", "30분 이하", "30분 이상"][x])
sleep = st.radio("수면 시간", [0, 1, 2], format_func=lambda x: ["<5시간", "5~7시간", "7시간 이상"][x])
stress = st.radio("스트레스 수준", [0, 1, 2], format_func=lambda x: ["높음", "보통", "낮음"][x])
fruits = st.radio("과일/채소 섭취", [0, 1, 2], format_func=lambda x: ["0~1회", "2~3회", "4회 이상"][x])

# 2. 점수 계산
total_score = water + exercise + sleep + stress + fruits

# 3. 건강 상태 색상
if total_score <= 3:
    color = "red"
    status = "⚠️ 건강 주의"
elif total_score <= 7:
    color = "yellow"
    status = "⚠️ 건강 보통"
else:
    color = "green"
    status = "✅ 건강 양호"

# 4. 결과 출력
st.markdown(f"### 오늘 건강 점수: {total_score}/10")
st.markdown(f"<h2 style='color:{color}'>{status}</h2>", unsafe_allow_html=True)

# 5. 시각화 - 막대 그래프
categories = ["물", "운동", "수면", "스트레스", "과일/채소"]
scores = [water, exercise, sleep, stress, fruits]

plt.bar(categories, scores, color=[color]*5)
plt.ylim(0,2)
plt.ylabel("점수 (0~2)")
plt.title("오늘 건강 체크 항목 점수")
st.pyplot(plt)

