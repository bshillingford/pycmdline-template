#!/usr/bin/env python2
#

import sys, argparse, logging


def main(args, loglevel):
    logging.basicConfig(format="%(levelname)s: %(message)s", level=loglevel)
    
    # TODO Replace this with your actual code.
    print "Hello there."
    logging.info("You passed an argument.")
    logging.debug("Your Argument: %s" % args.argument)


if __name__ == '__main__':
    parser = argparse.ArgumentParser( 
                                      description = "Manipulates a hostname before running a command.",
                                      epilog = "As an alternative to the commandline, params can be placed in a file, one per line, and specified on the commandline like '%(prog)s @params.conf'.",
                                      fromfile_prefix_chars = '@' )
    # TODO Specify your real parameters here.
    parser.add_argument(
                        "argument",
                        help = "pass ARG to the program",
                        metavar = "ARG")
    parser.add_argument(
                        "-v",
                        "--verbose",
                        help="increase output verbosity",
                        action="store_true")
    args = parser.parse_args()
    
    # Setup logging
    if args.verbose:
        loglevel = logging.DEBUG
    else:
        loglevel = logging.INFO
    
    main(args, loglevel)
