#!/usr/bin/perl
use strict;
use warnings;

my $filename = 'input.txt';

my $sector_sum = 0;

open(my $fh, "<", $filename)
    or die "Can't open $filename for reading\n";

while (my $line = <$fh>) {

    my $letters = '';
    my $numbers = '';
    my $checksum = '';
    my $computed_checksum = '';
    my %freq_hash = ();
    
    # remove newline and dashes
    chomp $line;
    $line =~ s/-//g;

    ($letters, $numbers, $checksum) = $line =~ /([a-z]+)([0-9]+)\[([a-z]+)\]/;
    
    my @letters_array = split(//, $letters);

    # add to hash for frequency counting
    foreach my $letter (@letters_array) {
        $freq_hash{$letter}++;
    }

    my $count = 0;
    # sort by highest value first, then alphabetical
    foreach my $key (sort { $freq_hash{$b} <=> $freq_hash{$a} or $a cmp $b } keys %freq_hash) {
        if ($count < 5) {
            $computed_checksum = $computed_checksum . $key;
            $count++;
        }
    }

    if ($computed_checksum eq $checksum) {
        $sector_sum += $numbers;
    }
    
}

print "final sum = $sector_sum\n";
