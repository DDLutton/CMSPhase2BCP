############################################################
## This file is generated automatically by Vivado HLS.
## Please DO NOT edit it.
## Copyright (C) 1986-2016 Xilinx, Inc. All Rights Reserved.
############################################################
open_project BCP
set_top algo_unpacked
add_files src/TPG.cc
add_files src/algo_unpacked.cpp
add_files -tb src/algo_unpacked_tb.cpp
open_solution "solution1"
set_part {xc7vx690tffg1927-2} -tool vivado
create_clock -period 8.333 -name default
#source "./BCP/solution1/directives.tcl"
csim_design -compiler gcc
csynth_design
cosim_design
export_design -format ip_catalog
