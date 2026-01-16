import streamlit as st
import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv('data.csv')
klist=df['키워드'].tolist()
# Streamlit title
st.title("News data")

# User choice for graph type
chart_type = st.selectbox("Select chart type:", (klist))


keyword = chart_type
df_keyword = df[df['키워드'] == keyword]

# 날짜별 값만 추출
df_plot = df_keyword.drop(columns=['키워드']).T  # 전치
df_plot.columns = ['Value']  # 컬럼 이름 변경
df_plot.index = pd.to_datetime(df_plot.index)  # 인덱스를 날짜로 변환

print(df_plot)
plt.figure(figsize=(10,5))
plt.plot(df_plot.index, df_plot['Value'], marker='o')
plt.title(f'{keyword} 키워드 11월 데이터')
plt.xlabel('Date')
plt.ylabel('Value')
plt.grid(True)
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

"""
if chart_type == "Line Chart":
    # Plot line chart
    plt.figure(figsize=(12, 6))
    plt.plot(yearly_stats['연도'], yearly_stats['평균기온(℃)'], label='Average Temperature (℃)', marker='o')
    plt.plot(yearly_stats['연도'], yearly_stats['최저기온(℃)'], label='Minimum Temperature (℃)', marker='o')
    plt.plot(yearly_stats['연도'], yearly_stats['최고기온(℃)'], label='Maximum Temperature (℃)', marker='o')
    plt.xlabel('Year')
    plt.ylabel('Temperature (℃)')
    plt.title('Yearly Temperature Trends')
    plt.legend()
    plt.grid(True)
    st.pyplot(plt)

elif chart_type == "Bar Chart":
    # Plot bar chart
    plt.figure(figsize=(12, 6))
    plt.bar(yearly_stats['연도'] - 0.2, yearly_stats['평균기온(℃)'], width=0.2, label='Average Temperature (℃)')
    plt.bar(yearly_stats['연도'], yearly_stats['최저기온(℃)'], width=0.2, label='Minimum Temperature (℃)')
    plt.bar(yearly_stats['연도'] + 0.2, yearly_stats['최고기온(℃)'], width=0.2, label='Maximum Temperature (℃)')
    plt.xlabel('Year')
    plt.ylabel('Temperature (℃)')
    plt.title('Yearly Temperature Trends')
    plt.legend()
    st.pyplot(plt)"""
