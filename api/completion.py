# OpenAI API のレスポンス dataclasses

from dataclasses import dataclass, field
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

# FIXME: 辞書型から変換したときデフォルト値を詰めれるようにしたい
@dataclass
class _StreamChatDelta:
    content: str | None = field(default=None)
    role: _Role | None = field(default=None)

@dataclass
class _StreamChatCompletionChoice:
    index: int
    finish_reason: str
    delta: _StreamChatDelta

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

@dataclass
class StreamChatCompletionResult:
    '''
    Streaming 処理の場合
    '''
    choices: list[_StreamChatCompletionChoice]
    created: int
    id: str
    model: str
    object: str

    def __repr__(self) -> str:
        return f'''StreamChatCompletionResult(
choices='{self.choices}',
created='{self.created}',
id='{self.id}',
model='{self.model}',
object='{self.object}',
)'''
