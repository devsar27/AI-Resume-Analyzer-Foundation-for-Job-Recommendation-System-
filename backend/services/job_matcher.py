def calculate_match(resume_skills, job_description):
    job_description = job_description.lower()

    matched_skills = []
    missing_skills = []

    for skill in resume_skills:
        if skill.lower() in job_description:
            matched_skills.append(skill)

    # Find required skills from JD
    for skill in resume_skills:
        if skill.lower() not in job_description:
            missing_skills.append(skill)

    if len(resume_skills) == 0:
        match_percent = 0
    else:
        match_percent = int((len(matched_skills) / len(resume_skills)) * 100)

    return {
        "match_percentage": match_percent,
        "matched_skills": matched_skills,
        "missing_skills": missing_skills
    }
