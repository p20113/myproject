import streamlit as st
import matplotlib.pyplot as plt
import pandas as pd

# 데이터 불러오기
df = pd.read_csv('data.csv')
df['날짜'] = pd.to_datetime(df['날짜'], format="%Y-%m-%d", errors='coerce')


# 키워드 목록 (첫 번째 컬럼은 날짜라고 가정)
klist = df.columns.tolist()[1:]  # 날짜 제외

st.title("News data")

# 키워드 선택
keyword = st.selectbox("Select keyword:", klist)

st.write(df['날짜'].dtype)
st.write(df['날짜'].head(10))
st.write(df['날짜'].map(type).value_counts())
st.write(df[df['날짜'].isna()].head())



fig, ax = plt.subplots(figsize=(10,5))
ax.plot(df['날짜'], df[keyword])
ax.set_xlabel('Year')
ax.set_ylabel('cnt')
ax.set_title('Trends')
st.pyplot(fig)
