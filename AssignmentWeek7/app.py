import streamlit as st
import numpy as np
import pandas as pd
import joblib
import matplotlib.pyplot as plt
import seaborn as sns
import os

svm_model = joblib.load(os.path.join("model", "tuned_svm_model.pkl"))
rf_model = joblib.load(os.path.join("model", "tuned_rf_model.pkl"))

st.set_page_config(page_title="📱 Mobile Price Prediction", layout="centered")

st.title("📱 Mobile Price Range Prediction")
st.markdown("Provide your mobile specifications below to predict its **price range category**.")

st.sidebar.header("Model Settings")
model_choice = st.sidebar.selectbox("Choose Prediction Model", ["SVM", "Random Forest"])

def user_input():
    st.header("📥 Enter Mobile Specifications")
    col1, col2 = st.columns(2)

    with col1:
        battery_power = st.slider('Battery Power (mAh)', 500, 2000, 1000)
        blue = st.selectbox('Bluetooth', [0, 1])
        clock_speed = st.slider('Clock Speed (GHz)', 0.5, 3.0, 1.5)
        dual_sim = st.selectbox('Dual SIM', [0, 1])
        fc = st.slider('Front Camera (MP)', 0, 20, 5)
        four_g = st.selectbox('4G', [0, 1])
        int_memory = st.slider('Internal Memory (GB)', 2, 64, 16)
        m_dep = st.slider('Mobile Depth (cm)', 0.1, 1.0, 0.5)
        mobile_wt = st.slider('Weight (g)', 80, 250, 150)

    with col2:
        n_cores = st.slider('No. of Cores', 1, 8, 4)
        pc = st.slider('Primary Camera (MP)', 0, 20, 10)
        px_height = st.slider('Pixel Height', 0, 1960, 1000)
        px_width = st.slider('Pixel Width', 0, 2000, 1000)
        ram = st.slider('RAM (MB)', 256, 4000, 2000)
        sc_h = st.slider('Screen Height (cm)', 5, 20, 10)
        sc_w = st.slider('Screen Width (cm)', 0, 18, 5)
        talk_time = st.slider('Talk Time (hrs)', 2, 20, 10)
        three_g = st.selectbox('3G', [0, 1])
        touch_screen = st.selectbox('Touch Screen', [0, 1])
        wifi = st.selectbox('WiFi', [0, 1])

    return pd.DataFrame({
        'battery_power': [battery_power],
        'blue': [blue],
        'clock_speed': [clock_speed],
        'dual_sim': [dual_sim],
        'fc': [fc],
        'four_g': [four_g],
        'int_memory': [int_memory],
        'm_dep': [m_dep],
        'mobile_wt': [mobile_wt],
        'n_cores': [n_cores],
        'pc': [pc],
        'px_height': [px_height],
        'px_width': [px_width],
        'ram': [ram],
        'sc_h': [sc_h],
        'sc_w': [sc_w],
        'talk_time': [talk_time],
        'three_g': [three_g],
        'touch_screen': [touch_screen],
        'wifi': [wifi]
    })

input_df = user_input()

st.subheader("📊 Input Summary")
st.dataframe(input_df)

if st.button("🔍 Predict Price Range"):
    model = svm_model if model_choice == "SVM" else rf_model
    prediction = model.predict(input_df)[0]

    price_map = {
        0: "💲 Low Cost",
        1: "💰 Medium Cost",
        2: "💵 High Cost",
        3: "💎 Very High Cost"
    }

    st.success(f"Predicted Price Range: **{price_map[prediction]}**")

    st.subheader("🎯 Prediction Class Overview")
    fig1, ax1 = plt.subplots()
    labels = list(price_map.values())
    sizes = [25, 25, 25, 25]  # assumed equal distribution
    ax1.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=90)
    ax1.axis('equal')
    st.pyplot(fig1)

if st.checkbox("📈 Show Model Comparison"):
    results = {
        'Tuned SVM': {
            'Accuracy': 0.89,
            'Precision': 0.90,
            'Recall': 0.89,
            'F1-score': 0.89
        },
        'Tuned RF': {
            'Accuracy': 0.92,
            'Precision': 0.93,
            'Recall': 0.92,
            'F1-score': 0.92
        }
    }

    results_df = pd.DataFrame(results).T

    st.subheader("⚖️ Model Metrics Comparison")

    model_name_map = {
        "SVM": "Tuned SVM",
        "Random Forest": "Tuned RF"
    }

    selected_model_key = model_name_map.get(model_choice)

    if selected_model_key in results_df.index:
        for metric in results_df.columns:
            st.metric(label=metric, value=f"{results_df.loc[selected_model_key, metric]:.2f}")
    else:
        st.error(f"Model '{model_choice}' not found in comparison results.")

    # Heatmap for visual comparison
    st.subheader("📊 Metric Heatmap")
    fig2, ax2 = plt.subplots()
    sns.heatmap(results_df, annot=True, cmap="YlGnBu", fmt=".2f", ax=ax2)
    st.pyplot(fig2)
