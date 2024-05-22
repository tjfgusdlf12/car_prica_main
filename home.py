import streamlit as st

def run_home():
    st.subheader('자동차 데이터를 분석하고 예측합니다!')
    st.text('데이터는 캐글에 있는 Car_Purchasing_Data.csv 파일을 사용했습니다.')
    st.text('탐색적 데이터 분석과 자동차 구매 금액을 예측하는 앱입니다.')
    
    # url로 해서 이미지를 넣어도 되고, 다운받아도됨 링크는 이미지를 내리면 에러가 뜰수도 있으니, 왠만하면 다운받아 하자.
    # url = 'https://www.motorgraph.com/news/photo/202301/31310_98337_5448.png'
    st.image('./image/car.png', use_column_width=True)