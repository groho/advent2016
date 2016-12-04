#!/usr/bin/perl
use strict;
use warnings;

my $filename = 'input.txt';
my $a0=0; 
my $b0=0; 
my $c0=0;
my $a1=0; 
my $b1=0; 
my $c1=0;
my $a2=0; 
my $b2=0; 
my $c2=0;

my @items;

my $valid = 0;

my $loop = 0;

open(my $fh, "<", $filename)
    or die "Can't open $filename for reading\n";

while (my $line = <$fh>) {
    chomp $line;
    if ($loop == 0) {
        ($a0, $a1, $a2) = $line =~ /\s*([0-9]+)\s*([0-9]+)\s*([0-9]+)/;
    } elsif ($loop == 1) {
        ($b0, $b1, $b2) = $line =~ /\s*([0-9]+)\s*([0-9]+)\s*([0-9]+)/;
    } else {
        ($c0, $c1, $c2) = $line =~ /\s*([0-9]+)\s*([0-9]+)\s*([0-9]+)/;
    }   

    if ($loop == 2) {
        if ($a0+$b0>$c0 && $b0+$c0>$a0 && $a0+$c0>$b0) {$valid++;}
        if ($a1+$b1>$c1 && $b1+$c1>$a1 && $a1+$c1>$b1) {$valid++;}
        if ($a2+$b2>$c2 && $b2+$c2>$a2 && $a2+$c2>$b2) {$valid++;}
        $loop = 0;
    } else {
        $loop++;
    }
    
}

print "$valid\n";
