# https://platform.openai.com/docs/guides/chat

import openai
import os
from dotenv import load_dotenv
from api.completion import ChatCompletionResult
load_dotenv('.env')

openai.organization = os.environ.get("OPENAI_ORGANIZATION")
openai.api_key = os.environ.get("OPENAI_API_KEY")

# question = 'ChatGPT APIの role である \'system\', \'user\', \'assistant\'の違いを教えてください'
# question = 'python の dataclass を使って web api から受け取ったレスポンスを dataclass に変換するコード例を示して'
question = 'python の dataclass を print するときに綺麗な表示になるためのコード例を教えてください。また、日本語が文字化けするので解決方法を教えて'

# モデルの定義
model = 'gpt-3.5-turbo'
## 回答文字数を絞ることで、レスポンスを高速化
character_limit = 250
## messages の role は 'system', 'user' または 'assistant'
### system: Chatの役割。前提条件
### user: Userの質問内容
### assistant: Chatが返してきた内容
### また、これまでのやりとりも全て含めて、+でuserの質問を追加してレスポンスを受け取る形で使う
## token数は https://platform.openai.com/tokenizer で大体の値を計測可能。'system'はtoken数節約のため、英語で作った方がいいかも
messages = [
    {
        'role': 'system',
        'content': f'''
        条件:
        - あなたはプロのpythonエンジニアです
        - プロなので、誤っていることは誤っていると説明し、説明に際して必要な質問をしてください
        - 相手は日本語しかわかりません。日本語で回答してください
        - プロなので、簡潔に回答することが大切です。{character_limit} 文字以内で回答してください
        '''
    },
    {
        'role': 'user',
        'content': question
    }
]

response = openai.ChatCompletion.create(
    model = model,
    messages = messages,
)
result = ChatCompletionResult(**response)

print(result)
print(result.choices[0].message.content)
