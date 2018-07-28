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



$filename = 'D:/files/b.csv';
$filename2 = 'D:/files/a.csv';
$fileout = 'D:/files/output.txt';


use Text::CSV;
use Data::Dumper;
%data=();
$csv=Text::CSV->new({sep_char => ','});
open($fh2,"<",$filename2) or die "Failed to open";
while(my $line = <$fh2>)
{
if($csv->parse($line))
{
	@fields =$csv->fields();
	@ARR=split(" ",$fields[0]);
	#print "Client : $ARR[3]  Ip address : $ARR[-10]";
	#print " $fields[-10] , $fields[3] \n";
	$data{$ARR[-10]}=$ARR[3];
}
else
{
print "could not parse lines";
}
}


#print Dumper(\%data);
open($outfh,'>',$fileout) or die "Could not open outfile $fileout $!";
print "Fetching details of Ip and cobrant";
print $outfh "Fetching details of Ip and cobrant";
foreach $key(keys %data)
{
	$flag=0;
	#print "Searching for Key : $key Data: $data{$key}";
if(open($fh, '<:encoding(UTF-8)', $filename))
{
	while ($row = <$fh>) 
	{
		my $value=$data{$key};
	if((index($row,$key) != -1) and (index($row,$value) != -1))
	{
		$flag++;
	#print "IP found $row";
	}
	}
	if($flag=='0')
	{
		print "\nIp Address : $key Cobrant Name : $data{$key} \n";

		print $outfh "\nIp Address : $key Cobrant Name : $data{$key} \n";
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

