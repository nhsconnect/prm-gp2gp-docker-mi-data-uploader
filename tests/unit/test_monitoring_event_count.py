from unittest.mock import MagicMock

from awsmesh.monitoring.error import MESH_CLIENT_NETWORK_ERROR
from awsmesh.monitoring.event.count import COUNT_MESSAGES_EVENT, CountMessagesEvent


def test_finish_calls_log_event_with_event_name():
    mock_output = MagicMock()

    count_messages_event = CountMessagesEvent(mock_output)
    count_messages_event.finish()

    mock_output.log_event.assert_called_with(COUNT_MESSAGES_EVENT, {})


def test_record_message_count():
    mock_output = MagicMock()
    message_count = 2

    count_messages_event = CountMessagesEvent(mock_output)
    count_messages_event.record_message_count(message_count)
    count_messages_event.finish()

    mock_output.log_event.assert_called_with(
        COUNT_MESSAGES_EVENT, {"inboxMessageCount": message_count}
    )


def test_record_mesh_client_network_error():
    mock_output = MagicMock()
    error_message = "Oh no!"
    mock_exception = MagicMock()
    mock_exception.error_message = error_message

    count_messages_event = CountMessagesEvent(mock_output)
    count_messages_event.record_mesh_client_network_error(mock_exception)
    count_messages_event.finish()

    mock_output.log_event.assert_called_with(
        COUNT_MESSAGES_EVENT, {"error": MESH_CLIENT_NETWORK_ERROR, "errorMessage": error_message}
    )
