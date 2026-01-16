import streamlit as st
import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv('data.csv')
klist=df.columns.tolist()
# Streamlit title
st.title("News data")

# User choice for graph type
keyword = st.selectbox("Select keyword:", (klist))
df_keyword = df[df['키워드'] == keyword]
st.dataframe(df_keyword)
# 날짜별 값만 추출
#df_plot.columns = ['Value']  # 컬럼 이름 변경
df_plot.index = pd.to_datetime(df_plot.index)  # 인덱스를 날짜로 변환
plt.figure(figsize=(10,5))
plt.plot(df_plot.index, df_plot['Value'], marker='o')
plt.title(f'{keyword} 키워드 11월 데이터')
plt.xlabel('Date')
plt.ylabel('Value')
plt.grid(True)
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
st.write("이것은 기본 텍스트 출력입니다.")

