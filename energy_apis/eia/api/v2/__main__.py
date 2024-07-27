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
        "-e",
        "--environment",
        help="The environment to run the model in.",
        type=str,
        required=True,
    )
    parser.add_argument(
        "-r",
        "--request_name",
        help="The EIA postman collection request name. [crude-oil-imports, electric-power-operational-data]. Refer to the Postman App.",
        type=str,
    )
    parser.add_argument(
        "-f",
        "--dataset_frequency",
        help="The EIA api dataset frequency.[monthly, yearly, etc]. Refer to eia documentation.",
        type=str,
    )
    parser.add_argument(
        "-v",
        "--verbose",
        help="The verbosity of the logs.",
        type=str,
    )

    args = parser.parse_args()

    env = args.environment
    request_name = args.request_name
    dataset_frequency = args.dataset_frequency

    postman = Postman()
    collections = postman._get_collections(dir="postman/collections")
    collection = postman._get_collection(name="EIA APIv2", collections=collections)
    flow.run(
        collection=collection,
        env=env,
        request_name=request_name,
        dataset_frequency=dataset_frequency,
    )


if __name__ == "__main__":
    main()
