import streamlit as st
from PIL import Image
import pandas as pd

st.subheader('当社の財務分析方針')

st.write('主に分析に使う財務諸表は以下の3つとします。')

expander1 = st.expander('・損益計算書')
expander1.write('損益計算書は、収益から費用を差し引いた「利益」を計算します。')
expander1.write('このダッシュボードで、次月の損益計算表を確認することができます。')
expander2 = st.expander('・貸借対照表')
expander2.write('貸借対照表は、「決算日時点の企業の財務状態」を表します。')
expander2.write('前年度のものは、別途、経理部にご確認ください。')
expander3 = st.expander('・キャッシュフロー計算書')
expander3.write('キャッシュフロー計算書は、「資金(お金)の流れ」を把握するための計算書です。')
expander3.write('前年度のものは、別途、経理部にご確認ください。')

st.write('「利益金処分計算書」「附属明細表」は必要に応じて経理部にご確認ください。')

image = Image.open('./data/img/financial_statements.png')
st.image(image)

st.markdown(' #### 前年度の損益計算表')
pl_data = pd.read_excel('./data/financial_data/2022financial_data.xlsx', engine='openpyxl', index_col=0)

st.dataframe(pl_data)

transposed_pl_data = pl_data.transpose()
transposed_pl_data = transposed_pl_data.drop(index=['合計'])

multidelectd_account = st.multiselect('項目を選んでください',
                                      ['売上高', '売上原価', '売上総利益', '販売費・一般管理費計', '営業利益'],
                                      ['売上高'])
st.line_chart(transposed_pl_data[multidelectd_account])