from PyPDF2 import PdfReader


def extract_text_from_pdf(
    file_path: str
):

    try:

        reader = PdfReader(
            file_path
        )

        text = ""

        for page in reader.pages:

            text += (
                page.extract_text()
                or ""
            )

            text += "\n"

        text = " ".join(
            text.split()
        )

        if not text.strip():

            raise ValueError(
                "No extractable text found."
            )

        return text

    except Exception as e:

        raise Exception(
            f"PDF Read Error: {e}"
        )