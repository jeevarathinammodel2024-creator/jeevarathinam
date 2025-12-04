# Hospital Patient Record System

patients = []   # list to store all patient records


def add_patient():
    print("\n--- Add New Patient ---")
    pid = input("Enter Patient ID: ")
    name = input("Enter Patient Name: ")
    age = int(input("Enter Age: "))
    gender = input("Enter Gender (M/F): ")
    disease = input("Enter Disease/Symptoms: ")
    doctor = input("Enter Doctor Assigned: ")
    phone = input("Enter Phone Number: ")

    patient = {
        "ID": pid,
        "Name": name,
        "Age": age,
        "Gender": gender,
        "Disease": disease,
        "Doctor": doctor,
        "Phone": phone
    }

    patients.append(patient)
    print("\nPatient Added Successfully!\n")


def view_patients():
    print("\n--- Patient Records ---")
    if not patients:
        print("No patient records found.\n")
        return

    for p in patients:
        print(f"ID: {p['ID']}")
        print(f"Name: {p['Name']}")
        print(f"Age: {p['Age']}")
        print(f"Gender: {p['Gender']}")
        print(f"Disease/Symptoms: {p['Disease']}")
        print(f"Doctor Assigned: {p['Doctor']}")
        print(f"Phone: {p['Phone']}")
        print("-" * 30)


def search_patient():
    print("\n--- Search Patient ---")
    pid = input("Enter Patient ID to search: ")

    for p in patients:
        if p["ID"] == pid:
            print("\nPatient Found:")
            print(f"Name: {p['Name']}")
            print(f"Age: {p['Age']}")
            print(f"Gender: {p['Gender']}")
            print(f"Disease: {p['Disease']}")
            print(f"Doctor Assigned: {p['Doctor']}")
            print(f"Phone: {p['Phone']}\n")
            return

    print("No patient found with that ID.\n")


def delete_patient():
    print("\n--- Delete Patient ---")
    pid = input("Enter Patient ID to delete: ")

    for p in patients:
        if p["ID"] == pid:
            patients.remove(p)
            print("\nPatient Deleted Successfully!\n")
            return

    print("No patient found with that ID.\n")


def main_menu():
    while True:
        print("===== Hospital Patient Record System =====")
        print("1. Add Patient")
        print("2. View All Patients")
        print("3. Search Patient")
        print("4. Delete Patient")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_patient()
        elif choice == "2":
            view_patients()
        elif choice == "3":
            search_patient()
        elif choice == "4":
            delete_patient()
        elif choice == "5":
            print("Exiting... Thank you!")
            break
        else:
            print("Invalid choice! Try again.\n")


# Run the program
main_menu()
