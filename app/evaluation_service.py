def evaluate_response(
    question,
    context,
    answer
):

    context_length = len(context)

    answer_length = len(answer)

    return {
        "question_length":
            len(question),

        "context_length":
            context_length,

        "answer_length":
            answer_length,

        "context_available":
            context_length > 100
    }


def confidence_score(
    context_length,
    hallucination_count
):

    score = 100

    if context_length < 200:
        score -= 30

    elif context_length < 500:
        score -= 15

    score -= min(
        hallucination_count,
        70
    )

    return max(
        min(score, 100),
        0
    )