import logging, random, os, yaml
from logging.config import dictConfig
class SensitiveInfoFilter(logging.Filter):
    def filter(self, record):
        if "bibli" in record.msg:
            return False
        return True

config_log = os.getenv("CONFIG")
print(config_log)
if config_log == "production":
    config_path_log = "config_production.yaml"
else:
    config_path_log = "config_dev.yaml"


with open(os.path.join(os.path.dirname(__file__), config_path_log), 'r') as f:
    config = yaml.safe_load(f.read())
    dictConfig(config)

livres_logger = logging.getLogger("livres_logger")
transactions_logger = logging.getLogger("transactions_logger")

bibliotheque = {}

def add_book(book_id):
    if random.random() < 0.9:
        bibliotheque[book_id] = True
        livres_logger.info(f"{book_id} added to bibli.")
    else:
        livres_logger.warning(f"{book_id} not added to bibli.")

def process_transaction(user_id, book_id):
    if book_id in bibliotheque:
        transactions_logger.info(f"{user_id} buys {book_id}")
        del bibliotheque[book_id]
    else:
        transactions_logger.warning(f"{user_id} can't buy {book_id}")

livres = ["Livre"+str(i) for i in range(0, 20)]
User = ["Paul", "Dupont", "Georges"]

for livre in livres:
    add_book(livre)

for index, livre in enumerate(livres):
    user = User[index % len(User)]
    process_transaction(user, livre)

