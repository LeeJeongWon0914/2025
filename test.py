import streamlit as st
import pandas as pd

st.title("🌱 나만의 건강 체크리스트")

# 세션 상태로 단계 관리
if "step" not in st.session_state:
    st.session_state.step = 0
if "answers" not in st.session_state:
    st.session_state.answers = {}

def next_step():
    st.session_state.step += 1

# 단계별 화면
if st.session_state.step == 0:
    st.markdown("👋 오늘의 건강 체크를 시작해볼까요?")
    if st.button("시작하기 ▶️"):
        next_step()

elif st.session_state.step == 1:
    st.session_state.answers["water"] = st.slider("💧 물 섭취 (ml, 목표 2000ml)", 0, 2000, 1000, step=100)
    if st.button("다음 ➡️"):
        next_step()

elif st.session_state.step == 2:
    st.session_state.answers["exercise"] = st.slider("🏃 운동 (분, 목표 120분)", 0, 120, 30, step=5)
    if st.button("다음 ➡️"):
        next_step()

elif st.session_state.step == 3:
    st.session_state.answers["sleep"] = st.slider("🛌 수면 시간 (시간, 목표 8시간)", 0.0, 12.0, 7.0, step=0.5)
    if st.button("다음 ➡️"):
        next_step()

elif st.session_state.step == 4:
    st.session_state.answers["stress"] = st.slider("😰 스트레스 (0=낮음, 10=높음)", 0, 10, 5)
    if st.button("다음 ➡️"):
        next_step()

elif st.session_state.step == 5:
    st.session_state.answers["fruits"] = st.slider("🍎 과일/채소 섭취 (횟수, 목표 5회)", 0, 5, 2)
    if st.button("결과 보기 🏁"):
        next_step()

# 최종 결과
elif st.session_state.step == 6:
    water = st.session_state.answers["water"]
    exercise = st.session_state.answers["exercise"]
    sleep = st.session_state.answers["sleep"]
    stress = st.session_state.answers["stress"]
    fruits = st.session_state.answers["fruits"]

    # 점수 계산
    scores = {
        "물": (water / 2000) * 100,
        "운동": (exercise / 120) * 100,
        "수면": (sleep / 8) * 100,
        "스트레스": ((10 - stress) / 10) * 100,
        "과일/채소": (fruits / 5) * 100,
    }
    total_score = sum(scores.values()) / len(scores)

    # 이모지 피드백
    if total_score <= 40:
        status = "🔴 주의! 생활습관을 개선해보세요."
        bg_color = "#ffcccc"
    elif total_score <= 70:
        status = "🟡 보통! 조금만 더 노력해봐요."
        bg_color = "#fff3cd"
    else:
        status = "🟢 좋음! 건강한 생활을 유지하세요."
        bg_color = "#d4edda"

    # 결과 출력
    st.markdown(
        f"""
        <div style="padding:20px; border-radius:10px; background-color:{bg_color}">
        <h3>오늘의 건강 점수: {total_score:.1f}/100</h3>
        <p>{status}</p>
        </div>
        """, unsafe_allow_html=True
    )

    df = pd.DataFrame(list(scores.items()), columns=["항목", "점수"]).set_index("항목")
    st.bar_chart(df)

    # 추가 팁 제공
    if water < 1500:
        st.info("💧 물을 더 마셔보세요! 하루 2L가 이상적입니다.")
    if exercise < 30:
        st.info("🏃 운동량이 부족해요! 가벼운 산책이라도 해볼까요?")
    if sleep < 6:
        st.info("🛌 수면 시간이 짧습니다. 수면 루틴을 지켜보세요.")
