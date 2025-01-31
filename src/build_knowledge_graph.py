import pandas as pd
import networkx as nx

def build_knowledge_graph(file_path):
    """ Go through the AI terms of each tweet to make a connection """
    df = pd.read_csv(file_path)
    G = nx.DiGraph()

    # Go through the AI terms of each tweet to make a connection
    for _, row in df.iterrows():
        terms = eval(row["ai_terms"])  # Read list format
        for i in range(len(terms)):
            for j in range(i + 1, len(terms)):
                G.add_edge(terms[i], terms[j], relation="related_to")

    return G

if __name__ == "__main__":
    terms_path = "data/ai_terms.csv"
    print("🔗 Building AI knowledge graph...")
    ai_graph = build_knowledge_graph(terms_path)

    # save the graph
    nx.write_gml(ai_graph, "data/ai_knowledge_graph.gml")
    print("✅ AI Knowledge Graph saved to 'data/ai_knowledge_graph.gml'.")