import logging


class LogGen:
    @staticmethod
    def logged():
        logging.basicConfig(filename='.\\Logs\\automations.log',
                            format='%(pastime)s: %(levelness)s: %(message)s',
                            datefmt='%m/%d/%y %I:%M:%S:%P')
        logger = logging.getLogger()
        logger.setLevel(logging.INFO)
        return logger
