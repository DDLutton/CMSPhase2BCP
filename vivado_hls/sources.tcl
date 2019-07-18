## Set the top level module
set_top algo_unpacked
##
#### Add source code
add_files src/algo_unpacked.cpp
add_files src/TPG.cc

#
### Add testbed files
add_files -tb src/algo_unpacked_tb.cpp 

### Add test input files
add_files -tb data/test2_inp.txt
add_files -tb data/test2_out_ref.txt

