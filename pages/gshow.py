import streamlit as st
import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv('data.csv')
klist=df.columns.tolist()
# Streamlit title
st.title("News data")

# User choice for graph type
keyword = st.selectbox("Select keyword:", (klist))
df = pd.DataFrame(data)
df["날짜"] = pd.to_datetime(df["날짜"])

# Streamlit에서 선택한 키워드라고 가정
# 실제 사용 시 st.multiselect에서 가져오

# 그래프 초기화
plt.figure(figsize=(8, 4))

# 선택한 키워드만 그리기
plt.plot(df["날짜"], df[keyword], marker='o', label=keyword)

# 그래프 꾸미기
plt.xlabel("날짜")
plt.ylabel("값")
plt.title("선택한 키워드별 날짜 그래프")
plt.legend()
plt.grid(True)
plt.xticks(rotation=45)
plt.tight_layout()  # 레이블 겹침 방지

# Streamlit에 표시
st.pyplot(plt)
