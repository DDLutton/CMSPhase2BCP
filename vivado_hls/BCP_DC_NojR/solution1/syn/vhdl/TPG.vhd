-- ==============================================================
-- RTL generated by Vivado(TM) HLS - High-Level Synthesis from C, C++ and SystemC
-- Version: 2016.4
-- Copyright (C) 1986-2016 Xilinx, Inc. All Rights Reserved.
-- 
-- ===========================================================

library IEEE;
use IEEE.std_logic_1164.all;
use IEEE.numeric_std.all;

entity TPG is
port (
    ap_clk : IN STD_LOGIC;
    ap_rst : IN STD_LOGIC;
    ap_start : IN STD_LOGIC;
    ap_done : OUT STD_LOGIC;
    ap_idle : OUT STD_LOGIC;
    ap_ready : OUT STD_LOGIC;
    ap_ce : IN STD_LOGIC;
    data_int_V : IN STD_LOGIC_VECTOR (13 downto 0);
    r_0_shift_reg_V_i : IN STD_LOGIC_VECTOR (13 downto 0);
    r_0_shift_reg_V_o : OUT STD_LOGIC_VECTOR (13 downto 0);
    r_0_shift_reg_V_o_ap_vld : OUT STD_LOGIC;
    r_1_shift_reg_V_i : IN STD_LOGIC_VECTOR (13 downto 0);
    r_1_shift_reg_V_o : OUT STD_LOGIC_VECTOR (13 downto 0);
    r_1_shift_reg_V_o_ap_vld : OUT STD_LOGIC;
    r_2_shift_reg_V_i : IN STD_LOGIC_VECTOR (13 downto 0);
    r_2_shift_reg_V_o : OUT STD_LOGIC_VECTOR (13 downto 0);
    r_2_shift_reg_V_o_ap_vld : OUT STD_LOGIC;
    r_3_shift_reg_V_i : IN STD_LOGIC_VECTOR (13 downto 0);
    r_3_shift_reg_V_o : OUT STD_LOGIC_VECTOR (13 downto 0);
    r_3_shift_reg_V_o_ap_vld : OUT STD_LOGIC;
    r_0_peak_reg_V_read : IN STD_LOGIC_VECTOR (18 downto 0);
    ap_return_0 : OUT STD_LOGIC_VECTOR (15 downto 0);
    ap_return_1 : OUT STD_LOGIC_VECTOR (18 downto 0) );
end;


