# import asyncio

import nltk
from newspaper import Article

from app.models.tortoise import TextSummary


async def generate_summary(summary_id: int, url: str) -> None:
    article = Article(url)
    article.download()
    article.parse()

    try:
        nltk.data.find("tokenizers/punkt")
    except LookupError:
        nltk.download("punkt")
    finally:
        article.nlp()

    summary = article.summary

    # await asyncio.sleep(10)  # To test, add asyncio.sleep to generate_summary
    # # So the summary is added after the response was already sent back to the user
    await TextSummary.filter(id=summary_id).update(summary=summary)
