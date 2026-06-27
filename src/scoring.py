def title_score(title):

    title = title.lower()

    if "senior machine learning engineer" in title:
        return 25

    if "ml engineer" in title:
        return 24

    if "machine learning engineer" in title:
        return 24

    if "ai engineer" in title:
        return 24

    if "data scientist" in title:
        return 20

    if "backend engineer" in title:
        return 12

    return 0


def experience_score(exp):

    if 6 <= exp <= 8:
        return 15

    if 5 <= exp <= 9:
        return 12

    if 3 <= exp < 5:
        return 8

    return 2


def skill_score(skills):

    important_skills = [
        "python",
        "nlp",
        "embeddings",
        "retrieval",
        "ranking",
        "vector",
        "milvus",
        "faiss",
        "pinecone",
        "elasticsearch",
        "bm25",
        "llm",
        "lora"
    ]

    score = 0

    for skill in skills:

        name = skill["name"].lower()

        for target in important_skills:

            if target in name:
                score += 2

    return min(score, 20)


def career_history_score(history):

    keywords = {
        "semantic search": 8,
        "retrieval": 8,
        "ranking": 8,
        "re-ranking": 10,
        "recommendation": 8,
        "embeddings": 8,
        "faiss": 10,
        "pinecone": 10,
        "milvus": 10,
        "weaviate": 8,
        "qdrant": 8,
        "bm25": 10,
        "elasticsearch": 8,
        "sentence-transformers": 10,
        "ndcg": 12,
        "mrr": 12,
        "a/b testing": 12
    }

    score = 0

    for job in history:

        description = job["description"].lower()

        for keyword, weight in keywords.items():

            if keyword in description:
                score += weight

    return min(score, 25)


def behavioral_score(signals):

    score = 0

    if signals["open_to_work_flag"]:
        score += 5

    if signals["recruiter_response_rate"] > 0.70:
        score += 5

    if signals["interview_completion_rate"] > 0.80:
        score += 5

    if signals["github_activity_score"] > 70:
        score += 5

    if signals["saved_by_recruiters_30d"] > 10:
        score += 5

    return score


def penalty_score(history):

    negative_keywords = [
        "computer vision",
        "image moderation",
        "object detection",
        "image classification",
        "robotics"
    ]

    penalty = 0

    for job in history:

        description = job["description"].lower()

        for keyword in negative_keywords:

            if keyword in description:
                penalty += 10

    return penalty
def recruitability_score(signals):

    score = 0

    if signals["recruiter_response_rate"] > 0.70:
        score += 5

    if signals["interview_completion_rate"] > 0.80:
        score += 5

    if signals["offer_acceptance_rate"] > 0.50:
        score += 5

    if signals["notice_period_days"] <= 30:
        score += 5

    return score