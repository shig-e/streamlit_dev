import streamlit as st
import pandas as pd
import altair as alt


'''
#### 品別売上
'''

def drink_kind():
    '''
    ラジオボタンでドリンク品名売上の棒グラフを表示する関数 
    '''
    st.markdown('#### ドリンクメニュー売上比較')
    drink_data = drink_data = pd.read_excel('./data/sales_data/2022sales_data.xlsx', sheet_name='drink', engine='openpyxl', index_col=0)
    
    transposed_drink_data = drink_data.transpose()
    col_1, col_2 = st.columns(2)
    with col_1:
        selected_drink = st.radio('メニューを選んでください',
            transposed_drink_data.columns.unique(),
            key='drink_1')
    with col_2:
        data = pd.DataFrame({
            '営業月': transposed_drink_data.index.unique(),
            '売上数': transposed_drink_data[selected_drink]
        })
        st.altair_chart(alt.Chart(data).mark_bar().encode(
            x=alt.X('営業月', sort=None),
            y='売上数',
        ),
        use_container_width=True)
        
def drink_multiselect():
    '''
    マルチセレクトでドリンク売上数を折れ線グラフで表示
    '''
    drink_data = drink_data = pd.read_excel('./data/sales_data/2022sales_data.xlsx', sheet_name='drink', engine='openpyxl', index_col=0)
    transposed_drink_data = drink_data.transpose()
    
    multiselected_drink_list = st.multiselect(
        '確認したいドリンクのメニューを選んでください(複数選択可)',
        transposed_drink_data.columns.unique(),
        '生大',
        key='drink_2'
    )
    st.write(transposed_drink_data[multiselected_drink_list])
    if not multiselected_drink_list:
        st.error('表示するメニューが選択されていません。')
    else:
        st.line_chart(transposed_drink_data[multiselected_drink_list])
        
def meat_sales():
    st.markdown('#### 肉類メニュー売上比較')
    meat_data = pd.read_excel('./data/sales_data/2022sales_data.xlsx', sheet_name='meat', engine='openpyxl', index_col=0)
    
    transposed_meat_data = meat_data.transpose()
    
    col_1, col_2 = st.columns(2)
    with col_1:
        selected_meat = st.radio('メニューを選んでください',
            transposed_meat_data.columns.unique(),
            key='meat_1')
    with col_2:
        data = pd.DataFrame({
            '営業月': transposed_meat_data.index.unique(),
            '売上数': transposed_meat_data[selected_meat]
        })
        st.subheader(selected_meat)
        st.altair_chart(alt.Chart(data).mark_bar().encode(
                    x=alt.X('営業月', sort=None),
                    y='売上数',
                    ),
                    use_container_width=True)

def meat_kind():
    '''
    ラジオボタンで品別にお肉売上の棒グラフを表示する関数 
    '''
    meat_data = drink_data = pd.read_excel('./data/sales_data/2022sales_data.xlsx', sheet_name='meat', engine='openpyxl', index_col=0)
    
    transposed_meat_data = meat_data.transpose()
    multiselected_meat = st.multiselect(
        '確認したい肉類のメニューを選んでください(複数選択可)',
        transposed_meat_data.columns.unique(),
        'トモサンカク',
        key='meat_2'
        )
    st.write(transposed_meat_data[multiselected_meat])
    if not multiselected_meat:
        st.error('表示するメニューが選択されていません。')
    else:
        st.line_chart(transposed_meat_data[multiselected_meat])
        
def side_sales():
    '''
    ラジオボタンサイドメニュー売上の棒グラフを表示する関数 
    '''
    
    saide_data = drink_data = pd.read_excel('./data/sales_data/2022sales_data.xlsx', sheet_name='sidemenu', engine='openpyxl', index_col=0)
    
    transposed_saide_data = saide_data.transpose()
    col_1, col_2 = st.columns(2)
    with col_1:
        selected_saide = st.radio('メニューを選んでください',
            transposed_saide_data.columns.unique(),
            key='saide_1')
    with col_2:
        data = pd.DataFrame({
            '営業月': transposed_saide_data.index.unique(),
            '売上数': transposed_saide_data[selected_saide]
        })
        st.subheader(selected_saide)
        st.altair_chart(alt.Chart(data).mark_bar().encode(
            x=alt.X('営業月', sort=None),
            y='売上数',
        ),
        use_container_width=True)
        
def saide_kind():
    '''
    ラジオボタンで品別にサイドメニュー売上の棒グラフを表示する関数 
    '''
    saide_data = saide_data = pd.read_excel('./data/sales_data/2022sales_data.xlsx', sheet_name='sidemenu', engine='openpyxl', index_col=0)
    
    transposed_saide_data = saide_data.transpose()
    multiselected_saide = st.multiselect(
        '確認したいサイドメニューを選んでください(複数選択可)',
        transposed_saide_data.columns.unique(),
        'クッパ',
        key='saide_2'
        )
    st.write(transposed_saide_data[multiselected_saide])
    if not multiselected_saide:
        st.error('表示するメニューが選択されていません。')
    else:
        st.line_chart(transposed_saide_data[multiselected_saide])
        

if st.checkbox('ドリンクの品別売上'):
    drink_kind()
if st.checkbox('ドリンクの品別売上(マルチセレクト)'):
    drink_multiselect()
if st.checkbox('肉類の品別売上'):
    meat_sales()
if st.checkbox('肉類の品別売上(マルチセレクト)'):
    meat_kind()
if st.checkbox('サイドメニューの品別売上'):
    side_sales()
if st.checkbox('サイドメニューの品別売上(マルチセレクト)'):
    saide_kind()
    
with st.form(key='sales_kind_comment'):
    comment = st.text_input('コメントを記入してください(今回は登録の取り消しはできません。)')
    submit_btn = st.form_submit_button('登録')
    with open('./data/sales_data/sales_kind_comment.txt', 'a') as f:
        f.write(f'{comment}')
    with open('./data/sales_data/sales_kind_comment.txt', 'r') as f:
        sales_comment = f.read()
        sales_comment
st.markdown(':red[今回は練習用にデータベースの代わりにtxtファイルを使用しています。]')
st.markdown(':red[また今回はコメント登録後の取消し機能を実装していません。]')
st.markdown(':red[monthly_sales_comment.txtを直接編集することは可能です。]')