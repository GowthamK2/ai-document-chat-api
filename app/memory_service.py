chat_history = []


def add_to_memory(
    question,
    answer
):

    chat_history.append(
        {
            "question": question,
            "answer": answer
        }
    )

    if len(chat_history) > 50:

        chat_history.pop(0)


def get_memory():

    return chat_history[-5:]