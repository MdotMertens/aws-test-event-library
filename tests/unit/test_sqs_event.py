import pytest
import json
from typing import Any, AnyStr 
from aws_event_test_library.events.sqs_event import SQSEvent

def test_sqs_event_should_be_a_dict():
    event_object = SQSEvent()

    assert type(event_object.generate_event()) is dict 

def test_sqs_event_should_have_records():
    event_ojbect = SQSEvent()

    assert "Records" in event_ojbect.generate_event()

def test_sqs_event_with_payload_should_have_a_list_of_records():
    event_object = SQSEvent()

    event_object.add_payload("test")

    event = event_object.generate_event()

    assert event.get("Records") is not None 

def test_sqs_event_without_payloads_should_return_none():
    event_object = SQSEvent()

    event = event_object.generate_event()

    assert event.get("Records") is None 

def test_sqs_event_adding_none_should_throw_value_exception():
    event_object = SQSEvent()

    with pytest.raises(ValueError):
        event_object.add_payload(None)

def test_sqs_event_body_with_primitive_body_key_should_be_string():
    event_object = SQSEvent()

    event_object.add_payload({"test": 123})

    event = event_object.generate_event()
    first_record_body = event.get("Records")[0].get("body") 

    assert type(first_record_body) == str 


def test_sqs_event_body_with_complex_body_key_should_be_string():
    event_object = SQSEvent()
    payload = SQSEvent()
    payload.add_payload("something")
    event_object.add_payload(payload=payload.generate_event())

    event = event_object.generate_event()

    first_record_body = event.get("Records")[0].get("body") 
    json_record_body = json.loads(first_record_body.replace("'", '"'))
    complex_type_payload = (json_record_body.get("Records")[0].get("body"))

    assert type(first_record_body) == str 
    assert complex_type_payload == "something"
