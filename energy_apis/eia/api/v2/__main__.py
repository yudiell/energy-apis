"""
The main function is the entry point of the eia flow.

It parses the command line arguments that this particular api endpoint requires.
It requres an environment variale named EIA_API_KEY.
"""
from python_postman.collection import Collection
from python_postman.utils.cli import Cli
from energy_apis.eia.api.v2 import flow


def main() -> None:
    """Define the main function for the EIA API."""
    # Cli allows you to pass any number of keyword arguments to the flow via the --extra_args flag.
    # Eg: poetry run eia-api --environment dev --request crude-oil-imports --extra_args dataFrequency=monthly
    cli = Cli()
    kwargs = cli.parse_arguments()


    collection = Collection(
        collection_file="postman/collections/EIA APIv2.postman_collection.json"
    )
    flow.run(
        collection=collection,
        kwargs=kwargs,
    )

# ---------------------------------------------------------------------------------------------------------------------
# You can add your own custom keyword arguments implementation.
    # import argparse

    # parser = argparse.ArgumentParser()
    # parser.add_argument(
    #     "--environment",
    #     help="The environment to run the model in.",
    #     type=str,
    #     required=True,
    # )
    # parser.add_argument(
    #     "--request_name",
    #     help="The EIA postman collection request name. [crude-oil-imports, electric-power-operational-data]. Refer to the Postman App.",
    #     type=str,
    # )
    # parser.add_argument(
    #     "--data_frequency",
    #     help="The EIA api dataset frequency.[monthly, yearly, etc]. Refer to eia documentation.",
    #     type=str,
    # )
    # parser.add_argument(
    #     "--verbose",
    #     help="The verbosity of the logs.",
    #     type=str,
    # )

    # args = parser.parse_args()
    # kwargs: dict = dict(args._get_kwargs())

if __name__ == "__main__":
    main()
