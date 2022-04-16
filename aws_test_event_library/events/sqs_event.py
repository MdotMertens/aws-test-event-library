from typing import List, Optional, Any

class SQSEvent:
    _payloads: List 
    _event_message: Optional[dict] 

    def __init__(self) -> None:
        self._payloads = [] 
        self._event_message = {}

    def generate_event(self):
        dict_to_return = {}
        dict_to_return["Records"] = self._add_payloads_to_event()
        return dict_to_return 

    def add_payload(self, payload: Any):
        if not payload:
            raise ValueError("Payload cannot be of type None")
        self._payloads.append(payload)

    def _add_payloads_to_event(self) -> Optional[List]:
        if not self._payloads:
            return None

        record_list = []
        body_wrapper = {}

        for payload in self._payloads:
            payload = str(payload) 
            body_wrapper["body"] = payload
            record_list.append(body_wrapper)
        
        return record_list

