import streamlit as st
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, MinMaxScaler, OneHotEncoder
from sklearn.impute import SimpleImputer
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.linear_model import LogisticRegression, LinearRegression
from sklearn.ensemble import RandomForestClassifier, RandomForestRegressor
from sklearn.metrics import accuracy_score, classification_report, r2_score

st.title("Model of ML")
st.write("Upload a dataset, preprocess, and train models with ease.")

# --- Upload CSV ---
uploaded_file = st.file_uploader("Upload CSV", type=["csv"])
if uploaded_file:
    df = pd.read_csv(uploaded_file)
    st.subheader("Dataset Preview")
    st.write(df.head())

    # Select target column
    target = st.selectbox("Select Target Column", df.columns)

    # Preprocessing options
    st.sidebar.header("Preprocessing Options")

    impute_method = st.sidebar.selectbox("Missing Value Imputation", ["None", "Mean", "Median", "Most Frequent"])
    scale_method = st.sidebar.selectbox("Scaling Method", ["None", "StandardScaler", "MinMaxScaler"])
    encode_method = st.sidebar.selectbox("Categorical Encoding", ["None", "OneHotEncoder"])

    # Algorithm Selection
    st.sidebar.header("Model Options")
    task_type = st.sidebar.radio("Task Type", ["Classification", "Regression"])
    model_choice = st.sidebar.selectbox("Select Algorithm", ["Logistic Regression", "Linear Regression", "Random Forest"])

    if st.button("Train Model"):
        X = df.drop(columns=[target])
        y = df[target]

        # Identify column types
        numeric_cols = X.select_dtypes(include=['float64', 'int64']).columns
        categorical_cols = X.select_dtypes(include=['object', 'category']).columns

        # Preprocessing steps
        transformers = []

        if impute_method != "None":
            strategy = impute_method.lower().replace("most frequent", "most_frequent")
            transformers.append(('imputer', SimpleImputer(strategy=strategy), numeric_cols))

        if scale_method != "None":
            scaler = StandardScaler() if scale_method == "StandardScaler" else MinMaxScaler()
            transformers.append(('scaler', scaler, numeric_cols))

        if encode_method == "OneHotEncoder" and len(categorical_cols) > 0:
            transformers.append(('encoder', OneHotEncoder(handle_unknown='ignore'), categorical_cols))

        preprocessor = ColumnTransformer(transformers, remainder='passthrough')

        # Choose model
        if task_type == "Classification":
            if model_choice == "Logistic Regression":
                model = LogisticRegression()
            else:
                model = RandomForestClassifier()
        else:
            if model_choice == "Linear Regression":
                model = LinearRegression()
            else:
                model = RandomForestRegressor()

        # Create Pipeline
        pipeline = Pipeline(steps=[
            ('preprocessor', preprocessor),
            ('model', model)
        ])

        # Train/Test split
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

        # Fit model
        pipeline.fit(X_train, y_train)

        # Predictions
        y_pred = pipeline.predict(X_test)

        # Evaluation
        st.subheader("Model Evaluation")
        if task_type == "Classification":
            st.write(f"Accuracy: {accuracy_score(y_test, y_pred):.4f}")
            st.text("Classification Report:")
            st.text(classification_report(y_test, y_pred))
        else:
            st.write(f"R² Score: {r2_score(y_test, y_pred):.4f}")
