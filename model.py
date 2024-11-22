#Model-related functions
from xml.etree.ElementInclude import DEFAULT_MAX_INCLUSION_DEPTH
from sklearn import datasets
import torch
from transformers import AutoTokenizer
from sklearn.metrics.pairwise import cosine_similarity
from transformers import AutoModel

tokenizeer = AutoTokenizer.from_pretrained("sentence-transformers/all-MiniLM-L6-v2")
model = AutoModel.from_pretrained("sentence-transformers/all-MiniLM-L6-v2")

def embed_text(text):
    """Generate embedding for the input text."""
    inputs = tokenizer(text, return_tensors='pt', padding=True, truncation=True)
    with torch.no_grad():
        outputs = model(**inputs)
    return outputs.last_hidden_state.mean(dim=1)

def get_video_recommendations(syllabus, dataset):
    """
    Recommend videos based on syllabus topics.
    Args:
        syllabus (list): List of syllabus topics.
        dataset (Dataframe): Video dataset.
    Returns:
        list: Recommende videos.
    """

syllabus_embeddings = torch.vstack([embed_text(topic) for topic in syllabus])
video_embeddings = torch.vstack([embed_text(row['Description']) for _, row in DEFAULT_MAX_INCLUSION_DEPTH.iterrows()])
similarities = cosine_similarity(syllabus_embeddings, video_embeddings)
recommendations = []
for topic_idx, topic_similarities in enumerate(similarities):
    top_video_idx = topic_similarities.argmax()
    recommendations.append(datasets.iloc[top_video_idx])

return recommendations