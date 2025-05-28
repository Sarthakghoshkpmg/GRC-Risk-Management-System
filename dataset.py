import csv
import random

# Sample data pools for each category
risk_statements = [
    "Unauthorized access to sensitive data", "Data breach due to phishing",
    "Non-compliance with financial regulations", "System downtime affecting operations",
    "Fraudulent transactions", "Inadequate vendor risk assessment",
    "Weak password policies leading to breaches", "Insider threats impacting confidentiality"
]
policies = [
    "Access Control Policy", "Cybersecurity Awareness Policy",
    "Regulatory Compliance Policy", "Business Continuity Policy",
    "Fraud Prevention Policy", "Vendor Risk Assessment Policy"
]
control_objectives = [
    "Implement multi-factor authentication", "Conduct regular phishing simulations",
    "Ensure periodic audits", "Maintain redundant infrastructure",
    "Monitor transaction anomalies", "Enforce strong password policies",
    "Establish real-time threat monitoring"
]
issues = [
    "Weak password enforcement", "Lack of employee training",
    "Delayed audit reporting", "No disaster recovery plan",
    "Insufficient fraud detection", "Inadequate risk mitigation strategies"
]
citations = [
    "ISO 27001: A.9.4.2", "NIST 800-53: AT-2", "SOX Section 404",
    "ISO 22301: 8.3", "PCI DSS Requirement 10", "GDPR Article 32"
]
business_contexts = [
    "Finance Department", "IT Security", "Accounting Division",
    "Operations Team", "Retail Banking", "Legal Compliance"
]

# Define the CSV file name
file_name = "synthetic_grc_dataset_1000.csv"

# Generate 1000 rows of synthetic data
with open(file_name, mode="w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)
    writer.writerow(["Risk Statement", "Policy", "Control Objectives", "Issue", "Citation", "Business Context"])  # Header
    for _ in range(1000):
        writer.writerow([
            random.choice(risk_statements), random.choice(policies),
            random.choice(control_objectives), random.choice(issues),
            random.choice(citations), random.choice(business_contexts)
        ])

print(f"Generated synthetic GRC dataset with 1000 rows: '{file_name}'")
