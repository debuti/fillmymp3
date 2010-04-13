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

LIB_PATH = 'lib'
sys.path.append(LIB_PATH)
print sys.path


#print inspect.getfile( inspect.currentframe() )

import Utils.shellutils.shellutils

# Parameters n' Constants
APP_PATH = os.getcwd() + '\\.' + _name 
LOG_PATH = APP_PATH + '\\' + 'logs'
LOG_FILENAME = LOG_PATH + '\\' + _name + '_' + time.strftime("%Y-%m-%d:%H:%M:%S") + '.log'

# Global variables
global now
global logger
global verbose
now = time.strftime("%Y-%m-%d:%H:%M:%S")
logger = ""

# Error declaration
error = { "" : "",
          "" : "",
          "" : "" }

# Usage function, logs, utils and check input
def createWorkDir():
    '''This function is for creating the working directory, if its not already
  
    --Description--

    --Test--
    >>> print createWorkDir()
    '''
  #TODO: Copy myself to global application path
    if not os.path.isdir(APP_PATH):
        os.mkdir(APP_PATH)
    if not os.path.isdir(LOG_PATH):
        os.mkdir(LOG_PATH)

def openLog():
    '''This function is for initialize the logging job
  
    --Description--

    --Test--
    >>> print openLog()
    '''
  
    global logger

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

def closeLog():
    '''This function is for shutdown the logging job

    --Description--

    --Test--
    >>> print closeLog()
    '''
  
    logging.shutdown()

def checkInput():
    '''This function is for treat the user command line parameters.

    --Description--

    --Test--
    >>> print checkInput()
  
    '''

    #####THIS SECTION IS A EXAMPLE#####
	#Global variable use declaration

    global verbose
	
    #Create instance of OptionParser Module, included in Standard Library
    p = optparse.OptionParser(description=_description,
                                            prog=_name,
                                            version=_version,
                                            usage='''\
%prog [options]''') 
    p.add_option('--ip','-i', action="store_true", help='gets current IP Address')
    p.add_option('--usage', '-u', action="store_true", help='gets disk usage of homedir')
    p.add_option('--verbose', '-v',
                action = 'store_true',
                help='prints verbosely',
                default=False)

    #Option Handling passes correct parameter to runBash
    options, arguments = p.parse_args()

    if len(arguments) == 1:
        p.print_help()
        sys.exit(-1)
    if options.verbose:
        verbose=True
    if options.ip:
        value = runBash(IPADDR)
        report(value,"IPADDR")
    elif options.usage:
        value = runBash(HOMEDIR_USAGE)
        report(value, "HOMEDIR_USAGE")
    else:
        p.print_help()
    #####/THIS SECTION IS A EXAMPLE#####

# Helper functions


# Main function
def main():
    '''This is the main procedure
  
    --Description--
  
    --Test--
    >>> print main()
  
    '''
    
    

# Entry point
if __name__ == '__main__':
    #doctest.testmod()   # automaticly run tests
    checkInput()
    createWorkDir()
    openLog()
    main()
    closeLog()
