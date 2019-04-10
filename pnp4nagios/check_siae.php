<?php

$def[1] = '';
$def[2] = '';
$def[3] = '';
$def[4] = '';
$def[5] = '';

for ($i=1; $i <= count($DS); $i++) {
  switch($NAME[$i]) {
    case 'msr':
    case 'rx_power':
    case 'tx_power': $def[1] .= rrd::def($NAME[$i], $RRDFILE[1], $DS[$i]); break;
    case 'rx_data_rate':
    case 'tx_data_rate': $def[2] .= rrd::def($NAME[$i], $RRDFILE[1], $DS[$i]); break;
    case 'If_Radio__OperStatus': $def[3] .= rrd::def($NAME[$i], $RRDFILE[1], $DS[$i]); break;
    case 'If_Radio__OctetsIn':
    case 'If_Radio__OctetsOut': $def[4] .= rrd::def($NAME[$i], $RRDFILE[1], $DS[$i]); break;
    case 'If_Radio__ErrorsIn':
    case 'If_Radio__ErrorsOut': $def[5] .= rrd::def($NAME[$i], $RRDFILE[1], $DS[$i]); break;
  }
}

$ds_name[1] = 'Power Statistics';
$opt[1] = "--upper-limit 7 --lower-limit \"-67\" --vertical-label \"dB\"  --title $hostname";
$def[1] .= rrd::gradient("rx_power", "f0f0f0","21db2a", "RX Power");
$def[1] .= rrd::gprint("rx_power", array("LAST","MIN","MAX","AVERAGE"), "%5.1lf%Sdb");

$def[1] .= rrd::gradient("tx_power", "f0f0f0", "0000b0","TX Power");
$def[1] .= rrd::gprint("tx_power", array("LAST","MIN","MAX","AVERAGE"), "%5.1lf%Sdb");

$def[1] .= rrd::line1("msr", "#9121db", "MSR");
$def[1] .= rrd::gprint("msr", array("LAST","MIN","AVERAGE"), "%5.1lf%Sdb");

$ds_name[2] = 'Radio Data Rate';
$opt[2] = "--lower-limit \"0\" --vertical-label \"bps\" --title $hostname";
$def[2] .= rrd::cdef("rx_data_rate_redef", "1024,rx_data_rate,*");
$def[2] .= rrd::area("rx_data_rate_redef", "#32CD32", "RX Data Rate");
$def[2] .= rrd::gprint("rx_data_rate",  array("LAST","MIN","AVERAGE"), "%8.2lf%Sbps");

$def[2] .= rrd::line1("tx_data_rate", "#0000CD","TX Data Rate");
$def[2] .= rrd::gprint("tx_data_rate",  array("LAST","MIN","AVERAGE"), "%8.2lf%Sbps");

$ds_name[3] = 'Radio Operational status';
$opt[3] = "--vertical-label \"\" --title 'Radio Operational status' --y-grid none --units-length 8";
$def[3] .= rrd::ticker("If_Radio__OperStatus", 1.1, 2.1, 0.33,"ff","#00ff00","#ff0000","#ff8c00");

$ds_name[4] = 'Radio traffic';
$opt[4] = " --vertical-label \"bits/s\" -l 0 -b 1000 --slope-mode  --title \"Radio Traffic\" ";
$def[4] .= rrd::cdef("bits_in_redef", "If_Radio__OctetsIn,UN,PREV,If_Radio__OctetsIn,8,*,IF");
$def[4] .= rrd::area("bits_in_redef", "#32CD32", "RX traffic");
$def[4] .= rrd::gprint("bits_in_redef",  array("LAST","MAX","AVERAGE"), "%8.2lf%Sbps");
$def[4] .= rrd::cdef("bits_out_redef", "If_Radio__OctetsOut,UN,PREV,If_Radio__OctetsOut,8,*,IF");
$def[4] .= rrd::line1("bits_out_redef", "#0000CD", "TX traffic");
$def[4] .= rrd::gprint("bits_out_redef",  array("LAST","MAX","AVERAGE"), "%8.2lf%Sbps");
# Total values In
$def[4] .= rrd::vdef("total_in", "If_Radio__OctetsIn,TOTAL");
$def[4] .= "GPRINT:total_in:\"Total in %3.2lf %sB total\\n\" ";
# Total values out
$def[4] .= rrd::vdef("total_out", "If_Radio__OctetsOut,TOTAL");
$def[4] .= "GPRINT:total_out:\"Total out %3.2lf %sB total\\n\" ";

$ds_name[5] = 'Radio Error packets';
$opt[5] = " --vertical-label \"pkts/s\" -l 0 -b 1000 --title \"Radio Error packets\" ";
$def[5] .= rrd::area("If_Radio__ErrorsIn",      '#FFD700', 'In Errors              ');
$def[5] .= rrd::gprint("If_Radio__ErrorsIn", array("LAST","MAX","AVERAGE"), "%5.1lf%S");
$def[5] .= rrd::area("If_Radio__ErrorsOut",      '#FF8C00', 'Out Errors              ','STACK');
$def[5] .= rrd::gprint("If_Radio__ErrorsOut", array("LAST","MAX","AVERAGE"), "%5.1lf%S");

?>
