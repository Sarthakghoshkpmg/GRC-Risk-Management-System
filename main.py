import tkinter as tk
from tkinter import messagebox, ttk
import csv
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

# Load synthetic dataset (sample from 1000 rows)
synthetic_data = [
    ["Unauthorized access to sensitive data", "Access Control Policy", "Implement multi-factor authentication", 
     "Weak password enforcement", "ISO 27001: A.9.4.2", "Finance Department"],
    ["Data breach due to phishing", "Cybersecurity Awareness Policy", "Conduct regular phishing simulations", 
     "Lack of employee training", "NIST 800-53: AT-2", "IT Security"],
    ["Non-compliance with financial regulations", "Regulatory Compliance Policy", "Ensure periodic audits", 
     "Delayed audit reporting", "SOX Section 404", "Accounting Division"],
    ["System downtime affecting operations", "Business Continuity Policy", "Maintain redundant infrastructure", 
     "No disaster recovery plan", "ISO 22301: 8.3", "Operations Team"],
    ["Fraudulent transactions", "Fraud Prevention Policy", "Monitor transaction anomalies", 
     "Insufficient fraud detection", "PCI DSS Requirement 10", "Retail Banking"]
]

column_names = ["Risk Statement", "Policy", "Control Objectives", "Issue", "Citation", "Business Context"]
dataset_columns = list(zip(*synthetic_data))  # Transpose dataset for validation reference

# Function to validate user entries against historical data
def validate_entries(user_data):
    return all(user_data[field] in dataset_columns[idx] for idx, field in enumerate(column_names))

# Function to generate AI-style risk report
def generate_report(user_data):
    report_window = tk.Toplevel(root)
    report_window.title("AI-Generated Risk Analysis Report")
    report_window.geometry("600x400")

    report_text = "📢 **AI Risk Analysis Report**\n\n"
    report_text += "🚀 Greetings! The system has analyzed your risk submission and detected key insights:\n\n"

    report_text += f"🔍 **Risk Statement:** {user_data['Risk Statement']}\n"
    report_text += f"📌 **Policy Applied:** {user_data['Policy']}\n"
    report_text += f"✅ **Control Objective:** {user_data['Control Objectives']}\n"
    report_text += f"🚨 **Issue Identified:** {user_data['Issue']}\n"
    report_text += f"📜 **Regulatory Citation:** {user_data['Citation']}\n"
    report_text += f"🏢 **Business Context:** {user_data['Business Context']}\n\n"

    report_text += "📊 **Recommended Actions:**\n"
    report_text += "- Strengthen **access control measures** against unauthorized access.\n"
    report_text += "- Conduct **cybersecurity awareness training** for employees.\n"
    report_text += "- Improve **audit tracking** for compliance verification.\n\n"

    messagebox.showinfo("Risk Analysis Report", report_text)

    # Graph visualization
    fig, ax = plt.subplots(figsize=(5, 3))
    ax.barh(list(user_data.keys()), list(user_data.values()))
    ax.set_title("Risk Submission Overview")
    ax.set_xlabel("Categories")
    ax.set_ylabel("User Entries")

    canvas = FigureCanvasTkAgg(fig, master=report_window)
    canvas.draw()
    canvas.get_tk_widget().pack()

# Function to handle predefined template selection
def open_dropdown_form():
    dropdown_window = tk.Toplevel(root)
    dropdown_window.title("Select Predefined Values")
    dropdown_window.geometry("500x500")

    dropdown_entries = {}

    for idx, field in enumerate(column_names):
        tk.Label(dropdown_window, text=field).grid(row=idx, column=0, padx=10, pady=5, sticky="w")
        dropdown = ttk.Combobox(dropdown_window, values=list(set(dataset_columns[idx])), width=40)
        dropdown.grid(row=idx, column=1, padx=10, pady=5)
        dropdown_entries[field] = dropdown

    def submit_dropdown_form():
        user_data = {field: dropdown_entries[field].get() for field in column_names}
        file_name = "grc_dataset_entries.csv"
        with open(file_name, mode="a", newline="", encoding="utf-8") as file:
            writer = csv.writer(file)
            if file.tell() == 0:
                writer.writerow(column_names)
            writer.writerow(list(user_data.values()))

        messagebox.showinfo("Success", "🎉 Your predefined template selection has been recorded!")
        dropdown_window.destroy()  # Close dropdown selection window

        # Generate AI report immediately after selection
        generate_report(user_data)

    tk.Button(dropdown_window, text="Submit Selection", command=submit_dropdown_form).grid(row=len(column_names), columnspan=2, pady=20)

# Function to handle form submission & predefined template selection
def submit_form():
    user_data = {field: entries[field].get() for field in column_names}

    use_template = messagebox.askyesno("Pre-filled Format", "Do you want to use the predefined template?")
    
    if use_template:
        root.withdraw()  # Hide main form
        open_dropdown_form()  # Open dropdown selection window
    else:
        if not validate_entries(user_data):
            messagebox.showerror("Invalid Entry", "🚨 Your risk submission does not match historical patterns. Please revise.")
            return

        file_name = "grc_dataset_entries.csv"
        with open(file_name, mode="a", newline="", encoding="utf-8") as file:
            writer = csv.writer(file)
            if file.tell() == 0:
                writer.writerow(column_names)
            writer.writerow(list(user_data.values()))

        messagebox.showinfo("Success", "🎉 Your risk submission has been verified and recorded.")

        # Generate AI report after successful validation
        generate_report(user_data)

# Create main UI window
root = tk.Tk()
root.title("GRC AI Risk Management System")
root.geometry("500x450")

entries = {}

for idx, field in enumerate(column_names):
    tk.Label(root, text=field).grid(row=idx, column=0, padx=10, pady=5, sticky="w")
    entry = tk.Entry(root, width=40)
    entry.grid(row=idx, column=1, padx=10, pady=5)
    entries[field] = entry

tk.Button(root, text="Submit", command=submit_form).grid(row=len(column_names), columnspan=2, pady=10)

root.mainloop()
