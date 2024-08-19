from logging import Logger

from python_postman.http import PreparedRequest
from python_postman.collection import Collection
from retry import retry

logger = Logger(name="Message: ")


@retry(tries=3, delay=5, backoff=3, logger=logger)
def get_data(collection: Collection, **kwargs: dict) -> None:
    """Get the data."""
    name = kwargs.get("request_name")
    collection_request = collection.get_request(name=name)
    prepared_request: PreparedRequest = PreparedRequest(request=collection_request)
    prepared_request.send


get_data(
    collection=Collection(
        collection_file="postman/collections/EIA APIv2.postman_collection.json"
    ),
    request_name="crude-oil-imports",
)
