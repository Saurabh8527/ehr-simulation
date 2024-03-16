import time

from util import simulate_error


class BasysAIProcessor:
    def process_patient_info(self, patient_info):
        processed_info = self._simulate_basys_ai_processing(patient_info)
        return processed_info

    def _simulate_basys_ai_processing(self, patient_info):
        time.sleep(1)
        simulate_error(error_chance=0.1)
        processed_info = (
            patient_info.copy()
        )  # Create a copy of the original info, to avoid changing the original one
        processed_info["processed"] = True
        processed_info["risk_assessment"] = self._simulate_risk_assessment(patient_info)
        return processed_info

    def _simulate_risk_assessment(self, patient_info):
        risk = "Low"
        for entry in patient_info.get("entry", []):
            condition = entry.get("resource", {}).get("code", {}).get("text", "")
            if "coronary artery disease" in condition:
                risk = "High"
                break
        return risk
