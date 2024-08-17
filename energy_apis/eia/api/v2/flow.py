"""Module for handling requests and responses."""

import json
import jmespath
from logging import Logger

from python_postman.modules.http import PreparedRequest
from python_postman.postman import Collection
from retry import retry

logger = Logger(name="Message: ")


@retry(tries=3, delay=5, backoff=3, logger=logger)
def get_data(collection: Collection, **kwargs: dict) -> None:
    """Get the data."""
    name = kwargs.get("request_name")
    collection_request = collection.get_request(name=name)
    print(collection_request.name)
    prepared_request: PreparedRequest = PreparedRequest(request=collection_request)

    # response = prepared_request.send
    # response_content = response.content
    # return response_content


# def run(
#     collection: Collection,
#     kwargs: dict,
# ):
#     params = {
#         "recordOffset": 0,
#         "sortColumn": "period",
#         "sortDirection": "asc",
#     }
#     kwargs.update(params)

#     data = get_data(collection=collection, **kwargs)

#     # ---------------------------------------------------------------------------------------------------------------------

#     import pandas as pd

#     records: list[dict] = jmespath.search(
#         expression="response.data", data=json.loads(data)
#     )
#     df = pd.DataFrame(data=records)
#     print(df.head())
