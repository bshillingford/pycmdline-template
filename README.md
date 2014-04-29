pycmdline-template
==================

Template for making your one-off Python utilities more user-friendly.

Add `@arg` and `@cmdline` decorators to a main function as below; this provides an easier interface to the `logging` and `optparse` modules.

# Examples
## Example 1: simple program
This program accepts 2 arguments: one a flag passed as `--count=COUNT`, or `-n COUNT`; another is a position argument, listed without a dash-prefixed flag name before it; and a default help flag `--help`/`-h` printing a usage page.

The arguments to the decorators are the same as in `optparse`.

```python
#!/usr/bin/env python

from simpleargs import cmdline, arg

@arg('argument', help="pass ARG to program", metavar="ARG") # simple positional argument
@arg('--count', '-n', help="number of bars to foo", type=int, default=1)
@cmdline(description="This program foos bars a given number of times.")
def main(argument, count):

    print("Hello there.")

    print("Your Argument: %s" % argument)

    for i in range(count):
        print("Fooing bar #%d" % i)
    print("Fooed %d bars." % count)

if __name__ == '__main__':
    main()
```

## Example 2: simple program + logging
```
#!/usr/bin/env python

import logging as L
from simpleargs import cmdline, arg, loglevel


@arg('argument', help="pass ARG to program", metavar="ARG") # simple positional argument
@arg('--count', '-n', type=int, default=1)
@loglevel()                                                 # if on, log level DEBUG, else INFO
@cmdline(description="This program foos bars a given number of times.")
def main(argument, count):

    print "Hello there."

    L.info("You passed an argument.")
    L.debug("Your Argument: %s" % argument)

    for i in range(count):
        L.debug("Fooing bar #%d" % i)
    L.info("Fooed %d bars." % count)

if __name__ == '__main__':
    main()
```
