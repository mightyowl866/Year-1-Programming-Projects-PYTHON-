class Doctor:
    __doctor_id = 0

    def __init__(self, doctor_name: str, max_patients: int = 10):
        if isinstance(doctor_name, str) and isinstance(max_patients, int):
            Doctor.__doctor_id += 1
            self.__id = "Doctor_" + str(Doctor.__doctor_id)
            self.__name = doctor_name
            self.__patients = []
            self.__max_patients = max_patients
        else:
            raise TypeError(
                "Name should be a string and max_patients must be an int.")

    @property
    def id(self):
        return self.__id

    @property
    def can_take_patient(self):
        return len(self.__patients) < self.__max_patients

    @property
    def name(self):
        return self.__name

    def add_patient(self, patient):
        if isinstance(patient, Patient):
            if self.can_take_patient:
                self.__patients.append(patient)
            else:
                raise Exception("Doctor is fully booked. Try another doctor.")
        else:
            raise TypeError("The argument must be of Type Patient")

    def remove_patient(self, patient):
        if isinstance(patient, Patient):
            if patient in self.__patients:
                self.__patients.remove(patient)
            else:
                raise ValueError("This patient is not registered with me")
        else:
            raise TypeError("The argument must be of Type Patient")

    def __str__(self):
        result = str(self.id) + ": " + self.name + "\n"
        for patient in self.__patients:
            result = result + patient.name + "\n"
        return result


class Patient:
    __patient_id = 0

    def __init__(self, patient_name: str, doctor):
        if isinstance(patient_name, str):
            Patient.__patient_id += 1
            self.__id = "Patient_" + str(Patient.__patient_id)
            self.__name = patient_name
        else:
            raise TypeError("Name should be a string")

        if isinstance(doctor, Doctor):
            self.__doctor = doctor
            self.__doctor.add_patient(self)
        else:
            raise TypeError("Argument must be a Doctor")


    @property
    def id(self):
        return self.__id

    @property
    def name(self):
        return self.__name

    def change_doctor(self, new_doctor):
        if isinstance(new_doctor, Doctor):
            self.__doctor.remove_patient(self)
            self.__doctor = new_room
            self.__doctor.add_patient(self)
        else:
            raise TypeError("Argument must be a Room")

    def discharge(self):
        self.__doctor.remove_patient(self)

    def __str__(self):
        result = "My name is " + self.__name + "\n"
        result = result + "My Doctor is " + self.__doctor.name + "\n"
        return result