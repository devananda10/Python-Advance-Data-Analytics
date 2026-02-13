class Customer:
    def __init__(self, customer_id):
        self.customer_id = customer_id


class KYCVerification(Customer):

    kyc_database = {}

    def __init__(self, customer_id, aadhaar, pan):
        super().__init__(customer_id)
        self.aadhaar = aadhaar
        self.pan = pan
        self.status = "Pending"

    def validate_aadhaar(self):
        return self.aadhaar.isdigit() and len(self.aadhaar) == 12

    def validate_pan(self):
        if len(self.pan) != 10:
            return False
        if not (self.pan[:5].isalpha() and
                self.pan[:5].isupper() and
                self.pan[5:9].isdigit() and
                self.pan[9].isalpha() and
                self.pan[9].isupper()):
            return False
        return True

    def check_duplicate(self):
        for record in KYCVerification.kyc_database.values():
            if record["Aadhaar"] == self.aadhaar:
                print("Aadhaar already registered!")
                return True
            if record["PAN"] == self.pan:
                print("PAN already registered!")
                return True
        return False

    def store_kyc(self):
        if self.check_duplicate():
            return

        KYCVerification.kyc_database[self.customer_id] = {
            "Aadhaar": self.aadhaar,
            "PAN": self.pan,
            "Status": self.status
        }
        print("KYC Submitted Successfully. Status: Pending")

    @classmethod
    def approve_kyc(cls, customer_id):
        if customer_id in cls.kyc_database:
            cls.kyc_database[customer_id]["Status"] = "Approved"
            print("KYC Approved Successfully.")
        else:
            print("Customer ID not found.")


while True:
    print("\n--- KYC VERIFICATION ---")
    cid = input("Enter Customer ID: ")
    aadhaar = input("Enter Aadhaar Number: ")
    pan = input("Enter PAN Number: ")

    kyc = KYCVerification(cid, aadhaar, pan)

    if not kyc.validate_aadhaar():
        print("Invalid Aadhaar Number! Must be 12 digits.")
        continue

    if not kyc.validate_pan():
        print("Invalid PAN Number! Format: AAAAA9999A")
        continue

    kyc.store_kyc()

    choice = input("Add another KYC? (yes/no): ")
    if choice.lower() != "yes":
        break


print("\n--- All KYC Records ---")
for cid, details in KYCVerification.kyc_database.items():
    print(f"Customer ID: {cid}, Details: {details}")
