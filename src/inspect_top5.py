import json

top_ids = {
    "CAND_0088025",
    "CAND_0071974",
    "CAND_0002025",
    "CAND_0037566",
    "CAND_0039383"
}

with open("data/candidates.jsonl", "r", encoding="utf-8") as f:

    for line in f:

        candidate = json.loads(line)

        if candidate["candidate_id"] in top_ids:

            print("\n" + "=" * 60)
            print("ID:", candidate["candidate_id"])
            print("Title:", candidate["profile"]["current_title"])
            print("Experience:", candidate["profile"]["years_of_experience"])

            print("\nCareer Description:")
            print(candidate["career_history"][0]["description"])