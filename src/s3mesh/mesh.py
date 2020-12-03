from datetime import datetime
from typing import Iterable

from mesh_client import MeshClient, Message


class MeshMessage:
    def __init__(self, client_message: Message):
        if client_message.mex_header("statusevent") != "TRANSFER":
            raise UnexpectedStatusEvent()

        self.id: str = client_message.id()
        self._client_message: Message = client_message
        self.file_name: str = client_message.mex_header("filename")
        self.date_delivered: datetime = datetime.strptime(
            client_message.mex_header("statustimestamp"), "%Y%m%d%H%M%S"
        )

    def acknowledge(self):
        self._client_message.acknowledge()

    def read(self, n=None):
        return self._client_message.read(n)


class MeshInbox:
    def __init__(self, client: MeshClient):
        self._client = client

    def read_messages(self) -> Iterable[MeshMessage]:
        for client_message in self._client.iterate_all_messages():
            yield MeshMessage(client_message)


class UnexpectedStatusEvent(Exception):
    pass
