from basys_ai_processor import BasysAIProcessor
from ehr_client import EHRClient
from um_client import UMClient
from util import retry


def main(patient_id):
    # Initialize clients
    cerner_client = EHRClient("Cerner")
    # basys_processor could also be dependent on the EHR client, if the responses of the clients are different, to keep it simple I haven't done that here.
    basys_processor = BasysAIProcessor()
    um_client = UMClient()

    # Fetch patient information from EHR
    def fetch_patient_info():
        return cerner_client.fetch_patient_info(patient_id)

    patient_info = retry(fetch_patient_info)
    print("Fetched patient info from EHR:")
    print(patient_info)

    # Process the information with basys.ai
    def process_patient_info():
        return basys_processor.process_patient_info(patient_info)

    processed_info = retry(process_patient_info)
    print("\nProcessed patient info with basys.ai:")
    print(processed_info)

    # Send the processed information to Unified Medical
    def send_patient_info():
        return um_client.send_patient_info(processed_info)

    um_response = retry(send_patient_info)
    print("\nResponse from Unified Medical:")
    print(um_response)


if __name__ == "__main__":
    patient_id = "12345"
    main(patient_id)
