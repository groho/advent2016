#!/usr/bin/perl
use strict;
use warnings;

my $filename = 'input.txt';

my @letters;
my $compressed_string = '';

open(my $fh, "<", $filename)
    or die "Can't open $filename for reading\n";

while (my $line = <$fh>) {
    chomp $line;  
    $compressed_string = $line;
}

# use lazy regex to match first decompression marker,
# counting all characters encountered up the marker
my $size = 0;
while (length($compressed_string) > 0) {

    $compressed_string =~ m!^([a-zA-Z]*?)\(([0-9]+)x([0-9]+)\)(.*)$!;

    # ignoring the actual chars, add up all the chars leading up
    # to a decompression marker, plus the number of chars that 
    # would be decompressed and duplicated due to the marker
    my $temp_size = 0;
    $temp_size += length $1; #chars before marker
    $temp_size += $2 * $3; #chars decompressed
    $size += $temp_size;

    # move forward in the sequence to the next parsing point
    $compressed_string = substr $4, $2;
}

print "decompressed_size = $size\n";
