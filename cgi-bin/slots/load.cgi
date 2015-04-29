#!/usr/bin/perl
####################################################################################################
# SLOT MACHINE		 		                       		Version 2.0                            
# Copyright 2000  Telecore Media International, Inc.			webmaster@superscripts.com                 
# Created 8/9/99                                      		Last Modified 2/12/00                           
####################################################################################################
# COPYRIGHT NOTICE                                                           
# Copyright 2000 Telecore Media International, INC - All Rights Reserved.                    
# http://www.superscripts.com                                                                                                            
# Selling the code for this program, modifying or redistributing this software over the Internet or 
# in any other medium is forbidden.  Copyright and header may not be modified
#
# My name is drew star... and i am funky...  http://www.drewstar.com/
#
####################################################################################################

require "configure.cgi";
&configure;
############################################################
#  MAIN ROUTINE
############################################################
&rollthedice;
&dumpslot;
exit;
############################################################
#  MAKE SLOT MACHINE HTML
############################################################
sub dumpslot {
print <<ENDSLOT;

<div align="center"><center>

<table border="3" width="50%" bordercolor="#000000" bordercolordark="#000000">
  <tr>
    <td width="25%"><img src="$imgdir/$img[$rollthedice1]" width="104" height="104"></td>
    <td width="25%"><img src="$imgdir/$img[$rollthedice2]" width="104" height="104"></td>
    <td width="25%"><img src="$imgdir/$img[$rollthedice3]" width="104" height="104"></td>
    <td width="25%"><form action="$slotcgi" method="post">
      <div align="center"><center><p><input TYPE="text" NAME="email" size="20"> <input
      type="submit" value="SPIN"></p>
      </center></div>
    </form>
    </td>
  </tr>
</table>




<a
href="http://www.superscripts.com/" style="text-decoration: underline"><small><small><font face="Arial" color="#000000">custom cgi
by drew star</small></small></a></font></p>

</center></div>&nbsp;

ENDSLOT

}
############################################################
#  GENERATE RESULTS
############################################################
sub rollthedice {
$rollthedice1="0";
$rollthedice2="0";
$rollthedice3="0";

srand;
$winner=(int(rand($odds)));

if ($winner eq "0"){
$rollthedice1 = "9";
$rollthedice2 = "9";
$rollthedice3 = "9";
dumpslot;
exit;
}

while ($rollthedice1 eq "0"){
srand;
$rollthedice1=(int(rand(10)));
}
while ($rollthedice2 eq "0"){
srand;
$rollthedice2=(int(rand(10)));
}
while ($rollthedice3 eq "0"){
srand;
$rollthedice3=(int(rand(10)));
}
}
############################################################
#  DATE ROUTINE
############################################################
sub getdate {            
chop($date = &ctime(time));
($weekday,$month,$day,$time,$zone,$year,$yyear)=split(/ /,$date);

if ($day eq ""){
$day = $time;
}

$thedate = "Date: $weekday, $day $month $yyear $zone";
print "$thedate\n";

}
############################################################
#  TIME ROUTINE
############################################################
sub ctime {

    @DoW = ('Sun','Mon','Tue','Wed','Thu','Fri','Sat');
    @MoY = ('Jan','Feb','Mar','Apr','May','Jun',
	    'Jul','Aug','Sep','Oct','Nov','Dec');

    local($time) = @_;
    local($[) = 0;
    local($sec, $min, $hour, $mday, $mon, $year, $wday, $yday, $isdst);

    $TZ = defined($ENV{'TZ'}) ? ( $ENV{'TZ'} ? $ENV{'TZ'} : 'GMT' ) : '';
    ($sec, $min, $hour, $mday, $mon, $year, $wday, $yday, $isdst) =
        ($TZ eq 'GMT') ? gmtime($time) : localtime($time);

    if($TZ=~/^([^:\d+\-,]{3,})([+-]?\d{1,2}(:\d{1,2}){0,2})([^\d+\-,]{3,})?/){
        $TZ = $isdst ? $4 : $1;
    }
    $TZ .= ' ' unless $TZ eq '';

    $year += 1900;
    sprintf("%s %s %2d %2d:%02d:%02d %s%4d\n",
      $DoW[$wday], $MoY[$mon], $mday, $hour, $min, $sec, $TZ, $year);
}
############################################################
#  FORM PARSE
############################################################
sub form_parse  {
	read (STDIN, $buffer, $ENV{'CONTENT_LENGTH'});
	@pairs = split(/&/, $buffer);
	foreach $pair (@pairs)
	{
    	($name, $value) = split(/=/, $pair);
    	$value =~ tr/+/ /;
    	$value =~ s/%([a-fA-F0-9][a-fA-F0-9])/pack("C", hex($1))/eg;
    	$FORM{$name} = $value;
	}}
############################################################
#  VALIDATE POST IS AUTHENTIC
############################################################
sub refergate {            
         if ($ENV{'HTTP_REFERER'} =~ /$localurl/i) {
			$flag = "OK";
          }
        if ($flag ne "OK"){
          print "Content-Type: text/html\n\n";
          print "PERMISSION DENIED:  $ENV{'HTTP_REFERER'}";
          exit;
          }                 
}  