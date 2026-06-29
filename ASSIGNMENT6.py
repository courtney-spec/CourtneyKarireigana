import csv
import json
import logging
import os

# ==============================
# LOGGING SETUP
# ==============================
logging.basicConfig(
    filename="student_system.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

# ==============================
# CUSTOM EXCEPTION
# ==============================
class StudentNotFoundError(Exception):
    pass


# ==============================
# FILE NAMES
# ==============================
CSV_FILE = "students.csv"
JSON_FILE = "students.json"


# ==============================
# INITIAL FILE SETUP
# ==============================
def initialize_files():
    if not os.path.exists(CSV_FILE):
        with open(CSV_FILE, "w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(["reg_no", "name", "age", "program"])

    if not os.path.exists(JSON_FILE):
        with open(JSON_FILE, "w") as file:
            json.dump({}, file)


# ==============================
# ADD STUDENT
# ==============================
def add_student():
    try:
        reg_no = input("Enter registration number: ").strip()
        name = input("Enter name: ").strip()
        age = int(input("Enter age: "))
        program = input("Enter program: ").strip()

        address = input("Enter address: ").strip()
        contact = input("Enter contact: ").strip()

        # Save CSV
        with open(CSV_FILE, "a", newline="") as file:
            writer = csv.writer(file)
            writer.writerow([reg_no, name, age, program])

        # Save JSON
        with open(JSON_FILE, "r") as file:
            data = json.load(file)

        data[reg_no] = {
            "address": address,
            "contact": contact
        }

        with open(JSON_FILE, "w") as file:
            json.dump(data, file, indent=4)

        logging.info(f"Added student {reg_no}")
        print("Student added successfully!")

    except ValueError:
        logging.error("Invalid age input")
        print("Error: Age must be a number.")

    except Exception as e:
        logging.error(f"Add student failed: {e}")
        print("An error occurred while adding student.")


# ==============================
# VIEW ALL STUDENTS
# ==============================
def view_students():
    try:
        with open(CSV_FILE, "r") as file:
            reader = csv.reader(file)
            next(reader)

            print("\n--- STUDENT LIST ---")
            for row in reader:
                print(row)

        logging.info("Viewed all students")

    except Exception as e:
        logging.error(f"View students failed: {e}")
        print("Error reading student records.")


# ==============================
# SEARCH STUDENT
# ==============================
def search_student():
    try:
        reg_no = input("Enter registration number: ").strip()
        found = False

        with open(CSV_FILE, "r") as file:
            reader = csv.reader(file)
            next(reader)

            for row in reader:
                if row[0] == reg_no:
                    print("\nStudent Found (CSV):", row)

                    with open(JSON_FILE, "r") as jf:
                        data = json.load(jf)

                    print("Extra Details (JSON):", data.get(reg_no, {}))

                    found = True
                    logging.info(f"Searched student {reg_no}")
                    break

        if not found:
            raise StudentNotFoundError("Student does not exist.")

    except StudentNotFoundError as e:
        logging.warning(str(e))
        print(e)

    except Exception as e:
        logging.error(f"Search error: {e}")
        print("Error searching student.")


# ==============================
# UPDATE STUDENT
# ==============================
def update_student():
    try:
        reg_no = input("Enter registration number to update: ").strip()
        rows = []
        found = False

        with open(CSV_FILE, "r") as file:
            reader = csv.reader(file)
            header = next(reader)
            rows.append(header)

            for row in reader:
                if row[0] == reg_no:
                    found = True
                    print("Current data:", row)

                    row[1] = input("Enter new name: ")
                    row[2] = input("Enter new age: ")
                    row[3] = input("Enter new program: ")

                rows.append(row)

        if not found:
            raise StudentNotFoundError("Student not found for update.")

        with open(CSV_FILE, "w", newline="") as file:
            writer = csv.writer(file)
            writer.writerows(rows)

        # Update JSON
        with open(JSON_FILE, "r") as file:
            data = json.load(file)

        if reg_no in data:
            data[reg_no]["address"] = input("Enter new address: ")
            data[reg_no]["contact"] = input("Enter new contact: ")

        with open(JSON_FILE, "w") as file:
            json.dump(data, file, indent=4)

        logging.info(f"Updated student {reg_no}")
        print("Student updated successfully!")

    except StudentNotFoundError as e:
        logging.warning(str(e))
        print(e)

    except Exception as e:
        logging.error(f"Update error: {e}")
        print("Error updating student.")


# ==============================
# DELETE STUDENT
# ==============================
def delete_student():
    try:
        reg_no = input("Enter registration number to delete: ").strip()
        rows = []
        found = False

        with open(CSV_FILE, "r") as file:
            reader = csv.reader(file)
            header = next(reader)
            rows.append(header)

            for row in reader:
                if row[0] != reg_no:
                    rows.append(row)
                else:
                    found = True

        if not found:
            raise StudentNotFoundError("Student not found for deletion.")

        with open(CSV_FILE, "w", newline="") as file:
            writer = csv.writer(file)
            writer.writerows(rows)

        # Remove from JSON
        with open(JSON_FILE, "r") as file:
            data = json.load(file)

        data.pop(reg_no, None)

        with open(JSON_FILE, "w") as file:
            json.dump(data, file, indent=4)

        logging.info(f"Deleted student {reg_no}")
        print("Student deleted successfully!")

    except StudentNotFoundError as e:
        logging.warning(str(e))
        print(e)

    except Exception as e:
        logging.error(f"Delete error: {e}")
        print("Error deleting student.")


# ==============================
# MENU
# ==============================
def menu():
    initialize_files()

    while True:
        print("\n===== STUDENT SYSTEM MENU =====")
        print("1. Add Student")
        print("2. View Students")
        print("3. Search Student")
        print("4. Update Student")
        print("5. Delete Student")
        print("6. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            add_student()
        elif choice == "2":
            view_students()
        elif choice == "3":
            search_student()
        elif choice == "4":
            update_student()
        elif choice == "5":
            delete_student()
        elif choice == "6":
            print("Exiting system...")
            break
        else:
            print("Invalid choice!")


if __name__ == "__main__":
    menu()