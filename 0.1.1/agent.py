import helper
import os
import constants

RAG_SECRET = os.environ.get('RAG_SECRET')
RAG_URL = os.environ.get('RAG_URL')

BAN_WORDS = env.read_file('banwords.txt')

prompt = {
    "role": "system",
    "content": constants.assistant_role_content
}

helper.handle_user_message(env, prompt, BAN_WORDS, RAG_URL, RAG_SECRET)
