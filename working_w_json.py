import json
from pathlib import Path


### Making a JSON file ###
# movies = [
#     {"id": 1, "title": "Terminator", "year": 1984},
#     {"id": 2, "title": "Blade Runner", "year": 1982}
# ]

# data = json.dumps(movies)
# Path("movies.json").write_text(data)

data = Path("movies.json").read_text()
movies = json.loads(data)
print(movies)
