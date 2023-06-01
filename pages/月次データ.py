import streamlit as st
import pandas as pd
import altair as alt


def monthly_drink_sales():
    '''
    drink_dataの売り上げデータと、棒グラフを表示する関数
    '''
    
    drink_data = pd.read_excel('./data/sales_data/2022sales_data.xlsx', sheet_name='drink',         engine='openpyxl', index_col=0)
    
    select_month = st.selectbox('月を選んでください', drink_data.columns.values.tolist(), key='drink')
    
    drink_data_dict = drink_data.to_dict()
    data = pd.DataFrame({
                        'メニュー': drink_data_dict[select_month].keys(),
                        '数量': drink_data_dict[select_month].values(),
    })
    
    st.subheader(f'{select_month}のドリンク販売実績')
    col_1, col_2 = st.columns(2)
    with col_1:
        st.dataframe(data)
    with col_2:
        st.altair_chart(alt.Chart(data).mark_bar().encode(
            x=alt.X('メニュー', sort=None),
            y='数量',
        ),
        use_container_width=True )
        
        
def monthly_meat_sales():
    '''
    meatの売り上げデータと、棒グラフを表示する関数
    '''
    meat_data = pd.read_excel('./data/sales_data/2022sales_data.xlsx', sheet_name='meat', engine='openpyxl', index_col=0)
    
    select_month = st.selectbox('月を選んでください',
                                meat_data.columns.values,
                                key=2)
    
    meat_data_dict = meat_data.to_dict()
    data = pd.DataFrame({
                        'メニュー': meat_data_dict[select_month].keys(),
                        '数量': meat_data_dict[select_month].values(),
    })
    
    st.subheader(f'{select_month}の肉類販売実績')
    col_1, col_2 = st.columns(2)
    with col_1:
        st.dataframe(data)
    with col_2:
        st.altair_chart(alt.Chart(data).mark_bar().encode(
            x=alt.X('メニュー', sort=None),
            y='数量',
        ),
        use_container_width=True )
        
        
def monthly_sidemenu_sales():
    '''
    sidemenuの売り上げデータと、棒グラフを表示する関数
    '''
    sidemenu_data = pd.read_excel('./data/sales_data/2022sales_data.xlsx', sheet_name='sidemenu',
                                  engine='openpyxl', index_col=0)
    
    select_month = st.selectbox('月を選んでください',
                                sidemenu_data.columns.values,
                                key=3)
    sidemenu_data_dict = sidemenu_data.to_dict()
    
    data = pd.DataFrame({
        'メニュー': sidemenu_data_dict[select_month].keys(),
        '数量': sidemenu_data_dict[select_month].values(),
    })
    st.subheader(f'{select_month}のサイドメニュー販売実績')
    col_1, col_2 = st.columns(2)
    with col_1:
        st.dataframe(data)
    with col_2:
        st.altair_chart(alt.Chart(data).mark_bar().encode(
            x=alt.X('メニュー', sort=None),
            y='数量',
        ),
        use_container_width=True )
    
st.markdown(' ### 月次データ')

if st.checkbox('ドリンク'):
    monthly_drink_sales()
    
if st.checkbox('肉類'):
    monthly_meat_sales()
    
if st.checkbox('サイドメニュー'):
    monthly_sidemenu_sales()
    
with st.form(key='monghly_sales_comment'):
    comment = st.text_input('コメントを記入してください')
    submit_btn = st.form_submit_button('登録')
    with open('./data/sales_data/monthly_sales_comment.txt', 'a') as f:
        f.write(f'{comment}')
    with open('./data/sales_data/monthly_sales_comment.txt', 'r') as f:
        sales_comment = f.read()
        sales_comment
        
st.markdown(':red[今回は練習用にデータベースの代わりにtxtファイルを使用しています。]')
st.markdown(':red[また今回はコメント登録後の取消し機能を実装していません。]')
st.markdown(':red[monthly_sales_comment.txtを直接編集することは可能です。]')
