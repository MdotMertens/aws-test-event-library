import pytest
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
