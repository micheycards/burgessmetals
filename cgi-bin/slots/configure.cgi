#!/usr/bin/perl
####################################################################################################
# SLOT MACHINE		 		                       		Version 2.0                            
# Copyright 2000  Telecore Media International, Inc.			webmaster@superscripts.com                 
# Created 8/9/99                                      		Last Modified 1/12/00                           
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

sub configure {
############################################################
#  REQUIRED CONFIGURATION AREA
############################################################


$slotcgi = "/cgi-bin/slots/slot.cgi";


$localurl = "www.micheycards.com";


$width=100;


$height=100;


$title = "THE SLOT MACHINE";


$odds = 10000;



$imgdir = "/public_html/cgi-bin/slots/images";


$mailinglist = "/public_html/cgi-bin/slots/emails";


$mailprogram = "/usr/sbin/sendmail";


$adminemail = "micheycards@gmail.com";


$subject = "YOU WON!";


$cookieblock = "perm"; # temp or perm block
############################################################
#  OPTIONAL CONFIGURATION AREA
############################################################
#===============================================
$img[0] = "0.gif";
$img[1] = "1.gif";
$img[2] = "2.gif";
$img[3] = "3.gif";
$img[4] = "4.gif";
$img[5] = "5.gif";
$img[6] = "6.gif";
$img[7] = "7.gif";
$img[8] = "8.gif";
$img[9] = "9.gif";
#===============================================
$link[0] = "http://www.infoready.net/";
$link[1] = "http://www.infoready.net/";
$link[2] = "http://www.infoready.net/";
$link[3] = "http://www.infoready.net/";
$link[4] = "http://www.infoready.net/";
$link[5] = "http://www.infoready.net/";
$link[6] = "http://www.infoready.net/";
$link[7] = "http://www.infoready.net/";
$link[8] = "http://www.infoready.net/";
$link[9] = "http://www.infoready.net/";
#===============================================
$product[0] = "One Free Copy of The Slot Machine Script";
$product[1] = "One Free Copy of The Slot Machine Script";
$product[2] = "One Free Copy of The Slot Machine Script";
$product[3] = "One Free Copy of The Slot Machine Script";
$product[4] = "One Free Copy of The Slot Machine Script";
$product[5] = "One Free Copy of The Slot Machine Script";
$product[6] = "One Free Copy of The Slot Machine Script";
$product[7] = "One Free Copy of The Slot Machine Script";
$product[8] = "One Free Copy of The Slot Machine Script";
$product[9] = "One Free Copy of The Slot Machine Script";
}
1;    #  Return true


