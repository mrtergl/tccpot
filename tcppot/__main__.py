"""
TCPPOT

Simple TCP honeypot logger

Usage:
    tcppot --config File [<config_file>]

Options:
     --config File      Path to config options in i.ni file
    -h --help           Show this script
"""
import configparser
import logging
import sys
from tcppot import TcpPot

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

config_filepath = 'tcppot.ini'

config = configparser.ConfigParser()
config.read(config_filepath)

ports = config.get('default', 'ports', raw=True, fallback="22,80,443,8080,8888,9999,3306")
log_filepath = config.get('default', 'logfile', raw=True, fallback="C:\\Users\\murat\\honeypot\\tcppot.log")

ports_list = []
try:
    ports_list = ports.split(",")
except Exception as e:
    logger.error("Error while parsing ports: %s", ports)

honeypot = TcpPot(ports_list, log_filepath)
honeypot.run()
