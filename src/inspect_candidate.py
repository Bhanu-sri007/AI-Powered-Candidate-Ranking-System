import json

with open("data/candidates.jsonl", "r", encoding="utf-8") as f:

    for line in f:

        candidate = json.loads(line)

        if candidate["candidate_id"] == "CAND_0070398":

            print(candidate["candidate_id"])
            print(candidate["profile"]["current_title"])
            print(candidate["career_history"][0]["description"])

            break