import streamlit as st
import pandas as pd
import plotly.express as px

# Title
st.title("📊 Data Visualization & Analytics Dashboard")

# Upload CSV
uploaded_file = st.file_uploader("Upload your dataset (CSV)", type="csv")
if uploaded_file:
    df = pd.read_csv(uploaded_file)
    st.write("### Dataset Preview", df.head())

    # Select column for visualization
    numeric_cols = df.select_dtypes(include=['float64','int64']).columns
    selected_col = st.selectbox("Select a numeric column to visualize", numeric_cols)

    # Histogram
    fig = px.histogram(df, x=selected_col, nbins=20, title=f"Distribution of {selected_col}")
    st.plotly_chart(fig)

    # Scatter Plot
    if len(numeric_cols) > 1:
        x_axis = st.selectbox("X-axis", numeric_cols)
        y_axis = st.selectbox("Y-axis", numeric_cols)
        scatter_fig = px.scatter(df, x=x_axis, y=y_axis, color=df.columns[0], title="Scatter Plot")
        st.plotly_chart(scatter_fig)

    # Summary Stats
    st.write("### Summary Statistics")
    st.write(df.describe())
