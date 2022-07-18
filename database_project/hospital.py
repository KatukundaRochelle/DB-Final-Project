from cs50 import SQL
import csv

open("hospital.db","w").close()

db = SQL("sqlite:///hospital.db")
db.execute ("CREATE TABLE patients(patient_id INTEGER PRIMARY KEY, patient_name TEXT, gender TEXT, age INTEGER, p_department TEXT);")
db.execute("CREATE TABLE doctors(doctor_id INTEGER PRIMARY KEY, doctor_name TEXT, field TEXT);")
db.execute("CREATE TABLE admission(admission_id INTEGER PRIMARY KEY, p_department TEXT, fee INTEGER);")
db.execute("CREATE TABLE treatment(patient_id INTEGER, doctor_id TEXT, admission_id TEXT, FOREIGN KEY(patient_id) REFERENCES patients(patient_id), FOREIGN KEY(doctor_id) REFERENCES doctors(doctor_id),FOREIGN KEY(admission_id) REFERENCES admission(admission_id));")



with open("hospital.csv", "r") as file:
    reader=csv.DictReader(file)

    for row in reader:
        
        p_id=row["patient_id"].strip().capitalize()
        p_name=row["patient_name"].strip().capitalize()
        gender=row["gender"].strip().capitalize()
        age=row["age"].strip().capitalize()
        p_dept=row["p_department"].strip().capitalize()
        fee=row["fee"].strip().capitalize()
        d_id=row["doctor_id"].strip().capitalize()
        d_name=row["doctor_name"].strip().capitalize()
        field=row["field"].strip().capitalize()
        ad_id=row["admission_id"].strip().capitalize()

        db.execute("INSERT INTO patients(patient_id, patient_name, gender, age, p_department) VALUES (?,?,?,?,?);", p_id, p_name, gender, age, p_dept)
        db.execute("INSERT INTO doctors(doctor_id, doctor_name, field) VALUES (?,?,?);", d_id, d_name, field)
        db.execute("INSERT INTO admission(admission_id, p_department, fee) VALUES (?,?,?);", ad_id, p_dept, fee)
        db.execute("INSERT INTO treatment(patient_id, doctor_id, admission_id) VALUES (?,?,?);", p_id, d_id, ad_id)