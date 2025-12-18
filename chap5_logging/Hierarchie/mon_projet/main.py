import logging
from module_a.sous_module_a1 import fonction_a1
from module_a.sous_module_a2 import fonction_a2
from module_b.sous_module_b1 import fonction_b1
from module_propagation.sous_module_propagation import fonction_sous_module_propagation
from module_surcharge.sous_module_surcharge import fonction_sous_module_surcharge

logger = logging.getLogger()
logger.setLevel(logging.DEBUG)
handler = logging.StreamHandler()
logger.addHandler(handler)


def main():
    logger.info("Démarrage de l'application.")
    #fonction_a1()
    #fonction_a2()
    #fonction_b1()
    fonction_sous_module_propagation()
    fonction_sous_module_surcharge()
    logger.info("Fin de l'application.")

if __name__ == "__main__":
    main()
