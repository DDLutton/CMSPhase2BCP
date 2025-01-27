set moduleName TPG
set isTaskLevelControl 1
set isCombinational 0
set isDatapathOnly 0
set isPipelined 1
set pipeline_type function
set FunctionProtocol ap_ctrl_hs
set isOneStateSeq 0
set ProfileFlag 0
set StallSigGenFlag 0
set C_modelName {TPG}
set C_modelType { int 54 }
set C_modelArgList {
	{ data_int_V int 14 regular  }
	{ lincoeff_V int 24 regular  }
	{ r_0_shift_reg_V int 18 regular {pointer 2}  }
	{ r_1_shift_reg_V int 18 regular {pointer 2}  }
	{ r_2_shift_reg_V int 18 regular {pointer 2}  }
	{ r_3_shift_reg_V int 18 regular {pointer 2}  }
	{ r_0_peak_reg_V_read int 19 regular  }
	{ r_1_peak_reg_V_read int 19 regular  }
}
set C_modelArgMapList {[ 
	{ "Name" : "data_int_V", "interface" : "wire", "bitwidth" : 14, "direction" : "READONLY"} , 
 	{ "Name" : "lincoeff_V", "interface" : "wire", "bitwidth" : 24, "direction" : "READONLY"} , 
 	{ "Name" : "r_0_shift_reg_V", "interface" : "wire", "bitwidth" : 18, "direction" : "READWRITE"} , 
 	{ "Name" : "r_1_shift_reg_V", "interface" : "wire", "bitwidth" : 18, "direction" : "READWRITE"} , 
 	{ "Name" : "r_2_shift_reg_V", "interface" : "wire", "bitwidth" : 18, "direction" : "READWRITE"} , 
 	{ "Name" : "r_3_shift_reg_V", "interface" : "wire", "bitwidth" : 18, "direction" : "READWRITE"} , 
 	{ "Name" : "r_0_peak_reg_V_read", "interface" : "wire", "bitwidth" : 19, "direction" : "READONLY"} , 
 	{ "Name" : "r_1_peak_reg_V_read", "interface" : "wire", "bitwidth" : 19, "direction" : "READONLY"} , 
 	{ "Name" : "ap_return", "interface" : "wire", "bitwidth" : 54} ]}
