from flask import Blueprint, request, jsonify
from services.resume_parser import parse_resume
from services.skill_extractor import extract_skills
from services.score_calculator import calculate_score

resume_bp = Blueprint("resume", __name__)

@resume_bp.route("/analyze", methods=["POST"])
def analyze_resume():
    file = request.files["resume"]
    text = parse_resume(file)
    skills = extract_skills(text)
    score = calculate_score(skills)

    return jsonify({
        "skills": skills,
        "score": score
    })
