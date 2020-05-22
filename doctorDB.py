class Doctor:

    doctorid
    doctorname
    specialization
    consultationFee
    
    def __init__(self, doctorid, doctorname, specialization, consultationFee):
        self.doctorid = doctorid
        self.doctorname = doctorname
        self.specialization = specialization
        self.consultationFee = consultationFee

class Hospital:
    doctorDB = {
        Serialnumber : Doctor
    }

    def __init__(self, doctorDB):
        self.doctorDB = doctorDB

class if __name__ == "__main__":
    serialnumber = input("serial number")
    doc