# RTL Port declarations: 
set portNum 26
set portList { 
	{ ap_clk sc_in sc_logic 1 clock -1 } 
	{ ap_rst sc_in sc_logic 1 reset -1 active_high_sync } 
	{ ap_start sc_in sc_logic 1 start -1 } 
	{ ap_done sc_out sc_logic 1 predone -1 } 
	{ ap_idle sc_out sc_logic 1 done -1 } 
	{ ap_ready sc_out sc_logic 1 ready -1 } 
	{ ap_ce sc_in sc_logic 1 ce -1 } 
	{ data_int_V sc_in sc_lv 14 signal 0 } 
	{ lincoeff_V sc_in sc_lv 24 signal 1 } 
	{ r_0_shift_reg_V_i sc_in sc_lv 18 signal 2 } 
	{ r_0_shift_reg_V_o sc_out sc_lv 18 signal 2 } 
	{ r_0_shift_reg_V_o_ap_vld sc_out sc_logic 1 outvld 2 } 
	{ r_1_shift_reg_V_i sc_in sc_lv 18 signal 3 } 
	{ r_1_shift_reg_V_o sc_out sc_lv 18 signal 3 } 
	{ r_1_shift_reg_V_o_ap_vld sc_out sc_logic 1 outvld 3 } 
	{ r_2_shift_reg_V_i sc_in sc_lv 18 signal 4 } 
	{ r_2_shift_reg_V_o sc_out sc_lv 18 signal 4 } 
	{ r_2_shift_reg_V_o_ap_vld sc_out sc_logic 1 outvld 4 } 
	{ r_3_shift_reg_V_i sc_in sc_lv 18 signal 5 } 
	{ r_3_shift_reg_V_o sc_out sc_lv 18 signal 5 } 
	{ r_3_shift_reg_V_o_ap_vld sc_out sc_logic 1 outvld 5 } 
	{ r_0_peak_reg_V_read sc_in sc_lv 19 signal 6 } 
	{ r_1_peak_reg_V_read sc_in sc_lv 19 signal 7 } 
	{ ap_return_0 sc_out sc_lv 16 signal -1 } 
	{ ap_return_1 sc_out sc_lv 19 signal -1 } 
	{ ap_return_2 sc_out sc_lv 19 signal -1 } 
}
set NewPortList {[ 
	{ "name": "ap_clk", "direction": "in", "datatype": "sc_logic", "bitwidth":1, "type": "clock", "bundle":{"name": "ap_clk", "role": "default" }} , 
 	{ "name": "ap_rst", "direction": "in", "datatype": "sc_logic", "bitwidth":1, "type": "reset", "bundle":{"name": "ap_rst", "role": "default" }} , 
 	{ "name": "ap_start", "direction": "in", "datatype": "sc_logic", "bitwidth":1, "type": "start", "bundle":{"name": "ap_start", "role": "default" }} , 
 	{ "name": "ap_done", "direction": "out", "datatype": "sc_logic", "bitwidth":1, "type": "predone", "bundle":{"name": "ap_done", "role": "default" }} , 
 	{ "name": "ap_idle", "direction": "out", "datatype": "sc_logic", "bitwidth":1, "type": "done", "bundle":{"name": "ap_idle", "role": "default" }} , 
 	{ "name": "ap_ready", "direction": "out", "datatype": "sc_logic", "bitwidth":1, "type": "ready", "bundle":{"name": "ap_ready", "role": "default" }} , 
 	{ "name": "ap_ce", "direction": "in", "datatype": "sc_logic", "bitwidth":1, "type": "ce", "bundle":{"name": "ap_ce", "role": "default" }} , 
 	{ "name": "data_int_V", "direction": "in", "datatype": "sc_lv", "bitwidth":14, "type": "signal", "bundle":{"name": "data_int_V", "role": "default" }} , 
 	{ "name": "lincoeff_V", "direction": "in", "datatype": "sc_lv", "bitwidth":24, "type": "signal", "bundle":{"name": "lincoeff_V", "role": "default" }} , 
 	{ "name": "r_0_shift_reg_V_i", "direction": "in", "datatype": "sc_lv", "bitwidth":18, "type": "signal", "bundle":{"name": "r_0_shift_reg_V", "role": "i" }} , 
 	{ "name": "r_0_shift_reg_V_o", "direction": "out", "datatype": "sc_lv", "bitwidth":18, "type": "signal", "bundle":{"name": "r_0_shift_reg_V", "role": "o" }} , 
 	{ "name": "r_0_shift_reg_V_o_ap_vld", "direction": "out", "datatype": "sc_logic", "bitwidth":1, "type": "outvld", "bundle":{"name": "r_0_shift_reg_V", "role": "o_ap_vld" }} , 
 	{ "name": "r_1_shift_reg_V_i", "direction": "in", "datatype": "sc_lv", "bitwidth":18, "type": "signal", "bundle":{"name": "r_1_shift_reg_V", "role": "i" }} , 
 	{ "name": "r_1_shift_reg_V_o", "direction": "out", "datatype": "sc_lv", "bitwidth":18, "type": "signal", "bundle":{"name": "r_1_shift_reg_V", "role": "o" }} , 
 	{ "name": "r_1_shift_reg_V_o_ap_vld", "direction": "out", "datatype": "sc_logic", "bitwidth":1, "type": "outvld", "bundle":{"name": "r_1_shift_reg_V", "role": "o_ap_vld" }} , 
 	{ "name": "r_2_shift_reg_V_i", "direction": "in", "datatype": "sc_lv", "bitwidth":18, "type": "signal", "bundle":{"name": "r_2_shift_reg_V", "role": "i" }} , 
 	{ "name": "r_2_shift_reg_V_o", "direction": "out", "datatype": "sc_lv", "bitwidth":18, "type": "signal", "bundle":{"name": "r_2_shift_reg_V", "role": "o" }} , 
 	{ "name": "r_2_shift_reg_V_o_ap_vld", "direction": "out", "datatype": "sc_logic", "bitwidth":1, "type": "outvld", "bundle":{"name": "r_2_shift_reg_V", "role": "o_ap_vld" }} , 
 	{ "name": "r_3_shift_reg_V_i", "direction": "in", "datatype": "sc_lv", "bitwidth":18, "type": "signal", "bundle":{"name": "r_3_shift_reg_V", "role": "i" }} , 
 	{ "name": "r_3_shift_reg_V_o", "direction": "out", "datatype": "sc_lv", "bitwidth":18, "type": "signal", "bundle":{"name": "r_3_shift_reg_V", "role": "o" }} , 
 	{ "name": "r_3_shift_reg_V_o_ap_vld", "direction": "out", "datatype": "sc_logic", "bitwidth":1, "type": "outvld", "bundle":{"name": "r_3_shift_reg_V", "role": "o_ap_vld" }} , 
 	{ "name": "r_0_peak_reg_V_read", "direction": "in", "datatype": "sc_lv", "bitwidth":19, "type": "signal", "bundle":{"name": "r_0_peak_reg_V_read", "role": "default" }} , 
 	{ "name": "r_1_peak_reg_V_read", "direction": "in", "datatype": "sc_lv", "bitwidth":19, "type": "signal", "bundle":{"name": "r_1_peak_reg_V_read", "role": "default" }} , 
 	{ "name": "ap_return_0", "direction": "out", "datatype": "sc_lv", "bitwidth":16, "type": "signal", "bundle":{"name": "ap_return_0", "role": "default" }} , 
 	{ "name": "ap_return_1", "direction": "out", "datatype": "sc_lv", "bitwidth":19, "type": "signal", "bundle":{"name": "ap_return_1", "role": "default" }} , 
 	{ "name": "ap_return_2", "direction": "out", "datatype": "sc_lv", "bitwidth":19, "type": "signal", "bundle":{"name": "ap_return_2", "role": "default" }}  ]}

