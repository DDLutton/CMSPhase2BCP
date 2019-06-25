############################################################
## This file is generated automatically by Vivado HLS.
## Please DO NOT edit it.
## Copyright (C) 1986-2018 Xilinx, Inc. All Rights Reserved.
############################################################
open_project ProjL
set_top algo_unpacked
add_files src/algo_unpacked.cpp
add_files src/TPG.cc
add_files -tb data/test3_out_ref.txt
add_files -tb data/test3_inp.txt
add_files -tb data/test2_out_ref.txt
add_files -tb data/test2_inp.txt
add_files -tb data/test1_out_ref.txt
add_files -tb data/test1_inp.txt
add_files -tb data/rnd_out_ref.txt
add_files -tb data/rnd_inp.txt
add_files -tb src/algo_unpacked_tb.cpp
open_solution "solution1"
set_part {xc7vx690tffg1927-2} -tool vivado
create_clock -period 120MHz -name default
#source "./ProjL/solution1/directives.tcl"
csim_design -argv {test1} -clean -compiler gcc
csynth_design
cosim_design -compiler gcc -argv {test1}
export_design -format ip_catalog
