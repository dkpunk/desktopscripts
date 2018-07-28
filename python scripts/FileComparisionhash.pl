sub Usage
{
print "
#______________________________INFOSTART______________________________
#
# Script Name   : FileComparision.pl
# Version       : 1.0
# Written By    : Dinesh Kumar
# Written Date  : 29th March 2018
# Modification History  :
#                        
# Description   : Compares Ip and cobrant name in file a.csv and checks whelther the same exists in File b.csv and creates a new File with the values not found.
# Usage :
#       1) Without Substitute :  perl FileComparision.pl
# Example :
#       1) Without Substitute :  perl FileComparision.pl
# Dependencies   :
#       1)files a.csv,b.csv present in D:/files
#		2)Text::CSV module required to open and read the csv files
# Log File Path  : NA
#______________________________INFOEND________________________________\n";
exit;
}
if($ARGV[0] eq '--help')
{

	Usage();
}



$filename1 = 'D:/files/b.csv';
$filename2 = 'D:/files/a_new.csv';
$fileout = 'D:/files/output.txt';

use Text::CSV;
use Data::Dumper;
%data1=();
%data2=();

#######################Hash for file a######################
$csv2=Text::CSV->new({sep_char => ','});
open($fh2,"<",$filename2) or die "Failed to open";
while(my $line2 = <$fh2>)
{
if($csv2->parse($line2))
{
	@fields2 =$csv2->fields();
	@ARR2=split(" ",$fields2[0]);
	#print "Cient : $ARR[3]  Ip address : $ARR[-10]";
	#print " fields[-10] , $fields[3] \n";
	#if($data2{$ARR2[-10]} != $ARR2[3])
	#{
	#push(@{$data2{$ARR2[-10]}}, $ARR2[3]);
	#}
	#else
	#{
	#	my @array = [];
	#	push(@array,$ARR2[3]);
	#	$data2{$ARR2[-10]}=\@array;
	#}
	if($data2{$ARR2[-10]}=$ARR2[3])
	{
		$data2{$ARR[-10]}++;
	}
	else
	{
		$data2{$ARR2[-10]}={$ARR2[3] => 1};
	}
}
else
{
print "could not parse lines";
}
}
print Dumper(\%data2);
############Hash for file b##############################

$csv1=Text::CSV->new({sep_char => ' '});
open($fh1,"<",$filename1) or die "Failed to open";
while(my $line1 = <$fh1>)
{
if($csv1->parse($line1))
{
	@fields1 =$csv1->fields();
	@ARR1=split(" ",$fields1[0]);
	#print "Client : $ARR[3]  Ip address : $ARR[-10]";
	#print " $fields[-10] , $fields[3] \n";
	$TEMP=$ARR1[3].$ARR1[4];
	$data1{$ARR1[0]}=$TEMP;
	#print "$ARR1[0] $TEMP" ;
}
else
{
print "could not parse lines";
}
}
#print Dumper \%data1;

=cut
#print Dumper(\%data1);
print "Fetching details of Ip and cobrant";
print $outfh "Fetching details of Ip and cobrant";
foreach $key(keys %data1)
{

		my $value=$data1{$key};
	if((index($row,$key) != -1) and (index($row,$value) != -1))
	{
		$flag++;
	#print "IP found $row";
	}
	}
	if($flag=='0')
	{
		print "\nIp Address : $key Cobrant Name : $data1{$key} \n";

		print $outfh "\nIp Address : $key Cobrant Name : $data1{$key} \n";
	}
} 
else
{
  warn "Could not open file '$filename' $!";
}
}
close $fh; 
close $fh2;
close $outfh;
=cut