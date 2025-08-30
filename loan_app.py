import streamlit as st
import numpy_financial as npf

st.title("Loan Calculator")

loan_amount = st.number_input("Loan Amount", min_value=0.0)
pricing = st.number_input("Annual Interest Rate (e.g., 0.05)", min_value=0.0, step=0.01)
tenor = st.number_input("Tenor (Months)", min_value=1, step=1)

if st.button("Calculate"):
    monthly_payment = -npf.pmt(pricing / 12, tenor, loan_amount)
    st.success(f"Monthly Payment: {monthly_payment:.2f}")