architecture behav of TPG is 
    constant ap_const_logic_1 : STD_LOGIC := '1';
    constant ap_const_logic_0 : STD_LOGIC := '0';
    constant ap_ST_fsm_pp0_stage0 : STD_LOGIC_VECTOR (0 downto 0) := "1";
    constant ap_const_lv32_0 : STD_LOGIC_VECTOR (31 downto 0) := "00000000000000000000000000000000";
    constant ap_const_lv1_1 : STD_LOGIC_VECTOR (0 downto 0) := "1";
    constant ap_const_lv32_7 : STD_LOGIC_VECTOR (31 downto 0) := "00000000000000000000000000000111";
    constant ap_const_lv32_14 : STD_LOGIC_VECTOR (31 downto 0) := "00000000000000000000000000010100";
    constant ap_const_lv32_6 : STD_LOGIC_VECTOR (31 downto 0) := "00000000000000000000000000000110";
    constant ap_const_lv32_18 : STD_LOGIC_VECTOR (31 downto 0) := "00000000000000000000000000011000";
    constant ap_const_lv32_2 : STD_LOGIC_VECTOR (31 downto 0) := "00000000000000000000000000000010";
    constant ap_const_lv32_D : STD_LOGIC_VECTOR (31 downto 0) := "00000000000000000000000000001101";
    constant ap_const_lv32_C : STD_LOGIC_VECTOR (31 downto 0) := "00000000000000000000000000001100";
    constant ap_const_lv32_12 : STD_LOGIC_VECTOR (31 downto 0) := "00000000000000000000000000010010";
    constant ap_const_lv7_0 : STD_LOGIC_VECTOR (6 downto 0) := "0000000";
    constant ap_const_lv5_0 : STD_LOGIC_VECTOR (4 downto 0) := "00000";
    constant ap_const_lv24_0 : STD_LOGIC_VECTOR (23 downto 0) := "000000000000000000000000";
    constant ap_const_lv2_0 : STD_LOGIC_VECTOR (1 downto 0) := "00";
    constant ap_const_lv32_17 : STD_LOGIC_VECTOR (31 downto 0) := "00000000000000000000000000010111";
    constant ap_const_lv3_0 : STD_LOGIC_VECTOR (2 downto 0) := "000";
    constant ap_const_lv19_0 : STD_LOGIC_VECTOR (18 downto 0) := "0000000000000000000";
    constant ap_const_lv32_11 : STD_LOGIC_VECTOR (31 downto 0) := "00000000000000000000000000010001";
    constant ap_const_lv16_3FF : STD_LOGIC_VECTOR (15 downto 0) := "0000001111111111";
    constant ap_const_lv16_0 : STD_LOGIC_VECTOR (15 downto 0) := "0000000000000000";
    constant ap_const_lv13_1F96 : STD_LOGIC_VECTOR (12 downto 0) := "1111110010110";
    constant ap_const_lv21_B7 : STD_LOGIC_VECTOR (20 downto 0) := "000000000000010110111";
    constant ap_const_lv25_1FFFFDD : STD_LOGIC_VECTOR (24 downto 0) := "1111111111111111111011101";

    signal ap_CS_fsm : STD_LOGIC_VECTOR (0 downto 0) := "1";
    attribute fsm_encoding : string;
    attribute fsm_encoding of ap_CS_fsm : signal is "none";
    signal ap_CS_fsm_pp0_stage0 : STD_LOGIC_VECTOR (0 downto 0);
    attribute fsm_encoding of ap_CS_fsm_pp0_stage0 : signal is "none";
    signal ap_enable_reg_pp0_iter0 : STD_LOGIC;
    signal ap_enable_reg_pp0_iter1 : STD_LOGIC := '0';
    signal ap_enable_reg_pp0_iter2 : STD_LOGIC := '0';
    signal r_0_peak_reg_V_read_1_reg_460 : STD_LOGIC_VECTOR (18 downto 0);
    signal ap_pipeline_reg_pp0_iter1_r_0_peak_reg_V_read_1_reg_460 : STD_LOGIC_VECTOR (18 downto 0);
    signal tmp_s_reg_467 : STD_LOGIC_VECTOR (13 downto 0);
    signal r_3_shift_reg_V_rea_reg_473 : STD_LOGIC_VECTOR (13 downto 0);
    signal r_0_shift_reg_V_rea_reg_479 : STD_LOGIC_VECTOR (13 downto 0);
    signal mul_V_reg_485 : STD_LOGIC_VECTOR (18 downto 0);
    signal tmp_6_reg_490 : STD_LOGIC_VECTOR (11 downto 0);
    signal icmp_fu_210_p2 : STD_LOGIC_VECTOR (0 downto 0);
    signal icmp_reg_495 : STD_LOGIC_VECTOR (0 downto 0);
    signal ap_pipeline_reg_pp0_iter1_icmp_reg_495 : STD_LOGIC_VECTOR (0 downto 0);
    signal r_0_peak_reg_V_writ_fu_388_p2 : STD_LOGIC_VECTOR (18 downto 0);
    signal r_0_peak_reg_V_writ_reg_500 : STD_LOGIC_VECTOR (18 downto 0);
    signal uncorrectedADC_V_fu_155_p1 : STD_LOGIC_VECTOR (11 downto 0);
    signal grp_fu_444_p3 : STD_LOGIC_VECTOR (20 downto 0);
    signal extLd3_fu_173_p1 : STD_LOGIC_VECTOR (17 downto 0);
    signal r_V_4_fu_453_p2 : STD_LOGIC_VECTOR (24 downto 0);
    signal tmp_15_fu_200_p4 : STD_LOGIC_VECTOR (6 downto 0);
    signal tmp_11_fu_219_p3 : STD_LOGIC_VECTOR (18 downto 0);
    signal p_shl_fu_226_p1 : STD_LOGIC_VECTOR (22 downto 0);
    signal p_shl_cast_fu_230_p1 : STD_LOGIC_VECTOR (23 downto 0);
    signal p_neg_fu_234_p2 : STD_LOGIC_VECTOR (23 downto 0);
    signal tmp_14_fu_244_p3 : STD_LOGIC_VECTOR (15 downto 0);
    signal p_shl1_fu_251_p1 : STD_LOGIC_VECTOR (19 downto 0);
    signal p_neg_cast_fu_240_p1 : STD_LOGIC_VECTOR (24 downto 0);
    signal p_shl1_cast_fu_255_p1 : STD_LOGIC_VECTOR (24 downto 0);
    signal r_V_2_fu_259_p2 : STD_LOGIC_VECTOR (24 downto 0);
    signal tmp_7_fu_275_p1 : STD_LOGIC_VECTOR (15 downto 0);
    signal extLd_fu_216_p1 : STD_LOGIC_VECTOR (17 downto 0);
    signal tmp_fu_286_p3 : STD_LOGIC_VECTOR (18 downto 0);
    signal p_shl2_fu_293_p1 : STD_LOGIC_VECTOR (22 downto 0);
    signal p_shl2_cast_fu_297_p1 : STD_LOGIC_VECTOR (23 downto 0);
    signal lhs_V_4_2_cast7_fu_282_p1 : STD_LOGIC_VECTOR (23 downto 0);
    signal r_V_4_2_fu_301_p2 : STD_LOGIC_VECTOR (23 downto 0);
    signal tmp_9_fu_307_p4 : STD_LOGIC_VECTOR (17 downto 0);
    signal tmp_4_fu_321_p3 : STD_LOGIC_VECTOR (18 downto 0);
    signal p_shl3_fu_328_p1 : STD_LOGIC_VECTOR (22 downto 0);
    signal tmp_5_fu_336_p3 : STD_LOGIC_VECTOR (16 downto 0);
    signal p_shl4_fu_343_p1 : STD_LOGIC_VECTOR (20 downto 0);
    signal p_shl3_cast_fu_332_p1 : STD_LOGIC_VECTOR (23 downto 0);
    signal p_shl4_cast_fu_347_p1 : STD_LOGIC_VECTOR (23 downto 0);
    signal r_V_4_3_fu_351_p2 : STD_LOGIC_VECTOR (23 downto 0);
    signal tmp_12_fu_357_p4 : STD_LOGIC_VECTOR (17 downto 0);
    signal tmp_22_1_cast_fu_278_p1 : STD_LOGIC_VECTOR (18 downto 0);
    signal tmp_10_fu_317_p1 : STD_LOGIC_VECTOR (18 downto 0);
    signal tmp_529_fu_265_p4 : STD_LOGIC_VECTOR (18 downto 0);
    signal tmp_13_fu_367_p1 : STD_LOGIC_VECTOR (18 downto 0);
    signal tmp5_fu_377_p2 : STD_LOGIC_VECTOR (18 downto 0);
    signal tmp4_fu_383_p2 : STD_LOGIC_VECTOR (18 downto 0);
    signal tmp3_fu_371_p2 : STD_LOGIC_VECTOR (18 downto 0);
    signal tmp_1_fu_394_p2 : STD_LOGIC_VECTOR (0 downto 0);
    signal tmp_2_fu_398_p2 : STD_LOGIC_VECTOR (0 downto 0);
    signal tmp_8_fu_409_p4 : STD_LOGIC_VECTOR (15 downto 0);
    signal or_cond_fu_403_p2 : STD_LOGIC_VECTOR (0 downto 0);
    signal tmpPeak_V_fu_418_p3 : STD_LOGIC_VECTOR (15 downto 0);
    signal agg_result_V_1_fu_425_p3 : STD_LOGIC_VECTOR (15 downto 0);
    signal grp_fu_444_p0 : STD_LOGIC_VECTOR (7 downto 0);
    signal grp_fu_444_p1 : STD_LOGIC_VECTOR (11 downto 0);
    signal grp_fu_444_p2 : STD_LOGIC_VECTOR (8 downto 0);
    signal r_V_4_fu_453_p0 : STD_LOGIC_VECTOR (6 downto 0);
    signal r_V_4_fu_453_p1 : STD_LOGIC_VECTOR (17 downto 0);
    signal ap_NS_fsm : STD_LOGIC_VECTOR (0 downto 0);
    signal ap_pipeline_idle_pp0 : STD_LOGIC;
    signal ap_pipeline_start_pp0 : STD_LOGIC;
    signal grp_fu_444_p10 : STD_LOGIC_VECTOR (12 downto 0);
    signal r_V_4_fu_453_p10 : STD_LOGIC_VECTOR (24 downto 0);

    component algo_unpacked_am_bkb IS
    generic (
        ID : INTEGER;
        NUM_STAGE : INTEGER;
        din0_WIDTH : INTEGER;
        din1_WIDTH : INTEGER;
        din2_WIDTH : INTEGER;
        dout_WIDTH : INTEGER );
    port (
        din0 : IN STD_LOGIC_VECTOR (7 downto 0);
        din1 : IN STD_LOGIC_VECTOR (11 downto 0);
        din2 : IN STD_LOGIC_VECTOR (8 downto 0);
        dout : OUT STD_LOGIC_VECTOR (20 downto 0) );
    end component;


    component algo_unpacked_mulcud IS
    generic (
        ID : INTEGER;
        NUM_STAGE : INTEGER;
        din0_WIDTH : INTEGER;
        din1_WIDTH : INTEGER;
        dout_WIDTH : INTEGER );
    port (
        din0 : IN STD_LOGIC_VECTOR (6 downto 0);
        din1 : IN STD_LOGIC_VECTOR (17 downto 0);
        dout : OUT STD_LOGIC_VECTOR (24 downto 0) );
    end component;



