import json

from pathlib2 import Path


def load_json_file(filepath: Path) -> dict:
    """Load json file."""
    with open(filepath, "r") as fp:
        json_file = json.load(fp)

    return json_file


data_list = load_json_file(
    "environments/elasticsearch/data/micromania/micromania_with_queries.json"
)

kb_id = 1
locale = "fr_fr"
bulk = []
for doc in data_list:
    del doc["_index"]
    del doc["_type"]
    del doc["_op_type"]
    del doc["_id"]

    question_id = doc["questionId"]
    bulk.append(
        {
            "index": {
                "_index": f"{locale}-knowledge_base-{kb_id}",
                "_id": question_id,
                "_type": "question",
            }
        }
    )
    bulk.append(doc)

list_of_dicts = [
    {"index": {"_index": "fr_fr-knowledge_base-0", "_id": 56, "_type": "question"}},
    {
        "questionId": 56,
        "lang": "fr",
        "title": "Puis-je annuler mon billet OUIGO et me faire rembourser ?",
    },
    {"index": {"_index": "fr_fr-knowledge_base-0", "_id": 49, "_type": "question"}},
    {
        "questionId": 49,
        "lang": "fr",
        "title": "aklsdjhfklkad ffkjhaskdjh kajsh fkfj hasdkjff akjsdh fkjahsdfkj ",
    },
    {"index": {"_index": "fr_fr-knowledge_base-0", "_id": 28, "_type": "question"}},
    {
        "questionId": 28,
        "lang": "fr",
        "title": "aklsdjhfklkad ffkjhaskdjh kajsh fkfj hasdkjff akjsdh fkjahsdfkj ",
    },
]
