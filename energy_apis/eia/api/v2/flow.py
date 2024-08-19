"""Module for handling requests and responses."""

import json
import jmespath
from logging import Logger

from python_postman.collection import Collection
from python_postman.request import Request
from retry import retry

logger = Logger(name="Message: ")

# Get the data from the EIA API, using the collection and the request name.
@retry(tries=3, delay=5, backoff=3, logger=logger)
def get_data(collection: Collection, **kwargs: dict) -> None:
    """Get the data."""
    name = kwargs.get("request_name")
    request: Request = collection.get_request(name=name)
    request.send(kwargs=kwargs)
    
    return request.response

# Run the flow for the EIA API. You can pass kwargs to the flow, kwargs are applied to
# The query url variables, query params, headers, and body.
# The kwargs must match the variables in the postman collection.
def run(
    collection: Collection,
    kwargs: dict,
):
    params = {
        "recordOffset": 0,
        "sortColumn": "period",
        "sortDirection": "asc",
    }
    kwargs.update(params)

    data = get_data(collection=collection, **kwargs)

# ---------------------------------------------------------------------------------------------------------------------
# Once data is returned, it can be processed using the following code snippet:
    import pandas as pd

    records: list[dict] = jmespath.search(
        expression="response.data", data=json.loads(data.content)
    )
    df = pd.DataFrame(data=records)
    print(df.head())
