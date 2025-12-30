import json

with open("data/skill_keywords.json") as f:
    SKILLS = json.load(f)

def extract_skills(text):
    found = []
    text = text.lower()
    for skill in SKILLS:
        if skill.lower() in text:
            found.append(skill)
    return found
