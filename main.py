import streamlit as st
import pandas as pd
import plotly.express as px

# ---------------------------------------
# 기본 설정
# ---------------------------------------
st.set_page_config(
    page_title="영화 데이터 그래프 도감 1 - 시간",
    page_icon="🎬",
    layout="wide"
)

st.title("🎬 영화 데이터 그래프 도감 1 - 시간")
st.write("1년치 일별 박스오피스 데이터를 시간의 흐름에 따라 살펴봅니다.")

# ---------------------------------------
# 데이터 불러오기
# ---------------------------------------
DATA_URL = "https://raw.githubusercontent.com/greatsong/modudata/main/data/kobis_daily.csv"

@st.cache_data
def load_data():
    df = pd.read_csv(DATA_URL)

    # 날짜: YYYYMMDD → 실제 날짜 형식
    df["날짜"] = pd.to_datetime(
        df["날짜"].astype(str),
        format="%Y%m%d",
        errors="coerce"
    )

    # 숫자형 데이터 변환
    numeric_columns = [
        "순위",
        "영화코드",
        "일관객",
        "누적관객",
        "스크린수",
        "상영횟수"
    ]

    for col in numeric_columns:
        df[col] = pd.to_numeric(df[col], errors="coerce")

    return df


try:
    df = load_data()

except Exception as e:
    st.error("데이터를 불러오는 중 문제가 발생했습니다.")
    st.write(e)
    st.stop()


# ---------------------------------------
# 그래프 1
# ---------------------------------------
st.header("📈 그래프 1. 영화별 일관객 변화")

st.write(
    "영화를 하나 선택하면 날짜에 따른 해당 영화의 일관객 변화를 확인할 수 있습니다."
)

movie_list = sorted(df["영화명"].dropna().unique())

selected_movie = st.selectbox(
    "영화를 선택하세요.",
    movie_list
)

movie_df = df[df["영화명"] == selected_movie].copy()
movie_df = movie_df.sort_values("날짜")

fig = px.line(
    movie_df,
    x="날짜",
    y="일관객",
    markers=True,
    title=f"「{selected_movie}」의 날짜별 일관객 변화",
    labels={
        "날짜": "날짜",
        "일관객": "일관객 수"
    },
    hover_data={
        "날짜": "|%Y-%m-%d",
        "일관객": ":,",
        "순위": True,
        "스크린수": ":,",
        "상영횟수": ":,"
    }
)

fig.update_traces(
    hovertemplate=
    "날짜: %{x|%Y-%m-%d}<br>"
    "일관객: %{y:,}명"
    "<extra></extra>"
)

fig.update_layout(
    hovermode="x unified",
    xaxis_title="날짜",
    yaxis_title="일관객 수(명)",
    height=500
)

st.plotly_chart(
    fig,
    use_container_width=True
)

st.markdown("### 💡 이 그래프로 알 수 있는 것")
st.info(
    "이곳에 이 그래프를 통해 알 수 있는 내용을 한 문장으로 작성해 보세요."
)


# ---------------------------------------
# 그래프 2를 추가할 공간
# ---------------------------------------
st.divider()

st.header("📊 그래프 2")
st.write("앞으로 새로운 그래프를 추가할 공간입니다.")

st.markdown("### 💡 이 그래프로 알 수 있는 것")
st.info(
    "이곳에 두 번째 그래프를 통해 알 수 있는 내용을 한 문장으로 작성해 보세요."
)


# ---------------------------------------
# 그래프 3을 추가할 공간
# ---------------------------------------
st.divider()

st.header("📊 그래프 3")
st.write("앞으로 새로운 그래프를 추가할 공간입니다.")

st.markdown("### 💡 이 그래프로 알 수 있는 것")
st.info(
    "이곳에 세 번째 그래프를 통해 알 수 있는 내용을 한 문장으로 작성해 보세요."
)
