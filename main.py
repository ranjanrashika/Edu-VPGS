#main script
import pandas as pd
from model import get_video_recommendations

def main():
    dataset = pd.read_csv('videos.csv')

    syllabus = [
        "Introduction to artificial intelligence",
        "Neural networs",
        "Deep Learning fundamentals",
        " Machine Learning",
        " Natural Language Processing",
        " Cloud Computing",
    ]
    recommendations = get_video_recommendations(syllabus, dataset)
    print("Recommended Playlist:")
    for idx, video in enumerate(recommendations, 1):
        print(f"{idx}. {video['Title']} ({video['Video ID']})")

if __name__ == "__main__":
    main()