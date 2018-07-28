#!/usr/bin/perl -w

use strict;
my $file;
my @ar;
my $my_ps =`which ps`;
my $my_grep = `which grep`;
my $my_awk = `which awk`;
my $my_xargs =`which xargs`;
my $my_kill =`which kill`;
chomp($my_ps,$my_grep,$my_awk,$my_xargs);
#print "$my_ps,  $my_grep, $my_awk, $my_xargs\n";

my $command = `$my_ps aux | $my_grep -w defunct | $my_grep -w check_server.pl | $my_grep -v grep | $my_awk '{print \$2}' `;
my @process_details = split("\n",$command);
if(@process_details){
        foreach (@process_details){
                my $temp_ps =  `ps -ef | grep -w $_ | grep -w check_server.pl | grep defunct | grep -v grep` ;
		if($temp_ps){
		#my $search = `$my_ps -ef | $my_grep -w $_ | $my_grep -v grep | $my_awk '{print \$2" " \$3}' | $my_xargs echo`;
                 my $search = `$my_ps -ef | $my_grep -w $_ | grep -w check_server.pl | $my_grep -v grep | $my_awk '{print \$2" " \$3}' | $my_xargs kill -9`;
			sleep(0.5);
		}
        }
}

my $hostname  = `hostname | cut -d"-" -f2`;
chomp($hostname);
my @array = `docker ps -q`;
#my @array = ('e9e0353c88c7','6903a05e585e');
foreach my $x (@array){
        $file = `perl check_server.pl $x`;
        chomp($file);
        push(@ar,"$file");

}
print "check_server_$hostname:";
foreach my $y (@ar){

        print "$y\n";
}

