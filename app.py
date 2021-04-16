import streamlit as st
import pandas as pd
import plotly.express as px
from sklearn.decomposition import PCA
from sklearn import preprocessing

st.set_page_config(layout='wide')
scatter_column, settings_column = st.beta_columns((4,1))

scatter_column.title("Multi-Dimensional Analysis")
settings_column.title("Settings")

uploaded_file = settings_column.file_uploader("Choose File")

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    pca_data, cat_cols, pca_cols = pca_maker(df)

    categorical_variable = settings_column.selectbox("Variable Select", options = cat_cols)
    cateorical_variable_2 = settings_column.selectbox("Second Variable Select", options = cat_cols)

    pca_1 = settings_column.selectbox("First Principle Component", options=pca_cols, index=0)
    pca_2 = settings_column.selectbox("Second Principle Component", options=pca_cols)

    scatter_column.plotly_chart(px.scatter(data_frame=pca_data, x = pca_1, y = pca_2, color=categorical_variable, template="plotly_dark", height=000, hver_data=[categorical_variable_2] ), use_container_width=True)

else:
    scatter_column.header("Please choose a file")
