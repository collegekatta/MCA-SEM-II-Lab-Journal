import pymongo

# Establish a connection to MongoDB
client = pymongo.MongoClient("mongodb://localhost:27017/")

# Create or switch to the database
db = client["hospital_db"]

# Create or switch to the collection for Hospital and Doctor tables
hospital_collection = db["hospital"]
doctor_collection = db["doctor"]

# 1. Insert 10 records in both Hospital and Doctor tables
def insert_records():
    hospitals = [
        {"Hospital_Id": 1, "Hospital_Name": "City Hospital", "Bed_Count": 100},
        {"Hospital_Id": 2, "Hospital_Name": "General Hospital", "Bed_Count": 150},
    ]
    doctors = [
        {"Doctor_Id": 101, "Doctor_Name": "Dr. John", "Hospital_Id": 1, "Joining_Date": "2022-03-15", "Speciality": "Cardiology", "Salary": 80000, "Experience": 5},
        {"Doctor_Id": 102, "Doctor_Name": "Dr. Emily", "Hospital_Id": 1, "Joining_Date": "2021-07-20", "Speciality": "Orthopedics", "Salary": 90000, "Experience": 8},
    ]
    hospital_collection.insert_many(hospitals)
    doctor_collection.insert_many(doctors)

# 2. Fetch Hospital and Doctor Information using hospital Id and doctor Id
def fetch_hospital_doctor_info(hospital_id, doctor_id):
    hospital_info = hospital_collection.find_one({"Hospital_Id": hospital_id})
    doctor_info = doctor_collection.find_one({"Doctor_Id": doctor_id})
    return hospital_info, doctor_info

# 3. Fetch all doctors whose salary higher than the input amount and specialty is the same as the input specialty
def fetch_doctors_by_salary_and_specialty(salary, specialty):
    doctors = doctor_collection.find({"Salary": {"$gt": salary}, "Speciality": specialty})
    return list(doctors)

# 4. Update doctor experience in years
def update_doctor_experience(doctor_id, experience):
    doctor_collection.update_one({"Doctor_Id": doctor_id}, {"$set": {"Experience": experience}})

# Main function
def main():
    insert_records()

    # 2. Fetch Hospital and Doctor Information
    hospital_id = int(input("Enter Hospital ID: "))
    doctor_id = int(input("Enter Doctor ID: "))
    hospital_info, doctor_info = fetch_hospital_doctor_info(hospital_id, doctor_id)
    print("Hospital Information:", hospital_info)
    print("Doctor Information:", doctor_info)

    # 3. Fetch doctors by salary and specialty
    salary = int(input("Enter minimum salary: "))
    specialty = input("Enter specialty: ")
    doctors = fetch_doctors_by_salary_and_specialty(salary, specialty)
    print("Doctors with salary higher than", salary, "and specialty", specialty, ":", doctors)

    # 4. Update doctor experience
    doctor_id = int(input("Enter Doctor ID to update experience: "))
    experience = int(input("Enter new experience in years: "))
    update_doctor_experience(doctor_id, experience)
    print("Doctor experience updated successfully.")

if __name__ == "__main__":
    main()
