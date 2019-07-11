## Set the top level module
set_top algo_unpacked_DC_NojR
##
#### Add source code
add_files src/algo_unpacked_DC_NojR.cpp
add_files src/TPG.cc

#
### Add testbed files
add_files -tb src/algo_unpacked_DC_NojR_tb.cpp 

### Add test input files
add_files -tb data/test1_inp.txt
add_files -tb data/test1_out_ref.txt
add_files -tb data/test2_DC_NojR_inp.txt
add_files -tb data/test2_DC_NojR_out_ref.txt

add_files -tb data/rnd_inp.txt
add_files -tb data/rnd_out_ref.txt
