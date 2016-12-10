#!/usr/bin/perl
use strict;
use warnings;

sub expand;

my $filename = 'input.txt';

my @letters;
my $compressed_string = '';

open(my $fh, "<", $filename)
    or die "Can't open $filename for reading\n";

while (my $line = <$fh>) {
    chomp $line;  
    $compressed_string = $line;
}

my $size = expand($compressed_string);
print "decompressed_size = $size\n";

# takes in substring for expansion, recursively returning expanded size
sub expand {
    my $in = $_[0];
    if ((my ($m1, $m2, $m3, $m4)) = ($in =~ m!^([a-zA-Z]*?)\(([0-9]+)x([0-9]+)\)(.*)$!)) {
        return ( (length $m1 || 0) + $m3 * expand(substr($m4, 0, $m2)) + expand(substr($m4, $m2)) );
    } else {
        return (length $in || 0);
    }
}
