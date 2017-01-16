#!/bin/env python
# coding: UTF-8

# log
#
# Copyright(c) 2015 Uptime Technologies, LLC.

import logging

logging.basicConfig(format='[%(asctime)s] %(levelname)s: %(message)s',
                    datefmt="%Y-%m-%d %H:%M:%S")
logger = logging.getLogger('PsqlWrapper')
logger.setLevel(logging.INFO)

INFO = logging.INFO
DEBUG = logging.DEBUG

def setLevel(level):
    logger.setLevel(level)

def debug(msg, *args):
    logger.debug(msg, *args)

def error(msg, *args):
    logger.error(msg, *args)

def warning(msg, *args):
    logger.warning(msg, *args)

def info(msg, *args):
    logger.info(msg, *args)
