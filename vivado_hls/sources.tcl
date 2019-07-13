## Set the top level module
set_top algo_unpacked_DCLRps_NojR
##
#### Add source code
add_files src/algo_unpacked_DCLRps_NojR.cpp
add_files src/TPG.cc

#
### Add testbed files
add_files -tb src/algo_unpacked_DCLRps_NojR_tb.cpp 

### Add test input files
add_files -tb data/test2_DCLRps_NojR_inp.txt
add_files -tb data/test2_DCLRps_NojR_out_ref.txt
