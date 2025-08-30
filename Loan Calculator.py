import numpy_financial as npf

loan_amount = float(input("Enter the loan amount: "))
pricing = float(input("Enter the pricing: "))
tenor = float(input("Enter the tenor (in months): "))

monthly_payment = -npf.pmt(pricing/12, tenor, loan_amount)
print(f"Monthly payment: {monthly_payment: .2f}")