begin
    algo_unpacked_am_bkb_U1 : component algo_unpacked_am_bkb
    generic map (
        ID => 1,
        NUM_STAGE => 1,
        din0_WIDTH => 8,
        din1_WIDTH => 12,
        din2_WIDTH => 9,
        dout_WIDTH => 21)
    port map (
        din0 => grp_fu_444_p0,
        din1 => grp_fu_444_p1,
        din2 => grp_fu_444_p2,
        dout => grp_fu_444_p3);

    algo_unpacked_mulcud_U2 : component algo_unpacked_mulcud
    generic map (
        ID => 1,
        NUM_STAGE => 1,
        din0_WIDTH => 7,
        din1_WIDTH => 18,
        dout_WIDTH => 25)
    port map (
        din0 => r_V_4_fu_453_p0,
        din1 => r_V_4_fu_453_p1,
        dout => r_V_4_fu_453_p2);





    ap_CS_fsm_assign_proc : process(ap_clk)
    begin
        if (ap_clk'event and ap_clk =  '1') then
            if (ap_rst = '1') then
                ap_CS_fsm <= ap_ST_fsm_pp0_stage0;
            else
                ap_CS_fsm <= ap_NS_fsm;
            end if;
        end if;
    end process;


    ap_enable_reg_pp0_iter1_assign_proc : process(ap_clk)
    begin
        if (ap_clk'event and ap_clk =  '1') then
            if (ap_rst = '1') then
                ap_enable_reg_pp0_iter1 <= ap_const_logic_0;
            else
                if (((ap_CS_fsm_pp0_stage0 = ap_const_lv1_1) and not((((ap_const_logic_1 = ap_enable_reg_pp0_iter0) and (ap_start = ap_const_logic_0)) or not((ap_const_logic_1 = ap_ce)))))) then 
                    ap_enable_reg_pp0_iter1 <= ap_start;
                end if; 
            end if;
        end if;
    end process;


    ap_enable_reg_pp0_iter2_assign_proc : process(ap_clk)
    begin
        if (ap_clk'event and ap_clk =  '1') then
            if (ap_rst = '1') then
                ap_enable_reg_pp0_iter2 <= ap_const_logic_0;
            else
                if (not((((ap_const_logic_1 = ap_enable_reg_pp0_iter0) and (ap_start = ap_const_logic_0)) or not((ap_const_logic_1 = ap_ce))))) then 
                    ap_enable_reg_pp0_iter2 <= ap_enable_reg_pp0_iter1;
                end if; 
            end if;
        end if;
    end process;

    process (ap_clk)
    begin
        if (ap_clk'event and ap_clk = '1') then
            if (((ap_CS_fsm_pp0_stage0 = ap_const_lv1_1) and not(((ap_const_logic_1 = ap_enable_reg_pp0_iter0) and (ap_start = ap_const_logic_0))) and (ap_const_logic_1 = ap_ce))) then
                ap_pipeline_reg_pp0_iter1_icmp_reg_495 <= icmp_reg_495;
                ap_pipeline_reg_pp0_iter1_r_0_peak_reg_V_read_1_reg_460 <= r_0_peak_reg_V_read_1_reg_460;
                icmp_reg_495 <= icmp_fu_210_p2;
                mul_V_reg_485 <= r_V_4_fu_453_p2(24 downto 6);
                r_0_peak_reg_V_read_1_reg_460 <= r_0_peak_reg_V_read;
                r_0_peak_reg_V_writ_reg_500 <= r_0_peak_reg_V_writ_fu_388_p2;
                r_0_shift_reg_V_rea_reg_479 <= r_0_shift_reg_V_i;
                r_3_shift_reg_V_rea_reg_473 <= r_3_shift_reg_V_i;
                tmp_6_reg_490 <= r_1_shift_reg_V_i(13 downto 2);
                tmp_s_reg_467 <= grp_fu_444_p3(20 downto 7);
            end if;
        end if;
    end process;

    ap_NS_fsm_assign_proc : process (ap_start, ap_CS_fsm, ap_enable_reg_pp0_iter0, ap_ce, ap_pipeline_idle_pp0, ap_pipeline_start_pp0)
    begin
        case ap_CS_fsm is
            when ap_ST_fsm_pp0_stage0 => 
                ap_NS_fsm <= ap_ST_fsm_pp0_stage0;
            when others =>  
                ap_NS_fsm <= "X";
        end case;
    end process;
    agg_result_V_1_fu_425_p3 <= 
        tmpPeak_V_fu_418_p3 when (or_cond_fu_403_p2(0) = '1') else 
        ap_const_lv16_0;
    ap_CS_fsm_pp0_stage0 <= ap_CS_fsm(0 downto 0);

    ap_done_assign_proc : process(ap_start, ap_CS_fsm_pp0_stage0, ap_enable_reg_pp0_iter0, ap_enable_reg_pp0_iter2, ap_ce)
    begin
        if ((((ap_const_logic_0 = ap_start) and (ap_CS_fsm_pp0_stage0 = ap_const_lv1_1) and (ap_const_logic_1 = ap_enable_reg_pp0_iter0)) or (not(((ap_const_logic_1 = ap_enable_reg_pp0_iter0) and (ap_start = ap_const_logic_0))) and (ap_const_logic_1 = ap_ce) and (ap_const_logic_1 = ap_enable_reg_pp0_iter2)))) then 
            ap_done <= ap_const_logic_1;
        else 
            ap_done <= ap_const_logic_0;
        end if; 
    end process;

    ap_enable_reg_pp0_iter0 <= ap_start;

    ap_idle_assign_proc : process(ap_start, ap_CS_fsm_pp0_stage0, ap_enable_reg_pp0_iter0, ap_enable_reg_pp0_iter1, ap_enable_reg_pp0_iter2)
    begin
        if (((ap_const_logic_0 = ap_start) and (ap_CS_fsm_pp0_stage0 = ap_const_lv1_1) and (ap_const_logic_0 = ap_enable_reg_pp0_iter0) and (ap_const_logic_0 = ap_enable_reg_pp0_iter1) and (ap_const_logic_0 = ap_enable_reg_pp0_iter2))) then 
            ap_idle <= ap_const_logic_1;
        else 
            ap_idle <= ap_const_logic_0;
        end if; 
    end process;


    ap_pipeline_idle_pp0_assign_proc : process(ap_start, ap_enable_reg_pp0_iter0, ap_enable_reg_pp0_iter1)
    begin
        if (((ap_const_logic_0 = ap_start) and (ap_const_logic_0 = ap_enable_reg_pp0_iter0) and (ap_const_logic_0 = ap_enable_reg_pp0_iter1))) then 
            ap_pipeline_idle_pp0 <= ap_const_logic_1;
        else 
            ap_pipeline_idle_pp0 <= ap_const_logic_0;
        end if; 
    end process;


    ap_pipeline_start_pp0_assign_proc : process(ap_start, ap_enable_reg_pp0_iter0, ap_enable_reg_pp0_iter1)
    begin
        if (((ap_const_logic_0 = ap_enable_reg_pp0_iter0) and (ap_const_logic_0 = ap_enable_reg_pp0_iter1) and (ap_const_logic_1 = ap_start))) then 
            ap_pipeline_start_pp0 <= ap_const_logic_1;
        else 
            ap_pipeline_start_pp0 <= ap_const_logic_0;
        end if; 
    end process;


    ap_ready_assign_proc : process(ap_start, ap_CS_fsm_pp0_stage0, ap_enable_reg_pp0_iter0, ap_ce)
    begin
        if (((ap_CS_fsm_pp0_stage0 = ap_const_lv1_1) and (ap_const_logic_1 = ap_enable_reg_pp0_iter0) and not(((ap_const_logic_1 = ap_enable_reg_pp0_iter0) and (ap_start = ap_const_logic_0))) and (ap_const_logic_1 = ap_ce))) then 
            ap_ready <= ap_const_logic_1;
        else 
            ap_ready <= ap_const_logic_0;
        end if; 
    end process;

    ap_return_0 <= agg_result_V_1_fu_425_p3;
    ap_return_1 <= r_0_peak_reg_V_writ_reg_500;
        extLd3_fu_173_p1 <= std_logic_vector(resize(signed(r_2_shift_reg_V_i),18));

        extLd_fu_216_p1 <= std_logic_vector(resize(signed(r_0_shift_reg_V_rea_reg_479),18));

    grp_fu_444_p0 <= ap_const_lv13_1F96(8 - 1 downto 0);
    grp_fu_444_p1 <= grp_fu_444_p10(12 - 1 downto 0);
    grp_fu_444_p10 <= std_logic_vector(resize(unsigned(uncorrectedADC_V_fu_155_p1),13));
    grp_fu_444_p2 <= ap_const_lv21_B7(9 - 1 downto 0);
    icmp_fu_210_p2 <= "1" when (signed(tmp_15_fu_200_p4) > signed(ap_const_lv7_0)) else "0";
    lhs_V_4_2_cast7_fu_282_p1 <= std_logic_vector(resize(unsigned(extLd_fu_216_p1),24));
    or_cond_fu_403_p2 <= (tmp_1_fu_394_p2 and tmp_2_fu_398_p2);
        p_neg_cast_fu_240_p1 <= std_logic_vector(resize(signed(p_neg_fu_234_p2),25));

    p_neg_fu_234_p2 <= std_logic_vector(unsigned(ap_const_lv24_0) - unsigned(p_shl_cast_fu_230_p1));
    p_shl1_cast_fu_255_p1 <= std_logic_vector(resize(unsigned(p_shl1_fu_251_p1),25));
        p_shl1_fu_251_p1 <= std_logic_vector(resize(signed(tmp_14_fu_244_p3),20));

    p_shl2_cast_fu_297_p1 <= std_logic_vector(resize(unsigned(p_shl2_fu_293_p1),24));
        p_shl2_fu_293_p1 <= std_logic_vector(resize(signed(tmp_fu_286_p3),23));

    p_shl3_cast_fu_332_p1 <= std_logic_vector(resize(unsigned(p_shl3_fu_328_p1),24));
        p_shl3_fu_328_p1 <= std_logic_vector(resize(signed(tmp_4_fu_321_p3),23));

    p_shl4_cast_fu_347_p1 <= std_logic_vector(resize(unsigned(p_shl4_fu_343_p1),24));
        p_shl4_fu_343_p1 <= std_logic_vector(resize(signed(tmp_5_fu_336_p3),21));

    p_shl_cast_fu_230_p1 <= std_logic_vector(resize(unsigned(p_shl_fu_226_p1),24));
        p_shl_fu_226_p1 <= std_logic_vector(resize(signed(tmp_11_fu_219_p3),23));

    r_0_peak_reg_V_writ_fu_388_p2 <= std_logic_vector(unsigned(tmp4_fu_383_p2) + unsigned(tmp3_fu_371_p2));
    r_0_shift_reg_V_o <= grp_fu_444_p3(20 downto 7);

    r_0_shift_reg_V_o_ap_vld_assign_proc : process(ap_start, ap_CS_fsm_pp0_stage0, ap_enable_reg_pp0_iter0, ap_ce)
    begin
        if (((ap_CS_fsm_pp0_stage0 = ap_const_lv1_1) and (ap_const_logic_1 = ap_enable_reg_pp0_iter0) and not(((ap_const_logic_1 = ap_enable_reg_pp0_iter0) and (ap_start = ap_const_logic_0))) and (ap_const_logic_1 = ap_ce))) then 
            r_0_shift_reg_V_o_ap_vld <= ap_const_logic_1;
        else 
            r_0_shift_reg_V_o_ap_vld <= ap_const_logic_0;
        end if; 
    end process;

    r_1_shift_reg_V_o <= r_0_shift_reg_V_i;

    r_1_shift_reg_V_o_ap_vld_assign_proc : process(ap_start, ap_CS_fsm_pp0_stage0, ap_enable_reg_pp0_iter0, ap_ce)
    begin
        if (((ap_CS_fsm_pp0_stage0 = ap_const_lv1_1) and (ap_const_logic_1 = ap_enable_reg_pp0_iter0) and not(((ap_const_logic_1 = ap_enable_reg_pp0_iter0) and (ap_start = ap_const_logic_0))) and (ap_const_logic_1 = ap_ce))) then 
            r_1_shift_reg_V_o_ap_vld <= ap_const_logic_1;
        else 
            r_1_shift_reg_V_o_ap_vld <= ap_const_logic_0;
        end if; 
    end process;

    r_2_shift_reg_V_o <= r_1_shift_reg_V_i;

    r_2_shift_reg_V_o_ap_vld_assign_proc : process(ap_start, ap_CS_fsm_pp0_stage0, ap_enable_reg_pp0_iter0, ap_ce)
    begin
        if (((ap_CS_fsm_pp0_stage0 = ap_const_lv1_1) and (ap_const_logic_1 = ap_enable_reg_pp0_iter0) and not(((ap_const_logic_1 = ap_enable_reg_pp0_iter0) and (ap_start = ap_const_logic_0))) and (ap_const_logic_1 = ap_ce))) then 
            r_2_shift_reg_V_o_ap_vld <= ap_const_logic_1;
        else 
            r_2_shift_reg_V_o_ap_vld <= ap_const_logic_0;
        end if; 
    end process;

    r_3_shift_reg_V_o <= r_2_shift_reg_V_i;

    r_3_shift_reg_V_o_ap_vld_assign_proc : process(ap_start, ap_CS_fsm_pp0_stage0, ap_enable_reg_pp0_iter0, ap_ce)
    begin
        if (((ap_CS_fsm_pp0_stage0 = ap_const_lv1_1) and (ap_const_logic_1 = ap_enable_reg_pp0_iter0) and not(((ap_const_logic_1 = ap_enable_reg_pp0_iter0) and (ap_start = ap_const_logic_0))) and (ap_const_logic_1 = ap_ce))) then 
            r_3_shift_reg_V_o_ap_vld <= ap_const_logic_1;
        else 
            r_3_shift_reg_V_o_ap_vld <= ap_const_logic_0;
        end if; 
    end process;

    r_V_2_fu_259_p2 <= std_logic_vector(signed(p_neg_cast_fu_240_p1) - signed(p_shl1_cast_fu_255_p1));
    r_V_4_2_fu_301_p2 <= std_logic_vector(unsigned(p_shl2_cast_fu_297_p1) - unsigned(lhs_V_4_2_cast7_fu_282_p1));
    r_V_4_3_fu_351_p2 <= std_logic_vector(unsigned(p_shl3_cast_fu_332_p1) - unsigned(p_shl4_cast_fu_347_p1));
    r_V_4_fu_453_p0 <= ap_const_lv25_1FFFFDD(7 - 1 downto 0);
    r_V_4_fu_453_p1 <= r_V_4_fu_453_p10(18 - 1 downto 0);
    r_V_4_fu_453_p10 <= std_logic_vector(resize(unsigned(extLd3_fu_173_p1),25));
    tmp3_fu_371_p2 <= std_logic_vector(unsigned(tmp_22_1_cast_fu_278_p1) + unsigned(tmp_10_fu_317_p1));
    tmp4_fu_383_p2 <= std_logic_vector(unsigned(tmp5_fu_377_p2) + unsigned(mul_V_reg_485));
    tmp5_fu_377_p2 <= std_logic_vector(unsigned(tmp_529_fu_265_p4) + unsigned(tmp_13_fu_367_p1));
    tmpPeak_V_fu_418_p3 <= 
        ap_const_lv16_3FF when (ap_pipeline_reg_pp0_iter1_icmp_reg_495(0) = '1') else 
        tmp_8_fu_409_p4;
        tmp_10_fu_317_p1 <= std_logic_vector(resize(signed(tmp_9_fu_307_p4),19));

    tmp_11_fu_219_p3 <= (r_3_shift_reg_V_rea_reg_473 & ap_const_lv5_0);
    tmp_12_fu_357_p4 <= r_V_4_3_fu_351_p2(23 downto 6);
        tmp_13_fu_367_p1 <= std_logic_vector(resize(signed(tmp_12_fu_357_p4),19));

    tmp_14_fu_244_p3 <= (r_3_shift_reg_V_rea_reg_473 & ap_const_lv2_0);
    tmp_15_fu_200_p4 <= r_0_peak_reg_V_read(18 downto 12);
    tmp_1_fu_394_p2 <= "1" when (signed(r_0_peak_reg_V_writ_reg_500) < signed(ap_pipeline_reg_pp0_iter1_r_0_peak_reg_V_read_1_reg_460)) else "0";
    tmp_22_1_cast_fu_278_p1 <= std_logic_vector(resize(unsigned(tmp_7_fu_275_p1),19));
    tmp_2_fu_398_p2 <= "1" when (signed(ap_pipeline_reg_pp0_iter1_r_0_peak_reg_V_read_1_reg_460) > signed(ap_const_lv19_0)) else "0";
    tmp_4_fu_321_p3 <= (tmp_s_reg_467 & ap_const_lv5_0);
    tmp_529_fu_265_p4 <= r_V_2_fu_259_p2(24 downto 6);
    tmp_5_fu_336_p3 <= (tmp_s_reg_467 & ap_const_lv3_0);
        tmp_7_fu_275_p1 <= std_logic_vector(resize(signed(tmp_6_reg_490),16));

    tmp_8_fu_409_p4 <= ap_pipeline_reg_pp0_iter1_r_0_peak_reg_V_read_1_reg_460(17 downto 2);
    tmp_9_fu_307_p4 <= r_V_4_2_fu_301_p2(23 downto 6);
    tmp_fu_286_p3 <= (r_0_shift_reg_V_rea_reg_479 & ap_const_lv5_0);
    uncorrectedADC_V_fu_155_p1 <= data_int_V(12 - 1 downto 0);
end behav;