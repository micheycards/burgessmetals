#!/usr/bin/perl
####################################################################################################
# SLOT MACHINE		 		                       		Version 2.0                            
# Copyright 2000  Telecore Media International, Inc.			webmaster@superscripts.com                 
# Created 8/9/99                                      		Last Modified 3/2/00                           
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
&securitycheck;
&form_parse;
	$email=$FORM{'email'};
	$action=$FORM{'action'};


if ($action eq ""){

&cookiecheck;

print "Content-type: text/html\n\n";
&lookup;
&testmail;
open (MAILINGLIST, ">>$mailinglist");
flock(MAILINGLIST, 2);
print MAILINGLIST "$email\n";
flock(MAILINGLIST, 8);
close MAILINGLIST;
&rollthedice;
&dumpslot;
exit;
}

&rollthedice;
print "Content-type: text/html\n\n";
&dumpslot;
if ($rollthedice1 eq $rollthedice2){
if ($rollthedice2 eq $rollthedice3){
&youwon;
}}
exit;
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
srand;
$rollthedice1=(int(rand(10)));
$rollthedice2 = $rollthedice1;
$rollthedice3 = $rollthedice1;
$wflag = "$rollthedice1";
return;
}

while ($rollthedice1 eq "0"){
srand;
$rollthedice1=(int(rand(10)));
}
while ($rollthedice2 eq "0"){
srand;
$rollthedice2=(int(rand(10)));
}

while (($rollthedice3 eq "0") or ($rollthedice3 eq $rollthedice1)){
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
############################################################
#  SECURITY CHECKS
############################################################
sub securitycheck{
$security = "$ENV{'REQUEST_METHOD'}";
	if ($security ne "POST"){
	print "Content-type: text/html\n\n";
	print "$security NOT ALLOWED";
	exit;
	}
$host = "$ENV{'REMOTE_HOST'}";
$refer = "$ENV{'HTTP_REFERER'}";
&refergate;
}
############################################################
#  DISPLAY WINNER HTML
############################################################
sub youwon{
print <<ENDYOUWON;
<body bgcolor=#FFFFFF text=#000000>
<p align="center"><font face="Tahoma" color="#FF0000"><big><strong>YOU WON the $product[$wflag]!</strong></big></font></big></p>
ENDYOUWON
&notifywinner;
&notifyadmin;
exit;
}
############################################################
#  ERROR MESSAGE IF ALREADY PLAYED
############################################################
sub sorry{
print <<ENDSORRY;
<body bgcolor=#FFFFFF text=#000000>
Sorry but only one play is allowed.
ENDSORRY
exit;
}
############################################################
#  NOTIFY WINNER
############################################################
sub notifywinner{

open (MAIL, "| $mailprogram $email");
print MAIL "Reply-to: $adminemail\n";
print MAIL "From: $adminemail\n";
print MAIL "To: $email\n";

print MAIL "Subject: $subject\n\n";

print MAIL <<ENDNOTIFYWINNER;

CONGRATULATIONS!  

You WON the $product[$wflag]
from The Slot Machine! You will recieve information soon, on how to claim your prize.

ENDNOTIFYWINNER

close MAIL;

}
############################################################
#  NOTIFY WINNER
############################################################
sub notifyadmin{

open (MAIL, "| $mailprogram $adminemail");
print MAIL "Reply-to: $email\n";
print MAIL "From: $email\n";
print MAIL "To: $adminemail\n";

print MAIL "Subject: $subject\n\n";

print MAIL <<ENDNOTIFYADMIN;

The $product[$wflag] from our Slot Machine has been won!

ENDNOTIFYADMIN

close MAIL;

}
############################################################
#  MAKE SLOT MACHINE HTML
############################################################
sub dumpslot {
print <<ENDSLOT;
<body bgcolor="#ffffff" text="#000000">
</body>


<div align="center"><center>
<form action="$slotcgi" method="post">
<input type="hidden" name="email" value="$email">
<input type="hidden" name="action" value="spin">
<input type="submit" value="SPIN"></form>

<table border="6" width="10%" cellspacing="0" cellpadding="0">
  <tr>
    <td width="25%"><a href="$link[$rollthedice1]"><img src="$imgdir/$img[$rollthedice1]" width="$width" height="$height"></a></td>
    <td width="25%"><a href="$link[$rollthedice2]"><img src="$imgdir/$img[$rollthedice2]" width="$width" height="$height"></a></td>
    <td width="25%"><a href="$link[$rollthedice3]"><img src="$imgdir/$img[$rollthedice3]" width="$width" height="$height"></a></td>

    </td>
  </tr>
</table>
</center></div><div align="center">




<a href="http://www.superscripts.com/" style="text-decoration: underline"><small><small><font face="Tahoma" color="#C0C0C0">custom cgi
by drew star</small></small></a></font></p>

<p align="center"><font face="Tahoma">Click on the images for more information.</p>

ENDSLOT

}
############################################################
#  CHECK TO SEE IF ALREADY PLAYED
############################################################
sub cookiecheck {

print "Content-type: text/html\n";

if ($cookieblock eq "perm"){
print "Set-Cookie: lottery=check; path=/; expires=Mon, 01-Jan-2020 00:00:00 GMT\n";
}
if ($cookieblock eq "temp"){
print "Set-Cookie: lottery=check; path=/;\n";
}

$memberdatabase = "$datadirectory/memberdatabase";
$cookie="$ENV{'HTTP_COOKIE'}";
($trash,$status) = split(/lottery=/,$cookie);
if ($status=~ /;/){
($status,$trash) = split(/;/,$status);
}


if ($status eq "check"){
print "Content-type: text/html\n\n";
&sorry;
}
}
############################################################
#  BOGUS EMAIL?  DONT BOTHER
############################################################
sub testmail	{

$flag = "OK";
if (!($email =~ /\@/)){
print "INVALID EMAIL ADDRESS";
exit;
}

if (!($email =~ /\./)){
print "INVALID EMAIL ADDRESS";
exit;
}

if ($email eq ""){
print "INVALID EMAIL ADDRESS";
exit;
}

if (length ($email) < 6){
print "INVALID EMAIL ADDRESS";
exit;
}

}
############################################################
#  MAKE SURE EMAIL ADDRESS IS UNIQUE
############################################################
sub lookup	{
open (MAILINGLIST, "$mailinglist");
flock(MAILINGLIST, 2);
@emails=<MAILINGLIST>;
flock(MAILINGLIST, 8);
close MAILINGLIST;

foreach $emails(@emails)	{
chomp $emails;

if ($email eq $emails)	{
&sorry;
	exit;		}}}
