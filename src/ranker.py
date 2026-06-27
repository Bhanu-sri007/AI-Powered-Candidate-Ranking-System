
import json
import csv

from scoring import (
    title_score,
    experience_score,
    skill_score,
    behavioral_score,
    penalty_score,
    career_history_score,
    recruitability_score
)

scores = []

with open("data/candidates.jsonl", "r", encoding="utf-8") as f:

    for line in f:

        candidate = json.loads(line)

        title = candidate["profile"]["current_title"]
        exp = candidate["profile"]["years_of_experience"]
        skills = candidate["skills"]
        signals = candidate["redrob_signals"]
        history = candidate["career_history"]

        title_points = title_score(title)
        experience_points = experience_score(exp)
        skill_points = skill_score(skills)
        career_points = career_history_score(history)
        behavior_points = behavioral_score(signals)
        recruitability_points = recruitability_score(signals)
        penalty_points = penalty_score(history)

        score = (
            title_points
            + experience_points
            + skill_points
            + career_points
            + behavior_points
            + recruitability_points
            - penalty_points
        )

        if score >= 100:
            status = "Strong Match"

        elif score >= 80:
            status = "Potential Match"

        elif score >= 60:
            status = "Weak Match"

        else:
            status = "Not Recommended"
        confidence = min(score, 100)

        scores.append(
    {
        "candidate_id": candidate["candidate_id"],
        "title": title,
        "score": score,
        "status": status,
        "confidence": confidence,
        "title_score": title_points,
        "experience_score": experience_points,
        "skill_score": skill_points,
        "career_score": career_points,
        "behavior_score": behavior_points,
        "recruitability_score": recruitability_points,
        "penalty_score": penalty_points,
        "experience": exp,
        "response_rate": signals["recruiter_response_rate"],
        "skills": [skill["name"] for skill in skills],
        "description": history[0]["description"]
    }
    
        )


scores.sort(
    key=lambda x: x["score"],
    reverse=True
)
strong_matches = 0
potential_matches = 0
weak_matches = 0
not_recommended = 0

for candidate in scores:

    if candidate["status"] == "Strong Match":
        strong_matches += 1

    elif candidate["status"] == "Potential Match":
        potential_matches += 1

    elif candidate["status"] == "Weak Match":
        weak_matches += 1

    else:
        not_recommended += 1
best_score = scores[0]["score"]

if best_score < 80:
    print("\nNo Strong Candidate Found")
else:
    print("\nStrong Candidates Available")
print("\n===== Recruiter Dashboard =====")

print(f"Total Candidates: {len(scores)}")
print(f"Strong Matches: {strong_matches}")
print(f"Potential Matches: {potential_matches}")
print(f"Weak Matches: {weak_matches}")
print(f"Not Recommended: {not_recommended}")


print("\n===== Candidate Comparison =====")

candidate_a = scores[0]
candidate_b = scores[1]

print(f"Candidate A: {candidate_a['candidate_id']}")
print(f"Score: {candidate_a['score']}")

print()

print(f"Candidate B: {candidate_b['candidate_id']}")
print(f"Score: {candidate_b['score']}")

print("\nTitle Score:")
print(
    f"{candidate_a['title_score']} vs "
    f"{candidate_b['title_score']}"
)

print("\nCareer Score:")
print(
    f"{candidate_a['career_score']} vs "
    f"{candidate_b['career_score']}"
)

print("\nBehavior Score:")
print(
    f"{candidate_a['behavior_score']} vs "
    f"{candidate_b['behavior_score']}"
)

print("\nRecruitability Score:")
print(
    f"{candidate_a['recruitability_score']} vs "
    f"{candidate_b['recruitability_score']}"
)

print("\nWinner:")
print(candidate_a["candidate_id"])

print("\n===== Best Candidate Breakdown =====")

best = scores[0]

print(f"Candidate ID: {best['candidate_id']}")
print(f"Final Score: {best['score']}")
print(f"Status: {best['status']}")
print(f"Confidence: {best['confidence']}%")

print("\nScore Breakdown:")
print(f"Title Score: {best['title_score']}")
print(f"Experience Score: {best['experience_score']}")
print(f"Skill Score: {best['skill_score']}")
print(f"Career Score: {best['career_score']}")
print(f"Behavior Score: {best['behavior_score']}")
print(f"Recruitability Score: {best['recruitability_score']}")
print(f"Penalty Score: {best['penalty_score']}")
print("\n===== Backup Candidate Pool =====")

for candidate in scores[10:20]:

    print(
        f"{candidate['candidate_id']} | "
        f"Score: {candidate['score']} | "
        f"{candidate['status']}"
    )
print("\n===== Missing Skills Analysis =====")

required_skills = [
    "Pinecone",
    "FAISS",
    "BM25",
    "Embeddings",
    "Ranking",
    "Retrieval"
]

candidate_skills = best["skills"]

missing = []

for skill in required_skills:

    found = False

    for candidate_skill in candidate_skills:

        if skill.lower() in candidate_skill.lower():
            found = True
            break

    if not found:
        missing.append(skill)

print("Missing Skills:")

for skill in missing:
    print(f"- {skill}")
print("\n===== AI Recruiter Recommendation =====")

if best["score"] >= 110:

    print(
        "Highly Recommended: Strong experience in "
        "retrieval, ranking, recommendation systems "
        "and production ML deployments."
    )

elif best["score"] >= 90:

    print(
        "Recommended: Good fit for the role with "
        "minor skill gaps."
    )

else:

    print(
        "Review Required: Candidate may need "
        "additional evaluation."
    )
print("\n===== Top 10 Candidates =====")

for row in scores[:10]:
    print(row)

with open(
    "output/submission.csv",
    "w",
    newline="",
    encoding="utf-8"
) as csvfile:

    writer = csv.writer(csvfile)

    writer.writerow(
        [
            "candidate_id",
            "rank",
            "score",
            "reasoning"
        ]
    )

    for rank, candidate in enumerate(
        scores[:100],
        start=1
    ):

        response_rate = candidate["response_rate"]

        exp = candidate["experience"]
        title = candidate["title"]
        description = candidate["description"].lower()
        required_skills = [
            "ranking",
            "retrieval",
            "embedding",
            "pinecone",
            "faiss",
            "bm25"
        ]
        missing_skills = []

        for skill in required_skills:

            if skill not in description:
                missing_skills.append(skill)
        reasons = []        

        

        if "pinecone" in description:
            reasons.append("Pinecone")

        if "ranking" in description:
            reasons.append("Ranking Systems")

        if "embedding" in description:
            reasons.append("Embeddings")

        if "recommendation" in description:
            reasons.append("Recommendation Systems")

        if len(reasons) == 0:
            reasons.append("Production ML Systems")

        reasoning = (
            f"{title} with {exp:.1f} years experience. "
            f"Experience in {', '.join(reasons)}. "
            f"Recruiter response rate: {response_rate:.2f}."
        )

        writer.writerow(
            [
                candidate["candidate_id"],
                rank,
                candidate["score"],
                reasoning
            ]
        )


print("submission.csv generated")

