import time

from util import simulate_error


class UMClient:
    def __init__(self):
        self.base_url = "https://api.unifiedmedical.com"

    def send_patient_info(self, processed_info):
        response = self._simulate_um_api_call(processed_info)
        return response

    def _simulate_um_api_call(self, processed_info):
        simulate_error(error_chance=0.2)
        time.sleep(1)

        patient_condition = (
            processed_info.get("entry", [])[0]
            .get("resource", {})
            .get("code", {})
            .get("text", "")
        )
        risk_assessment = processed_info.get("risk_assessment", "Unknown")

        return {
            "status": "success",
            "message": f"Patient condition ({patient_condition}) and risk assessment ({risk_assessment}) updated successfully in UM",
            "patient_id": processed_info.get("entry", [])[0]
            .get("resource", {})
            .get("patient", {})
            .get("reference", ""),
        }
