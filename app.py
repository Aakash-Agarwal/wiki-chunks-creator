import xml.etree.ElementTree as ET
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

vectorizer = None
parsed_xml = None

# Step 1: Parse XML file
def parse_xml(xml_file):
    tree = ET.parse(xml_file)
    root = tree.getroot()
    texts = [element.text for element in root.iter('text')]
    return texts


# Step 2: Preprocess and Vectorize Text
def vectorize_text(texts):
    # You might need more advanced preprocessing based on your data
    vectors = vectorizer.fit_transform(texts)
    return vectors


# Step 3: Semantic Search
def semantic_search(query, vectors, texts):
    query_vector = vectorizer.transform([query])
    similarity_scores = cosine_similarity(query_vector, vectors).flatten()

    # Get indices of top N most similar documents
    top_indices = similarity_scores.argsort()[:-N - 1:-1]

    # Return the most relevant documents
    results = [(texts[i], similarity_scores[i]) for i in top_indices]
    return results


def setup():
    global vectorizer, parsed_xml
    vectorizer = TfidfVectorizer()
    parsed_xml = parse_xml('test.xml')


# Step 4: Example Usage
if __name__ == "__main__":
    setup()
    xml_file = 'test.xml'
    N = 5  # Number of top results to retrieve
    query = 'Wie kann ich einen Job abonnieren?'

    # Step 1: Parse XML
    texts = parse_xml(xml_file)

    # Step 2: Vectorize Text
    vectors = vectorize_text(texts)

    # Step 3: Perform Semantic Search
    results = semantic_search(query, vectors, texts)

    # Step 4: Display Results
    print(f"Top {N} results for the query '{query}':")
    for result, score in results:
        print(f"Score: {score:.4f}, Text: {result}")
