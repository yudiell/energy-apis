Getting data from the EIA crude-oil-imports endopoint.

Supported endpoints: 

- crude-oil-imports
- electric-power-operational-data 

Please see the defaults of the request. 

You can modify the collection to accomodate more endpoints. 

See the EIA API v2 documentation. 


Install poetry:

    pip install poetry

    poetry install

---

Run the project using a development environment variable.
   
    poetry run eia-api --environment dev --request crude-oil-imports
    poetry run eia-api --environment dev --request electric-power-operational-data
