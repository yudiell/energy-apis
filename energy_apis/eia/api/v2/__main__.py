"""
The main function is the entry point of the eia flow.

It parses the command line arguments that this particular api endpoint requires.
It requres an environment variale named EIA_API_KEY.
"""

import argparse


from python_postman.postman import Postman
from energy_apis.eia.api.v2 import flow


def main() -> None:
    """Define the main function for the EIA API."""
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--environment",
        help="The environment to run the model in.",
        type=str,
        required=True,
    )
    parser.add_argument(
        "--request_name",
        help="The EIA postman collection request name. [crude-oil-imports, electric-power-operational-data]. Refer to the Postman App.",
        type=str,
    )
    parser.add_argument(
        "--data_frequency",
        help="The EIA api dataset frequency.[monthly, yearly, etc]. Refer to eia documentation.",
        type=str,
    )
    parser.add_argument(
        "--verbose",
        help="The verbosity of the logs.",
        type=str,
    )

    args = parser.parse_args()
    kwargs: dict = dict(args._get_kwargs())

    postman = Postman()
    collections = postman._get_collections(dir="postman/collections")
    collection = postman._get_collection(name="EIA APIv2", collections=collections)
    flow.run(
        collection=collection,
        kwargs=kwargs,
    )


if __name__ == "__main__":
    main()
