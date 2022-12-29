import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import plotly_express as px

def stats(dataframe):
    st.header('Data stats')
    st.writer(dataframe.describe())

def data_header(dataframe):
    st.header('Data Header')
    st.write(df.head())

def plot(dataframe):
    fig,ax=plt.subplot(1,1)
    ax.scatter(x=df['Depth'],y=df['Magnitude'])
    ax.set_xlabel('new')
    st.pyplot(fig)
def interactive_plot(dataframe):
    x_axis_val=st.selectbox()
    y_axis_val=st.selectbox()
    plot=px.scatter(dataframe,x=x_axis_val,y=y_axis_val)
    col=st.color_picker('select a color')
    plt=px.scatter(dataframe,x=x_axis_val,y=y_axis_val)
    plt.update_traces(marker=dict(color=col))
    st.plotly_chart(plot)

st.title('New Plot Graph')
st.text('new values')
st.sidebar.title('Navigation')
uploaded_file=st.sidebar.radio('Pages', options=[
    'Home','Data Header','Data Stats','Plot'])
## uploaded_files=pd.read_csv(r"C:/Users/00824732/Desktop/Business-employment-data-september-2022-quarter-csv.csv")
if uploaded_file:
    df=pd.read_csv(uploaded_file)

if options=='Data Science':
    stats(df)
elif options=='Data Header':
    data_header(df)
elif options=='Plot':
    plot(df)

