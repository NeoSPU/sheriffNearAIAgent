import rag_helper
import black_list_helper

def contains_blacklist_words(message, ban_words):
    black_list = black_list_helper.get_blacklist_from_string(ban_words)
    return any(word in message for word in black_list)

def get_last_user_message(env):
    for message in reversed(env.list_messages()):
        if message.get("role") == "user":
            return message

    return None

def handle_user_message(env, prompt, ban_words, rag_url, rag_secret, model_name='llama-v3-70b-instruct'):
    user_message = get_last_user_message(env)

    if contains_blacklist_words(user_message['content'], ban_words) or user_message['content']=="":
        env.add_message("agent", "Your message should be specific and related to checking vvulnerabilities and support security and realibility of Near Blockchain. Please try again.")
    else:
        context = rag_helper.find_relevant_context(user_message['content'], rag_url, rag_secret)
      
        prompt['content'] += '\n '

        if context:
            prompt['content'] += f"Relevant context: {context}\n\n"

        prompt['content'] += f"User question: {user_message}\n\n"

        messages = [
            prompt,
            user_message
        ]

        result = env.completion(model_name, messages)

        env.add_message("agent", result)

        env.request_user_input()
