"""Module for handling requests and responses."""

import json
import jmespath
from logging import Logger

from python_postman.modules.http import Request
from python_postman.postman import Postman, Collection
from retry import retry

logger = Logger(name="Message: ")


@retry(tries=3, delay=5, backoff=3, logger=logger)
def get_data(postman: Postman = Postman(), **kwargs: dict) -> None:
    """Get the data."""
    collection: Collection = kwargs.get("collection")
    requests: Request = postman._get_requests(collection=collection)
    name: str = kwargs.get("request_name")
    request = postman._get_request(name=name, requests=requests)
    prepared_request: Request = Request(request=request)
    prepared_request.set_params(kwargs)
    response = prepared_request.send
    response_content = response.content
    return response_content


def run(
    collection: Collection,
    env: str,
    request_name: str,
    dataset_frequency: str = "monthly",
):
    data = get_data(
        collection=collection,
        env=env,
        request_name=request_name,
        frequency=dataset_frequency,
        recordOffset="0",
        sortColumn="period",
        sortDirection="asc",
    )

    import pandas as pd

    records = jmespath.search("response.data", json.loads(data))

    df = pd.DataFrame(records)
    print(df.head())
    # END
