## Set the top level module
set_top algo_unpacked_DCLRps_NojR_S
##
#### Add source code
add_files src/algo_unpacked_DCLRps_NojR_S.cpp
add_files src/TPG.cc

#
### Add testbed files
add_files -tb src/algo_unpacked_DCLRps_NojR_S_tb.cpp 

### Add test input files
add_files -tb data/test2_DCLRps_NojR_S_inp.txt
add_files -tb data/test2_DCLRps_NojR_S_out_ref.txt
