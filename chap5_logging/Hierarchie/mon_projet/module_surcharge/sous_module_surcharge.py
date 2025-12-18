import logging

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

def fonction_sous_module_surcharge():
    logger.info("Exécution de fonction_sous_module_surcharge.")
    logger.debug("Debugging dans fonction_sous_module_surcharge.")
    logger.error("Erreur dans fonction_sous_module_surcharge.")
