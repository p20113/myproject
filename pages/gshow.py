import matplotlib.pyplot as plt
import pandas as pd
import streamlit as st
df = pd.read_csv('olddata.csv')
klist=df['키워드'].tolist()
# Streamlit title
st.title("News data")

# User choice for graph type
selected_options = st.multiselect(
    "Select keyword:",          # 사용자에게 보여질 레이블 (문자열)
    klist,        # 선택 가능한 전체 항목 리스트 (리스트, 튜플, pandas Series, numpy array)
)
#keyword = st.selectbox("Select keyword:", (klist))
keywordlist=selected_options
st.write(df)
ylist=list()
keyl=list(df['키워드'])
# User choice for graph type
# 날짜별 값만 추출
targetind=0
for tarkey in keywordlist:
    targetind=keyl.index(tarkey)
    ylist.append(list(df.iloc[targetind,1:]))
plt.figure(figsize=(10,5))
for ind in range(len(keywordlist)):
    plt.plot(list(df.columns[1:]),ylist[ind], marker='o')
# 날짜별 값만 추출
plt.title(f'{keywordlist} 키워드 11월 데이터')
plt.xlabel('Date')
plt.ylabel('Value')
plt.grid(True)
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
st.pyplot(plt)
st.write("이것은 기본 텍스트 출력입니다.")
