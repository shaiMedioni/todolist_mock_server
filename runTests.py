import logging
import pytest
import datetime

e = datetime.datetime.now()

logging.basicConfig(filename='config_check.log', level=logging.INFO)
# log the time of the test
logging.info("Time: %s" % e)
logging.info('start')
pytest.main()
logging.info('done\n')
