# OpenAI API のレスポンス dataclasses

from dataclasses import dataclass
from enum import Enum

@dataclass
class _Role(Enum):
    ASSISTANT = 'assistant'
    SYSTEM = 'system'
    USER = 'user'


@dataclass
class _ChatMessage:
    content: str
    role: _Role

@dataclass
class _ChatCompletionChoice:
    index: int
    finish_reason: str
    message: _ChatMessage

@dataclass
class _Usage:
    completion_tokens: int
    prompt_tokens: int
    total_tokens: int

@dataclass
class ChatCompletionResult:
    choices: list[_ChatCompletionChoice]
    created: int
    id: str
    model: str
    object: str
    usage: _Usage

    def __repr__(self) -> str:
        return f'''ChatCompletionResult(
            choices='{self.choices}',
            created='{self.created}',
            id='{self.id}',
            model='{self.model}',
            object='{self.object}',
            usage='{self.usage}',
)'''

