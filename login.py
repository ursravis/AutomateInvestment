import emailhelper
import logging
import logconfig

logger = logging.getLogger(__name__)

def main():
    logconfig.configure()
    logger.info('Starting process')
    emailhelper.sendmail("login Succeed")
    logging.info('Cmpleted process')

if __name__ == "__main__":
    main()