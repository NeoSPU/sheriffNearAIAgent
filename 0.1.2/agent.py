import json
from nearai.agents.environment import Environment
import constants
import os

MODEL = "llama-v3p3-70b-instruct"
VECTOR_STORE_ID = os.environ.get('VECTOR_STORE_ID')

print(VECTOR_STORE_ID)

def run(env: Environment):
    user_query = env.list_messages()[-1]["content"]

    # Query the Vector Store
    vector_results = env.query_vector_store(VECTOR_STORE_ID, user_query)
    docs = [{"file": res["chunk_text"]} for res in vector_results[:6]]

    user_query += '\n'
    user_query += constants.assistant_role_content

    prompt['content'] += '\n '

    prompt = [
        {
            "role": "user query",
            "content": user_query,
        },
        {
            "role": "documentation",
            "content": json.dumps(docs),
        },
        {
            "role": "accent",
            "content": constants.assistant_role_content,
        },
        {
            "role": "system",
            "content": "Provide a brief but complete answer to the user's request, checking whether there is a vulnerability in the code or in part of the smart contract code using the information about your role provided in accent. When answering, carefully use the data from the studies of vulnerabilities in the smart contract code provided in the documentation. If a vulnerability is detected in the provided code or part of it, provide the user with steps to eliminate it. For"
        }
    ]

    answer = env.completion(model=MODEL, messages=prompt)
    env.add_reply(answer)


run(env)