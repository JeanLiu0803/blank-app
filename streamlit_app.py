import streamlit as st
import pandas as pd
import numpy as np
from streamlit_option_menu import option_menu


def main():
    with st.sidebar:
        selected = option_menu(
            menu_title="Molex SI Toolbox",
            options=["Home Page", "iRL calculator", "EIPS calculator", "ccICN calculator", "Cable Loss Evaluator"],
            icons=["house", "calculator", "file-earmark-bar-graph", "graph-up", "graph-up"],
            menu_icon="cast",
            default_index=0,
        )
    
    if selected == "Home Page":
        st.title(f"{selected}")
        render_home_page()
        
    elif selected == "iRL calculator":
        st.title(f"{selected}")
        render_irl_calculator_page()

    elif selected == "EIPS calculator":
        st.title(f"{selected}")
        render_eips_calculator_page()

    elif selected == "ccICN calculator":
        st.title(f"{selected}")
        render_ccicn_calculator_page()
    
    elif selected == "Cable Loss Evaluator":
        st.title(f"{selected}")
        render_cable_loss_evaluator()

def render_home_page():
    st.header("Welcome to Molex SI Toolbox!")
    st.write("Hi there! This is a Streamlit app that showcases a few tools that you can use to calculate some parameter for your SI project.")
    st.divider()
    st.write("### Tools available:")
    st.write("- iRL calculator")
    st.write("- EIPS calculator")
    st.divider()
    st.write("### Under development:")
    st.write("- ccICN calculator")

def render_irl_calculator_page():
    # st.header("iRL calculator")
    # Add your IRL calculator functionality here
    st.write("### Step 1: Upload the s-parameter file.")
    st.file_uploader("Please upload the s-parameter file here.", type=["s4p"], accept_multiple_files=True, key="iRL_sparam_file")
    st.divider()
    
    st.write("### Step 2: Enter the parameter.")
    st.selectbox("Use Spec", ["PCIe Gen 5/6 IO spec"], key="iRL_spec")

    st.text_input("Symbol_Rate fb (GHz)", key="iRL_symbol_rate")
    st.text_input("Rise_Time Tr (ps)", key="iRL_rise_time")
    st.text_input("fr (GHz)", key="iRL_fr")

    st.divider()

    st.write("### Step 3: Click on the 'Calculate' button.")

    result_df = pd.DataFrame({"File1.s4p": "***", "File2.s4p": "***", "File3.s4p": "***"}, index=["iRL"])

    if st.button("Calculate", key="iRL_calculate"):
        st.dataframe(result_df)
        st.download_button("Download the result csv", "result.csv", "Click here to download the result")

    plot_placeholder = st.empty()

    

def render_eips_calculator_page():
    # st.header("EIPS calculator")
    # Add your EIPS calculator functionality here
    st.write("### Step 1: Upload the s-parameter file.")
    st.file_uploader("Please upload the s-parameter file here.", type=["s4p"], accept_multiple_files=True, key="eips_sparam_file")
    # st.write("### Step 2: Enter the parameter.")
    st.text_input("Symbol_Rate fb (GHz)", key="eips_symbol_rate")
    st.text_input("Max_Freq f_max (GHz)", key="eips_max_freq")
    st.text_input("Rise_Time Tr (ps)", key="eips_rise_time")
    st.text_input("fr (GHz)", key="eips_fr")

    st.write("### Step 3: Click on the 'Calculate' button.")

    result_df = pd.DataFrame({"File1.s4p": "***", "File2.s4p": "***", "File3.s4p": "***"}, index=["EIPS(ns)"])

    if st.button("Calculate", key="eips_calculate"):
        st.dataframe(result_df)
        st.download_button("Download the result csv", "result.csv", "Click here to download the result")


def render_ccicn_calculator_page():
    st.header("ccICN calculator")
    # Add your ccICN calculator functionality here

def render_cable_loss_evaluator():
    st.write('Note: I would suggest we can seperate this into another app because it may have to use a license for ANSYS designer')

    st.image("demo_plot.png")
    if st.selectbox("Select connector A", ["conn1", "conn2", "conn3", "User Defined"], key="connector_A") == "User Defined":
        st.file_uploader("Upload the s-parameter file for connector A", type=["s4p"], key="connector_A_file")

    if st.selectbox("Select raw cable", ["cable1", "cable2", "cable3", "User Defined"], key="cable") == "User Defined":
        st.file_uploader("Upload the s-parameter file for raw cable", type=["s4p"], key="cable_file")

    st.number_input("Length of the cable (mm)", key="cable_length")
    
    if st.selectbox("Select connector B", ["conn1", "conn2", "conn3", "User Defined"], key="connector_B") == "User Defined":
        st.file_uploader("Upload the s-parameter file for connector B", type=["s4p"], key="connector_B_file")

    if st.button("Calculate", key="cable_loss_calculate"):
        st.write("Cable loss = ** dB")

if __name__ == "__main__":
    main()
