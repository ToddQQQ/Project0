import networkx as nx

def build_custom_knowledge_graph():
    """ Create a knowledge graph that includes AI-related topics """
    kg = nx.DiGraph()


    kg.add_edge("ai", "machine learning", relation="related_to")
    kg.add_edge("ai", "deep learning", relation="related_to")
    kg.add_edge("ai", "neural networks", relation="related_to")
    kg.add_edge("chatgpt", "OpenAI", relation="developed_by")
    kg.add_edge("chatgpt", "language model", relation="type_of")
    kg.add_edge("machine learning", "data science", relation="related_to")
    kg.add_edge("neural networks", "backpropagation", relation="uses")
    kg.add_edge("deep learning", "large datasets", relation="requires")
    kg.add_edge("deep learning", "gpu", relation="optimized_by")
    

    kg.add_edge("OpenAI", "GPT-4", relation="developed")
    kg.add_edge("GPT-4", "transformer", relation="architecture")
    kg.add_edge("transformer", "self-attention", relation="core_concept")
    kg.add_edge("AI", "automation", relation="application")
    kg.add_edge("automation", "job market", relation="impacts")

    return kg

def query_custom_knowledge_graph(kg, keyword):
    """ Queries the knowledge graph and returns the entities associated with the keywords """
    if keyword in kg:
        related = list(kg.neighbors(keyword))
        return related if related else ["No related information found."]
    return ["No related information found."]

if __name__ == "__main__":
    kg = build_custom_knowledge_graph()
    test_query = "chatgpt"
    print(f"🔎 Query '{test_query}':", query_custom_knowledge_graph(kg, test_query))
