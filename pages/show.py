import streamlit as st
import matplotlib.pyplot as plt
import pandas as pd

# 데이터 불러오기
df = pd.read_csv('data.csv')

# 키워드 목록 (첫 번째 컬럼은 날짜라고 가정)
klist = df.columns.tolist()[1:]  # 날짜 제외

st.title("News data")

# 키워드 선택
keyword = st.selectbox("Select keyword:", klist)
'''
df_keyword = df['날짜',keyward] 
#df_keyword = df[df['날짜'] == keyword]
st.dataframe(df_keyword)
# 선택한 키워드 데이터 추출
df_plot = df[['날짜', keyword]].copy()
df_plot.set_index('날짜', inplace=True)
df_plot.index = pd.to_datetime(df_plot.index)
df_plot.columns = ['Value']
'''
# 그래프 그리기
plt.figure(figsize=(10,5))
#plt.plot(df_plot.index, df_plot['Value'], marker='o')
fig, ax = plt.subplots()
ax.plot(df['날짜'], df[keyword], marker='o')
st.pyplot(fig)

plt.title(f'{keyword} 키워드 11월 데이터')
plt.xlabel('Date')
plt.ylabel('Value')
plt.grid(True)
plt.xticks(rotation=45)
plt.tight_layout()

# Streamlit에 출력
st.pyplot(plt)

st.write("이것은 기본 텍스트 출력입니다.")
