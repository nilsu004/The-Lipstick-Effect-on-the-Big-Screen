import streamlit as st
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.ensemble import RandomForestRegressor

# --------------------------------------------------
# PAGE CONFIG
# --------------------------------------------------
st.set_page_config(
    page_title="Netflix Demand Predictor",
    layout="wide"
)

# --------------------------------------------------
# CINEMA / OLD FILM STYLE
# --------------------------------------------------
st.markdown(
    """
    <style>
    .stApp {
        background:
            linear-gradient(rgba(18,14,10,0.88), rgba(18,14,10,0.88)),
            url("https://images.unsplash.com/photo-1489599849927-2ee91cede3ba");
        background-size: cover;
        background-attachment: fixed;
        color: #f2e3c6;
        font-family: Georgia, serif;
    }

    section[data-testid="stSidebar"] {
        background-color: rgba(10, 8, 6, 0.95);
    }

    h1, h2, h3 {
        color: #f0d9a6;
        letter-spacing: 1px;
    }

    p, label, span {
        color: #e6d3a3;
    }

    div[data-testid="metric-container"] {
        background-color: rgba(28, 22, 16, 0.9);
        border: 1px solid rgba(240, 217, 166, 0.25);
        padding: 16px;
        border-radius: 6px;
    }

    .stApp:before {
        content: "";
        position: fixed;
        inset: 0;
        pointer-events: none;
        background-image: url("https://www.transparenttextures.com/patterns/asfalt-dark.png");
        opacity: 0.25;
        z-index: 1;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# --------------------------------------------------
# TITLE
# --------------------------------------------------
st.title("Netflix Demand Predictor")
st.markdown(
    """
    This application estimates potential audience demand for film content
    using macroeconomic indicators and cultural preferences.
    """
)

# --------------------------------------------------
# DATA (SIMULATED)
# --------------------------------------------------
@st.cache_data
def load_data():
    data_tr = {
        "Country": ["Turkey"] * 20,
        "Genre": [
            "Comedy","Drama","Crime","Fantasy","Comedy","Drama","Action","Romance",
            "Comedy","Drama","Crime","Sci-Fi","Comedy","Drama","Horror","Biography",
            "Comedy","Drama","Romance","Animation"
        ],
        "Views": [
            17400000,3300000,19300000,12400000,15000000,4000000,8000000,5000000,
            25000000,5500000,15000000,6000000,22000000,4500000,3000000,2500000,
            18000000,4200000,10300000,2000000
        ]
    }

    data_it = {
        "Country": ["Italy"] * 20,
        "Genre": [
            "Comedy","Drama","Crime","Fantasy","Comedy","Drama","Action","Romance",
            "Comedy","Drama","Crime","Sci-Fi","Comedy","Drama","Horror","Biography",
            "Comedy","Drama","Romance","Animation"
        ],
        "Views": [
            16900000,17600000,4800000,4900000,12000000,14000000,3000000,2000000,
            8000000,11000000,2000000,1500000,6000000,9000000,1000000,800000,
            17000000,14500000,3000000,5500000
        ]
    }

    df = pd.concat([pd.DataFrame(data_tr), pd.DataFrame(data_it)])
    np.random.seed(42)
    df["Tot_mean_infrate"] = np.random.uniform(2, 70, len(df))
    df["Tot_mean_unemprate"] = np.random.uniform(5, 12, len(df))
    return df

df = load_data()

# --------------------------------------------------
# MODEL
# --------------------------------------------------
X = df[["Country", "Genre", "Tot_mean_infrate", "Tot_mean_unemprate"]]
y = df["Views"]

X_encoded = pd.get_dummies(X, drop_first=False)

model = RandomForestRegressor(
    n_estimators=100,
    random_state=42
)
model.fit(X_encoded, y)

# --------------------------------------------------
# SIDEBAR
# --------------------------------------------------
st.sidebar.header("Scenario Settings")

selected_country = st.sidebar.selectbox(
    "Country", ["Turkey", "Italy"]
)

selected_genre = st.sidebar.selectbox(
    "Genre",
    ["Comedy", "Drama", "Crime", "Fantasy", "Sci-Fi", "Romance", "Action"]
)

inflation = st.sidebar.slider(
    "Inflation Rate (%)", 0, 100, 50
)

unemployment = st.sidebar.slider(
    "Unemployment Rate (%)", 0, 20, 10
)

# --------------------------------------------------
# PREDICTION
# --------------------------------------------------
input_data = pd.DataFrame(0, index=[0], columns=X_encoded.columns)
input_data["Tot_mean_infrate"] = inflation
input_data["Tot_mean_unemprate"] = unemployment

if f"Country_{selected_country}" in input_data.columns:
    input_data[f"Country_{selected_country}"] = 1

if f"Genre_{selected_genre}" in input_data.columns:
    input_data[f"Genre_{selected_genre}"] = 1

prediction = model.predict(input_data)[0]

# --------------------------------------------------
# OUTPUT
# --------------------------------------------------
col1, col2 = st.columns(2)

with col1:
    st.subheader("Prediction Result")
    st.metric(
        label="Estimated View Count",
        value=f"{prediction:,.0f}"
    )

    if prediction > 10_000_000:
        st.success("High demand expected")
    elif prediction > 5_000_000:
        st.warning("Moderate demand expected")
    else:
        st.error("Low demand expected")

with col2:
    st.subheader("Contextual Analysis")
    st.write(
        f"Country: {selected_country} | "
        f"Genre: {selected_genre} | "
        f"Inflation: {inflation}% | "
        f"Unemployment: {unemployment}%"
    )

    avg_views = (
        df[df["Country"] == selected_country]
        .groupby("Genre")["Views"]
        .mean()
        .sort_values(ascending=False)
        .head(5)
    )

    fig, ax = plt.subplots(figsize=(5, 3))
    sns.barplot(
        x=avg_views.values,
        y=avg_views.index,
        ax=ax
    )
    ax.set_title(f"Average Views by Genre in {selected_country}")
    st.pyplot(fig)

# --------------------------------------------------
# FOOTER
# --------------------------------------------------
st.markdown("---")
st.caption("Netflix Demand Predictor")
