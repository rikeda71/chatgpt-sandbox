# https://platform.openai.com/docs/api-reference/requesting-organization

import openai
import os
from dotenv import load_dotenv
load_dotenv('.env')

openai.organization = os.environ.get("OPENAI_ORGANIZATION")
openai.api_key = os.environ.get("OPENAI_API_KEY")

print('\n'.join([model['id'] for model in openai.Model.list()['data']]))
