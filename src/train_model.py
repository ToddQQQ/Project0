from gpt4all import GPT4All
import os
import sys
import re
from src.knowledge_graph import build_custom_knowledge_graph, query_custom_knowledge_graph

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

#   GPT4Allmodel
MODEL_PATH = r"C:\Users\Todd\AppData\Local\nomic.ai\GPT4All\gpt4all-falcon-newbpe-q4_0.gguf"
gpt4all_model = GPT4All(MODEL_PATH, device="cpu")

#  load knowledge graph
kg = build_custom_knowledge_graph()

def extract_keywords(text):
    """Extract possible keywords from user input"""
    words = re.findall(r'\b\w+\b', text.lower())  # extract words
    return words

def generate_reply(input_text):
    """ Use GPT4All to generate Twitter-style replies combined with knowledge graph information """
    try:
        # ✅ extract keywords and generate knowledge graph
        keywords = extract_keywords(input_text)
        related_knowledge = []

        for word in keywords:
            results = query_custom_knowledge_graph(kg, word)
            if results and results[0] != "No related information found.":
                related_knowledge.extend(results)

        # ✅ generate Prompt
        if related_knowledge:
            knowledge_text = f"AI facts: {', '.join(set(related_knowledge))} are connected to this topic. "
            humor_text = "Give a snarky, funny Twitter-style reply! Keep it short and witty. 🤖🔥"
        else:
            knowledge_text = ""
            humor_text = "Reply like a funny Twitter user. Be witty and a little sarcastic. 😏"

        prompt = f"{knowledge_text}{humor_text} Tweet: {input_text}"
        response = gpt4all_model.generate(prompt, max_tokens=50)

        return response
    except Exception as e:
        print(f"⚠️ GPT4All Error: {e}")
        return "Hmm, that's a good question! What do you think? 🤔"

if __name__ == "__main__":
    # ✅ test
    test_input = "What do you think about ChatGPT?"
    print("TwiUser:", generate_reply(test_input))
