# Student Showcase
from pyscript import document

ASSESSMENTS = [
    {
        "title": "The Nickname Atlas",
        "description": (
            "Choose a European country and uncover the nickname "
            "attached to its story."
        ),
        "href": "SW1.html",
        "topics": {"Geography", "Dictionaries"},
    },
    {
        "title": "Element Checker",
        "description": (
            "Look up a non-metal by its chemical symbol "
            "and see its key details."
        ),
        "href": "skillstest.html",
        "topics": {"Science", "Dictionaries"},
    },
    {
        "title": "School Club Members",
        "description": (
            "Combine grade-level rosters and add a new name "
            "to the club community."
        ),
        "href": "PA2.html",
        "topics": {"Set operators"},
    },
]


def render_assessments():
    cards = []

    for assessment in ASSESSMENTS:
        topics = "".join(
            f'<span class="topic-label">{topic}</span>'
            for topic in sorted(assessment["topics"])
        )

        card = f"""
        <div class="col-md-6 col-lg-4">
            <a
                class="project-card-link"
                href="{assessment["href"]}"
                aria-label="Open {assessment["title"]}"
            >
                <article class="project-card">
                    <h3>{assessment["title"]}</h3>
                    <p>{assessment["description"]}</p>
                    <div>{topics}</div>
                    <span class="card-link">Open assessment</span>
                </article>
            </a>
        </div>
        """
        cards.append(card)

    document.querySelector("#assessment-list").innerHTML = "".join(cards)


render_assessments()