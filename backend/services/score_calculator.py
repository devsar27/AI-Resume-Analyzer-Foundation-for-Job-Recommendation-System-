def calculate_score(skills):
    score = len(skills) * 5
    return min(score, 100)
