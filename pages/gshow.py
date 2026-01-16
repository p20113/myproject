import matplotlib.pyplot as plt
import pandas as pd
import streamlit as st
df = pd.read_csv('olddata.csv')
klist=df['키워드'].tolist()
# Streamlit title
st.title("News data")

# User choice for graph type
keyword = st.selectbox("Select keyword:", (klist))
st.write(df)
# 날짜별 값만 추출
ylist=list()
keyl=list(df['키워드'])
# User choice for graph type
# 날짜별 값만 추출
targetind=keyl.index(keyword)
ylist=list(df.iloc[targetind,1:])
plt.figure(figsize=(10,5))
plt.plot(list(df.columns[1:]),ylist, marker='o')
plt.title(f'{keyword} 키워드 11월 데이터')
plt.xlabel('Date')
plt.ylabel('Value')
plt.grid(True)
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
st.pyplot(fig)
st.write("이것은 기본 텍스트 출력입니다.")
