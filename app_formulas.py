import streamlit as st
import pandas as pd
import plotly.express as px
from sklearn.decomposition import PCA
from sklearn import preprocessing
import numpy as npimport streamlit as st
import pandas as pd
import plotly.express as px
from sklearn.decomposition import PCA
from sklearn import preprocessing
import numpy as np
from app_formulas import pca_maker

def pca_maker(df):
    #df = pd.read_csv("data/2021_MPG_data.csv")
    #df2 = df.copy()

    numerical_columns_list = []
    categorical_columns_list = []

    for i in df.columns:
        if df[i].dtype == np.dtype("float64") or df[i].dtype == np.dtype("int64"):
            numerical_columns_list.append(df[i])
        else:
            categorical_columns_list.append(df[i])

    numerical_data = pd.concat(numerical_columns_list, axis=1)
    categorical_data = pd.concat(categorical_columns_list, axis=1)

    numerical_data = numerical_data.apply(lambda x: x.fillna(np.mean(x)))
    scaler = StandardScaler()

    scaled_values = scaler.fit_transform(numerical_data)
    pca_data = pca.fit_transform(scaled_values)

    pca_data = pd.DataFrame(pca_data)

    new_column_names = ["PCA_" + str(i) for i in range(1, len(pca_data.columns) + 1)]

    column_mapper = dict(zip(list(pca_data.columns), new_column_names))

    pca_data = pca_data.rename(columns=column_mapper)

    output = pd.concat([df, pca_data], axis=1)

    return output, list(categorical_data.columns), new_column_names