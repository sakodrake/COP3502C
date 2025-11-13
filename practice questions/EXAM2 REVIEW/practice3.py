def classify_student_scores(scores):
    if scores == {}:
        return {}
    name, score = scores.popitem()
    rest = classify_student_scores(scores)
    if score >= 90:
        rest[name] = 'Excellent'
    elif 89 >= score >= 75:
        rest[name] = "Good"
    else:
        rest[name] = "Needs improvement"
    return rest 