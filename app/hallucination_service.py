import re


STOP_WORDS = {
    "the", "a", "an",
    "is", "are", "was", "were",
    "of", "to", "for",
    "and", "in", "on",
    "with", "by", "that",
    "this", "it", "has",
    "have", "had"
}


def clean_words(text):

    words = re.findall(
        r"\w+",
        text.lower()
    )

    return {
        word
        for word in words
        if word not in STOP_WORDS
    }


def detect_hallucination(
    answer: str,
    context: str
):

    answer_words = clean_words(
        answer
    )

    context_words = clean_words(
        context
    )

    unsupported_words = (
        answer_words -
        context_words
    )

    unsupported_count = len(
        unsupported_words
    )

    return {
        "unsupported_word_count":
            unsupported_count,

        "unsupported_words":
            list(unsupported_words),

        "possible_hallucination":
            unsupported_count > 10
    }