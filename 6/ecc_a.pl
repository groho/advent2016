#!/usr/bin/perl
use strict;
use warnings;

my $filename = 'input.txt';

my @letters;
my $line_num = 0;

my $message = '';

open(my $fh, "<", $filename)
    or die "Can't open $filename for reading\n";

# parse input file to big character matrix
while (my $line = <$fh>) {
   
    chomp $line;

    # split input line into array of characters and add to $letters[line][character]
    push @{ $letters[$line_num] }, split(//, $line);

    $line_num++;
}

for (my $char = 0; $char < scalar(@{$letters[0]}); $char++) {

    my %dict;

    for (my $line = 0; $line < $line_num; $line++) {
        print "letter = $letters[$line][$char]\n";
        $dict{$letters[$line][$char]}++;
    }

    my @sorted_dict_keys = sort { $dict{$b} <=> $dict{$a} } keys %dict;

    print "Decoding letter #$char = @sorted_dict_keys[0]\n";
    $message .= @sorted_dict_keys[0];
    
    undef %dict;
    
}

print "Decoded message = $message\n";
