#!/usr/bin/env python
###############################################################################################
#  Author: 
_author = '<a href="mailto:debuti@gmail.com">Borja Garcia</a>'
# Program: 
_name = 'template'
# Descrip: 
_description = ''' '''
# Version: 
_version = '0.0.0'
#    Date:
_date = 'YYYY-MM-DD:hh:mm'
# License: This script doesn't require any license since it's not intended to be redistributed.
#          In such case, unless stated otherwise, the purpose of the author is to follow GPLv3.
# History: 0.0.0 (YYYY-MM-DD:hh:mm)
#            -Initial release
###############################################################################################

# imports
import logging
import sys
import doctest
import datetime, time
import os
import subprocess
import optparse
import inspect

# User-libs imports 
LIB_PATH = 'lib'
sys.path.append(LIB_PATH)

  # Example : 
   #from Utils import *
   #print shellutils.runBash('dir')

# Parameters n' Constants
APP_PATH = os.getcwd() + os.path.sep + '.' + _name 
LOG_PATH = APP_PATH + os.path.sep + 'logs'
LOG_FILENAME = LOG_PATH + os.path.sep + _name + '_' + time.strftime("%Y%m%d_%H%M%S") + '.log'

# Global variables
global logger
logger = ""

# Error declaration
error = { "" : "",
          "" : "",
          "" : "" }

# Usage function, logs, utils and check input
def now():
    '''This function returns the current time
    '''

    return time.strftime("%Y-%m-%d:%H:%M:%S")


def openLog(logger):
    '''This function is for initialize the logging job
    '''
  
    desiredLevel = logging.DEBUG
    logger = logging.getLogger(_name)
    logger.setLevel(desiredLevel)
    # create file handler which logs even debug messages
    fh = logging.FileHandler(LOG_FILENAME)
    fh.setLevel(desiredLevel)
    # create console handler with a higher log level
    ch = logging.StreamHandler()
    ch.setLevel(desiredLevel)
    # create formatter and add it to the handlers
    formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
    ch.setFormatter(formatter)
    fh.setFormatter(formatter)
    # add the handlers to logger
    logger.addHandler(ch)
    logger.addHandler(fh)

    return logger

def closeLog():
    '''This function is for shutdown the logging job
    '''
  
    logging.shutdown()

def checkInput():
    '''This function is for treat the user command line parameters.
    '''

    #####THIS SECTION IS A EXAMPLE#####
    #Create instance of OptionParser Module, included in Standard Library
    p = optparse.OptionParser(description=_description,
                              prog=_name,
                              version=_version,
                              usage='''%prog [options]''') 
    p.add_option('--old', '-o', action="store", type="string", dest="old_regexp", help='Regular expression to search for')
    p.add_option('--new', '-n', action="store", type="string", dest="new_string", help='New text to replace it')
    p.add_option('--preview','-p', action="store_true", dest="do_preview", help='Ask to replace the coincidence before doing it')
    p.add_option('--file','-f', action="store", type="string", dest="filename", help='The input/output file')

    #Parse the commandline
    options, arguments = p.parse_args()

    #Decide what to do
    if options.old_regexp is None or options.new_string is None or options.filename is None :
        p.print_help()
        sys.exit(-1)
    else:
        old_regexp = options.old_regexp
        new_string = options.new_string
        do_preview = options.do_preview
        filename = options.filename
        return [old_regexp, new_string, do_preview, filename]

    #####/THIS SECTION IS A EXAMPLE#####

# Helper functions
def createWorkDir():
    '''This function is for creating the working directory, if its not already
    '''

    #####THIS SECTION IS A EXAMPLE#####

    if not os.path.isdir(APP_PATH):
        os.mkdir(APP_PATH)
    if not os.path.isdir(LOG_PATH):
        os.mkdir(LOG_PATH)
    if not os.path.isfile(LOG_FILENAME):
        f = open(LOG_FILENAME, "w")
        f.close()

    #####/THIS SECTION IS A EXAMPLE#####

# Main function
def main():
    '''This is the main procedure
    '''
    
    createWorkDir()
    

# Entry point
if __name__ == '__main__':
    checkInput()
    openLog()
    main()
    closeLog()
