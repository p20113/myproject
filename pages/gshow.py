import matplotlib.pyplot as plt
import pandas as pd
import streamlit as st
df = pd.read_csv('olddata.csv')
klist=df['키워드'].tolist()
# Streamlit title
st.title("News data")

# User choice for graph type
keyword = st.selectbox("Select keyword:", (klist))
df_keyword = df[df['키워드'] == keyword]
st.dataframe(df_keyword)
st.write(df)
# 날짜별 값만 추출
ylist=list()
keyl=list(df['키워드'])
targetind=keyl.index(keyword)
for dictkey in df[1:]:
  ylist.append(df[dictkey][targetind])
#df_plot = df_keyword.drop(columns=['키워드']).T  # 전치
#df_plot.columns = ['Value']  # 컬럼 이름 변경
#df_plot.index = pd.to_datetime(df_plot.index)  # 인덱스를 날짜로 변환
plt.figure(figsize=(10,5))
plt.plot(list(df.columns[1:]),ylist, marker='o')
plt.title(f'{keyword} 키워드 11월 데이터')
plt.xlabel('Date')
plt.ylabel('Value')
plt.grid(True)
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
st.write("이것은 기본 텍스트 출력입니다.")
