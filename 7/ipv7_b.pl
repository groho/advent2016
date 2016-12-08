#!/usr/bin/perl
use strict;
use warnings;

sub aba_check;
sub aba_reverse;

my $filename = 'input.txt';

my $valid_count = 0;

open(my $fh, "<", $filename)
    or die "Can't open $filename for reading\n";

# parse input file to big character matrix
while (my $line = <$fh>) {
    chomp $line;

    my @letters = split(//, $line);

    # loop through letters examining a window of 3 characters, keeping
    # track of whether we are inside/outside a bracket to determine
    # which dictionary to add character sequence to
    my $inside_bracket = 0;
    my @shift_reg = (0, 0, 0);
    my %aba = ();
    my %bab = ();
    foreach my $letter (@letters) {
        if ($letter eq '[' || $letter eq ']') { $inside_bracket = !$inside_bracket };
        @shift_reg = ($shift_reg[1], $shift_reg[2], $letter);      
        if (aba_check(@shift_reg)) {
            $aba{join('',@shift_reg)} = 1 if !$inside_bracket;
            $bab{join('',aba_reverse(@shift_reg))} = 1 if $inside_bracket;
        }
    }

    #loop through aba and try to match corresponding bab
    foreach my $key (keys %aba) {
        if (exists $bab{$key}) {
            $valid_count++;
            last;
        }
    }

}

print "IPs supporting SSL = $valid_count\n";

# take as input a 3 character array and check whether it
# satisfies the ABA property (three characters matching pattern)
sub aba_check {
    return ($_[0] eq $_[2] && $_[1] ne $_[2] && $_[0] ne $_[1] && ($_[1] ne '[' && $_[1] ne ']'));
}

# take as input a 3 character array and reverse aba <-> bab
sub aba_reverse {
    return ($_[1], $_[0], $_[1]);
}