set RtlHierarchyInfo {[
	{"ID" : "0", "Level" : "0", "Path" : "`AUTOTB_DUT_INST", "Parent" : "", "Child" : ["1", "2"],
		"CDFG" : "TPG",
		"Protocol" : "ap_ctrl_hs",
		"ControlExist" : "1", "ap_start" : "1", "ap_ready" : "1", "ap_done" : "1", "ap_continue" : "0", "ap_idle" : "1",
		"Pipeline" : "Aligned", "UnalignedPipeline" : "0", "RewindPipeline" : "0", "ProcessNetwork" : "0",
		"II" : "1",
		"VariableLatency" : "0", "ExactLatency" : "2", "EstimateLatencyMin" : "2", "EstimateLatencyMax" : "2",
		"Combinational" : "0",
		"Datapath" : "0",
		"ClockEnable" : "1",
		"InDataflowNetwork" : "0",
		"Port" : [
			{"Name" : "data_int_V", "Type" : "None", "Direction" : "I"},
			{"Name" : "lincoeff_V", "Type" : "None", "Direction" : "I"},
			{"Name" : "r_0_shift_reg_V", "Type" : "OVld", "Direction" : "IO"},
			{"Name" : "r_1_shift_reg_V", "Type" : "OVld", "Direction" : "IO"},
			{"Name" : "r_2_shift_reg_V", "Type" : "OVld", "Direction" : "IO"},
			{"Name" : "r_3_shift_reg_V", "Type" : "OVld", "Direction" : "IO"},
			{"Name" : "r_0_peak_reg_V_read", "Type" : "None", "Direction" : "I"},
			{"Name" : "r_1_peak_reg_V_read", "Type" : "None", "Direction" : "I"}]},
	{"ID" : "1", "Level" : "1", "Path" : "`AUTOTB_DUT_INST.algo_unpacked_mulbkb_U1", "Parent" : "0"},
	{"ID" : "2", "Level" : "1", "Path" : "`AUTOTB_DUT_INST.algo_unpacked_mulcud_U2", "Parent" : "0"}]}


set ArgLastReadFirstWriteLatency {
	TPG {
		data_int_V {Type I LastRead 0 FirstWrite -1}
		lincoeff_V {Type I LastRead 0 FirstWrite -1}
		r_0_shift_reg_V {Type IO LastRead 0 FirstWrite 0}
		r_1_shift_reg_V {Type IO LastRead 0 FirstWrite 0}
		r_2_shift_reg_V {Type IO LastRead 0 FirstWrite 0}
		r_3_shift_reg_V {Type IO LastRead 0 FirstWrite 0}
		r_0_peak_reg_V_read {Type I LastRead 0 FirstWrite -1}
		r_1_peak_reg_V_read {Type I LastRead 0 FirstWrite -1}}}

set hasDtUnsupportedChannel 0

set PerformanceInfo {[
	{"Name" : "Latency", "Min" : "2", "Max" : "2"}
	, {"Name" : "Interval", "Min" : "1", "Max" : "1"}
]}

set PipelineEnableSignalInfo {[
	{"Pipeline" : "0", "EnableSignal" : "ap_enable_pp0"}
]}

set Spec2ImplPortList { 
	data_int_V { ap_none {  { data_int_V in_data 0 14 } } }
	lincoeff_V { ap_none {  { lincoeff_V in_data 0 24 } } }
	r_0_shift_reg_V { ap_ovld {  { r_0_shift_reg_V_i in_data 0 18 }  { r_0_shift_reg_V_o out_data 1 18 }  { r_0_shift_reg_V_o_ap_vld out_vld 1 1 } } }
	r_1_shift_reg_V { ap_ovld {  { r_1_shift_reg_V_i in_data 0 18 }  { r_1_shift_reg_V_o out_data 1 18 }  { r_1_shift_reg_V_o_ap_vld out_vld 1 1 } } }
	r_2_shift_reg_V { ap_ovld {  { r_2_shift_reg_V_i in_data 0 18 }  { r_2_shift_reg_V_o out_data 1 18 }  { r_2_shift_reg_V_o_ap_vld out_vld 1 1 } } }
	r_3_shift_reg_V { ap_ovld {  { r_3_shift_reg_V_i in_data 0 18 }  { r_3_shift_reg_V_o out_data 1 18 }  { r_3_shift_reg_V_o_ap_vld out_vld 1 1 } } }
	r_0_peak_reg_V_read { ap_none {  { r_0_peak_reg_V_read in_data 0 19 } } }
	r_1_peak_reg_V_read { ap_none {  { r_1_peak_reg_V_read in_data 0 19 } } }
}
