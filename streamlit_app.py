import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

st.title("🎈 Streamlit Elements Showcase")
st.write("이 페이지는 Streamlit의 다양한 요소들을 보여줍니다. 각 요소의 예시를 확인하세요!")

# Text Elements
st.header("📝 텍스트 요소들")
st.subheader("제목과 텍스트")
st.title("이건 제목이에요")
st.header("헤더")
st.subheader("서브헤더")
st.text("일반 텍스트")
st.markdown("**마크다운** 텍스트: *이탤릭*, `코드`")
st.latex(r"E = mc^2")

# Input Widgets
st.header("🔧 입력 위젯들")
st.subheader("버튼과 체크박스")
if st.button("클릭하세요!"):
    st.write("버튼이 클릭되었습니다!")

agree = st.checkbox("동의합니다")
if agree:
    st.write("동의하셨습니다!")

st.subheader("선택 위젯들")
genre = st.radio("좋아하는 장르를 선택하세요", ("코미디", "드라마", "액션"))
st.write(f"선택한 장르: {genre}")

option = st.selectbox("옵션을 선택하세요", ("옵션 1", "옵션 2", "옵션 3"))
st.write(f"선택한 옵션: {option}")

multi_options = st.multiselect("여러 개 선택하세요", ["A", "B", "C", "D"])
st.write(f"선택한 옵션들: {multi_options}")

st.subheader("슬라이더와 입력")
age = st.slider("나이를 선택하세요", 0, 100, 25)
st.write(f"나이: {age}")

name = st.text_input("이름을 입력하세요")
st.write(f"이름: {name}")

number = st.number_input("숫자를 입력하세요", min_value=0.0, max_value=100.0, value=50.0)
st.write(f"숫자: {number}")

text_area = st.text_area("긴 텍스트를 입력하세요")
st.write(f"입력된 텍스트: {text_area}")

date = st.date_input("날짜를 선택하세요")
st.write(f"선택한 날짜: {date}")

time = st.time_input("시간을 선택하세요")
st.write(f"선택한 시간: {time}")

uploaded_file = st.file_uploader("파일을 업로드하세요")
if uploaded_file is not None:
    st.write("파일이 업로드되었습니다:", uploaded_file.name)

# Output Elements
st.header("📊 출력 요소들")
st.subheader("데이터프레임과 테이블")
df = pd.DataFrame({
    '이름': ['Alice', 'Bob', 'Charlie'],
    '나이': [25, 30, 35],
    '점수': [85, 90, 95]
})
st.dataframe(df)
st.table(df)

st.subheader("JSON과 메트릭")
data = {"이름": "Alice", "나이": 25, "점수": 85}
st.json(data)

col1, col2, col3 = st.columns(3)
with col1:
    st.metric("온도", "70 °F", "1.2 °F")
with col2:
    st.metric("습도", "86%", "-8%")
with col3:
    st.metric("압력", "30.4 inHg", "0.5 inHg")

# Media Elements
st.header("🎥 미디어 요소들")
st.subheader("이미지, 오디오, 비디오")
st.image("https://www.streamlit.io/images/brand/streamlit-logo-secondary-colormark-darktext.png", caption="Streamlit 로고")
# 오디오와 비디오 예시는 실제 파일이 필요하지만, 여기서는 생략

# Charts
st.header("📈 차트 요소들")
st.subheader("라인 차트, 바 차트, 에어리어 차트")
chart_data = pd.DataFrame(np.random.randn(20, 3), columns=['A', 'B', 'C'])
st.line_chart(chart_data)
st.bar_chart(chart_data)
st.area_chart(chart_data)

st.subheader("Matplotlib 차트")
fig, ax = plt.subplots()
ax.plot([1, 2, 3, 4], [1, 4, 2, 3])
st.pyplot(fig)

# Layout Elements
st.header("🏗️ 레이아웃 요소들")
st.subheader("사이드바, 컬럼, 익스팬더")
with st.sidebar:
    st.write("이건 사이드바입니다!")
    sidebar_option = st.selectbox("사이드바 옵션", ["옵션 A", "옵션 B"])

col1, col2 = st.columns(2)
with col1:
    st.write("왼쪽 컬럼")
with col2:
    st.write("오른쪽 컬럼")

with st.expander("더 보기"):
    st.write("익스팬더 내부 내용")

# Other Fun Elements
st.header("🎉 기타 재미있는 요소들")
st.subheader("프로그레스 바, 스피너, 풍선")
progress_bar = st.progress(0)
for i in range(100):
    progress_bar.progress(i + 1)

with st.spinner("로딩 중..."):
    import time
    time.sleep(1)
st.success("완료되었습니다!")

if st.button("풍선 터뜨리기"):
    st.balloons()

if st.button("눈 내리기"):
    st.snow()

st.write("Streamlit의 다양한 요소들을 확인해보세요! 더 많은 정보는 [docs.streamlit.io](https://docs.streamlit.io/)에서 확인할 수 있습니다.")
