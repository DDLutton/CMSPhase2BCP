#!/bin/sh
lli=${LLVMINTERP-lli}
exec $lli \
    /afs/cern.ch/user/d/dlutton/dlutton/VHLS/centos/praCodeMyFork/CMSPhase2BCP/vivado_hls/ProjL/solution1/.autopilot/db/a.g.bc ${1+"$@"}
