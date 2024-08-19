"""Module for handling requests and responses."""

import json
import jmespath
from logging import Logger

from python_postman.collection import Collection
from python_postman.request import Request
from retry import retry

logger = Logger(name="Message: ")


@retry(tries=3, delay=5, backoff=3, logger=logger)
def get_data(collection: Collection, **kwargs: dict) -> None:
    """Get the data."""
    name = kwargs.get("request_name")
    request: Request = collection.get_request(name=name)
    request.send(kwargs=kwargs)
    
    return request.response


def run(
    collection: Collection,
    kwargs: dict,
):
    params = {
        "recordOffset": 0,
        "sortColumn": "period",
        "sortDirection": "asc",
        "dataFrequency": "monthly",
    }
    kwargs.update(params)

    data = get_data(collection=collection, **kwargs)

#     # ---------------------------------------------------------------------------------------------------------------------

    import pandas as pd

    records: list[dict] = jmespath.search(
        expression="response.data", data=json.loads(data.content)
    )
    df = pd.DataFrame(data=records)
    print(df.head())
