import re
PATTERNS = {"IBAN": r"[A-Z]{2}\d{2}[ ]?[A-Z0-9]{4}[ ]?\d{4}[ ]?\d{4}[ ]?\d{4}"}
print("[+] Euro-GDPR-Leak-Hunter Started | Mehar Sindh")
test = "DE89 3704 0044 0532 0130 00"
for k,p in PATTERNS.items():
    m=re.findall(p,test)
    print(f"Found {k}: {m} - Risk 99/100 - GDPR Violation!")
