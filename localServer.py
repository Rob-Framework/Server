import logging
import time
from main import run
from tcpServer import tcpServer

logger = logging.getLogger('server_logger')
logger.setLevel(logging.DEBUG)
# create file handler which logs even debug messages
fh = logging.FileHandler('grpc_server.log')
fh.setLevel(logging.DEBUG)

logger.addHandler(fh)

tcpServer("0.0.0.0", 7781)
run()