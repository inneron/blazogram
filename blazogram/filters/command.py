from .base import BaseFilter
from ..types.message import Message

class Command(BaseFilter):
    def __init__(self, command: str):
        self.command = '/' + command.lower().strip()

    async def __check__(self, message: Message) -> bool:
        text = message.text.lower().strip()
        return text == self.command
