from flask import Blueprint, request, jsonify
from services.resume_parser import parse_resume
from services.skill_extractor import extract_skills
from services.score_calculator import calculate_score
from services.job_matcher import calculate_match


resume_bp = Blueprint("resume", __name__)
@resume_bp.route("/analyze", methods=["POST"])
def analyze_resume():
    file = request.files["resume"]
    job_desc = request.form.get("job_description", "")

    text = parse_resume(file)
    skills = extract_skills(text)

    match_result = calculate_match(skills, job_desc)

    return jsonify({
        "skills": skills,
        "match_percentage": match_result["match_percentage"],
        "matched_skills": match_result["matched_skills"],
        "missing_skills": match_result["missing_skills"]
    })
