#pylint: disable=E0401

import error
import sys
import version_manager

try:
    version_manager.main()
except:
    message = "Could not launch HappyMac"
    error.error(message)
    sys.exit(message)
