import json

count = 0

with open("data/candidates.jsonl", "r", encoding="utf-8") as f:

    for line in f:

        candidate = json.loads(line)

        title = candidate["profile"]["current_title"]

        if any(x in title.lower() for x in [
            "ml engineer",
            "machine learning",
            "ai engineer",
            "data scientist"
        ]):

            count += 1

            print("\n" + "=" * 60)
            print("Candidate ID:", candidate["candidate_id"])
            print("Title:", title)
            print("Experience:", candidate["profile"]["years_of_experience"])

            print("\nSkills:")
            for skill in candidate["skills"][:10]:
                print("-", skill["name"])

            print("\nCareer Description:")
            print(candidate["career_history"][0]["description"])

            if count == 10:
                break