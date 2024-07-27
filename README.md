Create a local virtual environment using:
  python -m venv .venv
  python3 -m venv .venv

---

On Windows:
`.venv\Scripts\activate`
Bash: 
`source .venv/bin/activate`

---

`pip install poetry`

`poetry config virtualenvs.path .venv`

---

poetry install

---

Run the project using a development environment variable.
   
    poetry run eia-api --environment dev --request crude-oil-imports
