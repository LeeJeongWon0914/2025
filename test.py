import streamlit as st
import pandas as pd

st.title("✅ 간단 건강 체크")

water = st.slider("💧 물 (ml)", 0, 2000, 100, step=100)
exercise = st.slider("🏃‍♂️ 운동 (분)", 0, 120, 30, step=5)
sleep = st.slider("🛌 수면 (시간)", 0.0, 10.0, 7.0, step=0.5)
stress = st.slider("😰 스트레스 (0=낮음, 10=높음)", 0, 10, 5)
fruits = st.slider("🍎 과일/채소 (회)", 0, 5, 2)

score = (water/2000 + exercise/120 + sleep/10 + (10-stress)/10 + fruits/5) * 20
st.write(f"오늘 점수: {score:.1f}/100")

