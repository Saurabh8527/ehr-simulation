import time

from util import simulate_error


class EHRClient:
    def __init__(self, system):
        self.system = system

    def fetch_patient_info(self, patient_id):
        if self.system == "Cerner":
            return self._simulate_cerner_patient_info(patient_id)
        elif self.system == "Epic":
            return self._simulate_epic_patient_condition(patient_id)
        else:
            raise ValueError("Unsupported EHR system")

    def _simulate_cerner_patient_info(self, patient_id):
        simulate_error(error_chance=0.2)
        time.sleep(1)
        return {
            "resourceType": "Bundle",
            "type": "searchset",
            "total": 1,
            "entry": [
                {
                    "resource": {
                        "resourceType": "Condition",
                        "id": "example-id",
                        "patient": {
                            "display": "Derrick Lin",
                            "reference": f"https://fhir.epic.com/api/FHIR/DSTU2/Patient/{patient_id}",
                        },
                        "asserter": {
                            "display": "Physician Family Medicine, MD",
                            "reference": "https://fhir.epic.com/api/FHIR/DSTU2/Practitioner/example-practitioner-id",
                        },
                        "dateRecorded": "2019-05-28",
                        "code": {
                            "coding": [
                                {
                                    "system": "http://hl7.org/fhir/sid/icd-9-cm/diagnosis",
                                    "code": "V49.89",
                                    "display": "Risk for coronary artery disease between 10% and 20% in next 10 years",
                                }
                            ],
                            "text": "Risk for coronary artery disease between 10% and 20% in next 10 years",
                        },
                        "category": {
                            "coding": [
                                {
                                    "system": "http://hl7.org/fhir/condition-category",
                                    "code": "diagnosis",
                                    "display": "Diagnosis",
                                }
                            ],
                            "text": "Diagnosis",
                        },
                        "clinicalStatus": "active",
                        "verificationStatus": "confirmed",
                        "onsetDateTime": "2019-05-28",
                    }
                }
            ],
        }

    def _simulate_epic_patient_condition(self, patient_id):
        simulate_error(error_chance=0.2)
        time.sleep(1)
        return {
            "resourceType": "Bundle",
            "type": "searchset",
            "total": 1,
            "entry": [
                {
                    "resource": {
                        "resourceType": "Condition",
                        "id": "example-id",
                        "patient": {
                            "display": "Derrick Lin",
                            "reference": f"https://fhir.epic.com/api/FHIR/DSTU2/Patient/{patient_id}",
                        },
                        "asserter": {
                            "display": "Physician Family Medicine, MD",
                            "reference": "https://fhir.epic.com/api/FHIR/DSTU2/Practitioner/example-practitioner-id",
                        },
                        "dateRecorded": "2019-05-28",
                        "code": {
                            "coding": [
                                {
                                    "system": "http://hl7.org/fhir/sid/icd-9-cm/diagnosis",
                                    "code": "V49.89",
                                    "display": "Risk for coronary artery disease between 10% and 20% in next 10 years",
                                }
                            ],
                            "text": "Risk for coronary artery disease between 10% and 20% in next 10 years",
                        },
                        "category": {
                            "coding": [
                                {
                                    "system": "http://hl7.org/fhir/condition-category",
                                    "code": "diagnosis",
                                    "display": "Diagnosis",
                                }
                            ],
                            "text": "Diagnosis",
                        },
                        "clinicalStatus": "active",
                        "verificationStatus": "confirmed",
                        "onsetDateTime": "2019-05-28",
                    }
                }
            ],
        }
