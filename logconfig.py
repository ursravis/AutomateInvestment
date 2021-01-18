from opencensus.ext.azure.log_exporter import AzureLogHandler
import logging

def configure():

    logger = logging.getLogger(__name__)
    logging.basicConfig(filename='logs/logfile.log',level=logging.DEBUG,format='%(asctime)s %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p')

    logger.addHandler(AzureLogHandler(
        connection_string='InstrumentationKey=d55e7aef-fec3-498b-8d52-230503cc5fe2;IngestionEndpoint=https://centralindia-0.in.applicationinsights.azure.com/')
    )
    properties = {'custom_dimensions': {'key_1': 'value_1', 'key_2': 'value_2'}}

        # Use properties in logging statements
    logger.warning('action', extra=properties)