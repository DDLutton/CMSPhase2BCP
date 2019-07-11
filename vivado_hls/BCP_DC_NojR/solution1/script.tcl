############################################################
## This file is generated automatically by Vivado HLS.
## Please DO NOT edit it.
## Copyright (C) 1986-2018 Xilinx, Inc. All Rights Reserved.
############################################################
open_project BCP_DC_NojR
set_top algo_unpacked_DC_NojR
add_files src/TPG.cc
add_files src/algo_unpacked_DC_NojR.cpp
add_files -tb src/algo_unpacked_DC_NojR_tb.cpp
add_files -tb data/test2_DC_NojR_inp.txt
add_files -tb data/test2_DC_NojR_out_ref.txt
open_solution "solution1"
set_part {xc7vx690tffg1927-2} -tool vivado
create_clock -period 8.333 -name default
#source "./BCP_DC_NojR/solution1/directives.tcl"
csim_design -argv {test2_DC_NojR} -clean -compiler gcc
csynth_design
cosim_design
export_design -format ip_catalog
