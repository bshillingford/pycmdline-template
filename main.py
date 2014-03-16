#!/usr/bin/env python2
#

import logging as L
from simpleargs import cmdline, arg, loglevel


@arg('argument', help="pass ARG to program", metavar="ARG") # simple positional argument
@arg('--count', '-n', type=int, default=1)
@loglevel()                                                 # if on, log level DEBUG, else INFO
@cmdline(description="This program foos bars a given number of times.")
def main(argument, count):
    # TODO: Replace this with your actual code.

    print "Hello there."

    L.info("You passed an argument.")
    L.debug("Your Argument: %s" % argument)

    for i in range(count):
        L.debug("Fooing bar #%d" % i)
    L.info("Fooed %d bars." % count)


if __name__ == '__main__':
    main()
