import json

count = 0

with open("data/candidates.jsonl", "r", encoding="utf-8") as f:
    for line in f:
        count += 1

        if count <= 5:
            candidate = json.loads(line)

            print(
                candidate["candidate_id"],
                candidate["profile"]["current_title"],
                candidate["profile"]["years_of_experience"]
            )

print("Total Candidates:", count)