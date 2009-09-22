"""
Worksheet process base clase

AUTHORS:

  - William Stein
"""

#############################################################################
#
#       Copyright (C) 2009 William Stein <wstein@gmail.com>
#  Distributed under the terms of the GNU General Public License (GPL)
#  The full text of the GPL is available at:
#                  http://www.gnu.org/licenses/
#
#############################################################################

###################################################################
# Abstract base class
###################################################################
class WorksheetProcess:
    """
    A controlled Python process that executes code.  This is a
    reference implementation.
    """
    def __init__(self):
        """
        Initialize this worksheet process.
        """
        raise NotImplementedError

    def __repr__(self):
        """
        Return string representation of this worksheet process. 
        """
        return "Worksheet process"

    def __getstate__(self):
        """
        Used for pickling.  We return an empty state otherwise
        this could not be pickled.
        """
        return {}

    ###########################################################
    # Control the state of the subprocess
    ###########################################################
    def interrupt(self):
        """
        Send an interrupt signal to the currently running computation
        in the controlled process.  This may or may not succeed.  Call
        ``self.is_computing()`` to find out if it did. 
        """
        raise NotImplementedError

    def quit(self):
        """
        Quit this worksheet process.  
        """
        raise NotImplementedError

    def start(self):
        """
        Start this worksheet process running.
        """
        raise NotImplementedError

    ###########################################################
    # Query the state of the subprocess
    ###########################################################
    def is_computing(self):
        """
        Return True if a computation is currently running in this worksheet subprocess.

        OUTPUT:

            - ``bool``
        """
        raise NotImplementedError        

    def is_started(self):
        """
        Return true if this worksheet subprocess has already been started.

        OUTPUT:

            - ``bool``
        """
        raise NotImplementedError                

    ###########################################################
    # Sending a string to be executed in the subprocess
    ###########################################################
    def execute(self, string):
        """
        Start executing the given string in this subprocess.

        INPUT:

            ``string`` -- a string containing code to be executed.
        """
        raise NotImplementedError                        

    ###########################################################
    # Getting the output so far from a subprocess
    ###########################################################
    def output_status(self):
        """
        Return OutputStatus object, which includes output from the
        subprocess from the last executed command up until now,
        information about files that were created, and whether
        computing is now done.

        OUTPUT:

            - ``OutputStatus`` object.
        """
        raise NotImplementedError                        




