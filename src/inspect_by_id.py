

import json

target_ids = {
    "CAND_0088025",
    "CAND_0081846",
    "CAND_0071974"
}

with open("data/candidates.jsonl", "r", encoding="utf-8") as f:

    for line in f:

        candidate = json.loads(line)

        if candidate["candidate_id"] in target_ids:

            print("\n" + "="*60)
            print("ID:", candidate["candidate_id"])
            print("Title:", candidate["profile"]["current_title"])
            print("Experience:", candidate["profile"]["years_of_experience"])
            print("Response Rate:",
                  candidate["redrob_signals"]["recruiter_response_rate"])

            print("\nSkills:")
            for skill in candidate["skills"][:10]:
                print("-", skill["name"])

            print("\nCareer Description:")
            print(candidate["career_history"][0]["description"])