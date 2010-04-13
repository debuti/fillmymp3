#!/usr/bin/env python
###############################################################################################
#  Author: 
_author = '<a href="mailto:debuti@gmail.com">Borja Garcia</a>'
# Program: 
_name = 'configTemplate'
# Descrip: 
_description = '''This scripts customizes the project and copies the required libraries'''
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
import sys, shutil
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
global now
global logger
global verbose
now = time.strftime("%Y-%m-%d:%H:%M:%S")
logger = ""

requiredLibraries = { "from" : "",
                      "b" : "2",
                      "c" : "3" }

# Error declaration
error = { "" : "",
          "" : "",
          "" : "" }

# Usage function, logs, utils and check input

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
    # create console handler with a higher log level
    ch = logging.StreamHandler()
    ch.setLevel(desiredLevel)
    # create formatter and add it to the handlers
    formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
    ch.setFormatter(formatter)
    # add the handlers to logger
    logger.addHandler(ch)

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
def copyLibraries():
    '''This procedure copies the libraries in its last version'''
    PYTHON_CUSTOM_LIB_PATH = os.getenv("PYTHON_CUSTOM_LIB_PATH")
    for i in requiredLibraries.keys():
        if requiredLibraries[i] == "":
            to = os.getcwd() + os.path.sep + 'lib'
        else:
            to = requiredLibraries[i]
            
        print "Copying", i, " to ", to  
        #remove the destination first
        shutil.copy(i, to)
    
# Main function
def main():
    '''This is the main procedure
  
    --Description--
  
    --Test--
    >>> print main()
  
    '''
    copyLibraries()

    

# Entry point
if __name__ == '__main__':
    #checkInput()
    openLog()
    main()
    closeLog()
