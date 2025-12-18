import logging, random

class SensitiveInfoFilter(logging.Filter):
    def filter(self, record):
        if "bibli" in record.msg:
            return False
        return True


livres_logger = logging.getLogger("livres")
transactions_logger = logging.getLogger("transactions")

livres_logger.setLevel(logging.WARNING)
transactions_logger.setLevel(logging.WARNING)

livres_stream_handler = logging.StreamHandler()
livres_logger.addHandler(livres_stream_handler)
livres_logger.addFilter(SensitiveInfoFilter())

livres_formatter = logging.Formatter("%(asctime)s-%(module)s-%(funcName)s-%(levelname)s-%(message)s", datefmt="(%d/%Y-%I:%M)")
livres_stream_handler.setFormatter(livres_formatter)

transactions_stream_handler = logging.StreamHandler()
transaction_formatter = logging.Formatter("%(name)s-%(levelname)s-%(message)s")
transactions_stream_handler.setFormatter(transaction_formatter)
transactions_logger.addHandler(transactions_stream_handler)

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

