import requests
import json
import asyncio

# Method for use Knowledge Base for RAG pattern and find relevant context
def find_relevant_context(question, rag_url, rag_secret):
    if not rag_secret:
        return ''

    payload = json.dumps({
        "user_question": question
    })
    headers = {
        'Content-Type': 'application/json',
        'x-api-key': rag_secret
    }

    response = requests.request("POST", rag_url, headers=headers, data=payload)

    if response.status_code == 200:
        response_data = response.json()
        result_text = response_data.get('data', '')
        return result_text

    return ""