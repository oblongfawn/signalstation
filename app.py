from flask import Flask, render_template, request

app = Flask(__name__)

QUESTION_SETS = {
    "overlooked": {
        "Outside":    "What is an outsider's POV or experience?",
        "Other Side": "What is the inverse or contradictory tension?",
        "Dark Side":  "What is the malicious or distressing angle?",
        "Back Side":  "What is the devious or stigmatized twist?",
        "Quiet Side": "What is not being talked about?",
        "Long Side":  "What are the long-term implications or effects?",
        "Inside":     "What is the internal or personal impact?",
        "Old Side":   "What are the historical roots or deeper origins?"
    },
    "standard": {
        "Surprising":    "What could be considered surprising in the insights?",
        "Illumination":  "What do the insights illuminate that is different from today's norm?",
        "Overlooked":    "What ideas might these insights showcase that have been overlooked?",
        "Patterns":      "Do the insights showcase a new or unexpected pattern or challenge existing paradigms? If so, how?",
        "Cultural":      "Is there a cultural or social aspect that we should be paying attention to?",
        "Subversive":    "How are the signals subversive? What disruption does it create or imply?",
        "Implications":  "What are potential further implications from the insights?",
        "Provenance":    "What is the provenance of these insights?",
        "Delayed":       "Are any of the insights delayed? What does it showcase that should already be happening?"
    }
}

SUBMIT_LINK = "https://your-submission-link.com"

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        set_choice = request.form["question_set"]
        questions = QUESTION_SETS[set_choice]
        answers = {k: request.form.get(k, "") for k in questions}
        artefact1 = request.form.get("artefact1", "")
        artefact2 = request.form.get("artefact2", "")
        return render_template(
            "results.html",
            submit_link=SUBMIT_LINK,
            questions=questions,
            answers=answers,
            artefacts=[artefact1, artefact2]
        )
    return render_template("index.html", submit_link=SUBMIT_LINK)

if __name__ == "__main__":
    app.run(debug=True)
