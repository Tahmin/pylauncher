#!/usr/bin/env python

import pylauncher3

##
## Emulate the classic launcher, using a one liner
##

pylauncher3.ClassicLauncher("commandlines",
                            numactl="core",
                            debug="job+host+exec",
                            )
