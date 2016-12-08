#!/usr/bin/perl
use strict;
use warnings;

sub abba_check;

my $filename = 'input.txt';

my $valid_count = 0;

open(my $fh, "<", $filename)
    or die "Can't open $filename for reading\n";

# parse input file to big character matrix
while (my $line = <$fh>) {
    chomp $line;

    my @letters = split(//, $line);

    # loop through letters examining a window of 4 characters, keeping
    # track of whether we are inside/outside a bracket
    my $found_abba = 0;
    my $inside_bracket = 0;
    my @shift_reg = (0, 0, 0, 0);
    foreach my $letter (@letters) {
        if ($letter eq '[' || $letter eq ']') { $inside_bracket = !$inside_bracket };
        @shift_reg = ($shift_reg[1], $shift_reg[2], $shift_reg[3], $letter);
        if (abba_check(@shift_reg)) {
            if ($inside_bracket) {
                $found_abba = 0;
                last;
            } else {
                $found_abba = 1;
            }
        }
    }

    $valid_count += $found_abba;

}

print "IPs supporting TLS = $valid_count\n";

# take as input a 4 character array and check whether it
# satisfies the ABBA property (pair of different chars, concat with reverse)
sub abba_check {
    return ($_[0] eq $_[3] && $_[1] eq $_[2] && $_[0] ne $_[1]);
}
