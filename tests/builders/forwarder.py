from unittest.mock import MagicMock

from s3mesh.forwarder import MeshToS3Forwarder


def build_forwarder(**kwargs):
    mock_mesh_inbox = kwargs.get("mesh_inbox", MagicMock())
    mock_uploader = kwargs.get("uploader", MagicMock())
    mock_probe = kwargs.get("probe", MagicMock())
    mock_uploader.upload.side_effect = kwargs.get("uploader_error", None)
    mock_mesh_inbox.read_messages.return_value = kwargs.get("incoming_messages", [])
    mock_mesh_inbox.read_messages.side_effect = kwargs.get("read_error", None)
    mock_mesh_inbox.count_messages.side_effect = kwargs.get("count_error", None)
    mock_mesh_inbox.count_messages.return_value = kwargs.get("inbox_message_count", 0)

    return MeshToS3Forwarder(mock_mesh_inbox, mock_uploader, mock_probe)
