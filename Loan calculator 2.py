import tkinter as tk
import numpy_financial as npf

def calculate_payment():
    try:
        loan_amount = float(entry_loan.get())
        pricing = float(entry_rate.get())
        tenor = int(entry_tenor.get())
        monthly_payment = -npf.pmt(pricing / 12, tenor, loan_amount)
        result_label.config(text=f"Monthly Payment: {monthly_payment:.2f}")
    except ValueError:
        result_label.config(text="Invalid input. Enter numbers only.")

# GUI setup
root = tk.Tk()
root.title("Loan Calculator")

tk.Label(root, text="Loan Amount:").grid(row=0, column=0)
entry_loan = tk.Entry(root)
entry_loan.grid(row=0, column=1)

tk.Label(root, text="Annual Interest Rate (e.g., 0.05):").grid(row=1, column=0)
entry_rate = tk.Entry(root)
entry_rate.grid(row=1, column=1)

tk.Label(root, text="Tenor (months):").grid(row=2, column=0)
entry_tenor = tk.Entry(root)
entry_tenor.grid(row=2, column=1)

tk.Button(root, text="Calculate", command=calculate_payment).grid(row=3, column=0, columnspan=2)
result_label = tk.Label(root, text="")
result_label.grid(row=4, column=0, columnspan=2)

root.mainloop()