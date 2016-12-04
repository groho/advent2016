#!/usr/bin/perl
use strict;
use warnings;

my $x = 0;
my $y = 0;
my @xs = (0);
my @ys = (0);

my $facing = 'n';
my $next_facing = '';

my $input = "L5, R1, R3, L4, R3, R1, L3, L2, R3, L5, L1, L2, R5, L1, R5, R1, L4, R1, R3, L4, L1, R2, R5, R3, R1, R1, L1, R1, L1, L2, L1, R2, L5, L188, L4, R1, R4, L3, R47, R1, L1, R77, R5, L2, R1, L2, R4, L5, L1, R3, R187, L4, L3, L3, R2, L3, L5, L4, L4, R1, R5, L4, L3, L3, L3, L2, L5, R1, L2, R5, L3, L4, R4, L5, R3, R4, L2, L1, L4, R1, L3, R1, R3, L2, R1, R4, R5, L3, R5, R3, L3, R4, L2, L5, L1, L1, R3, R1, L4, R3, R3, L2, R5, R4, R1, R3, L4, R3, R3, L2, L4, L5, R1, L4, L5, R4, L2, L1, L3, L3, L5, R3, L4, L3, R5, R4, R2, L4, R2, R3, L3, R4, L1, L3, R2, R1, R5, L4, L5, L5, R4, L5, L2, L4, R4, R4, R1, L3, L2, L4, R3";

my @input = split(/,\s/, $input);

foreach my $in (@input) {

    $in =~ /([LR])([0-9]+)/;
    my $dir =$1;
    my $steps = $2;

    for (my $i=0; $i < $steps; $i++) {
    
        if ($facing eq 'n') {
            if ($dir eq 'L') {
                $x--;
                $next_facing = 'w';
            } else {
                $x++;
                $next_facing = 'e';
            }
        } elsif ($facing eq 's') {
            if ($dir eq 'L') {
                $x++;
                $next_facing = 'e';
            } else {
                $x--;
                $next_facing = 'w';
            }       
        } elsif ($facing eq 'e') {
            if ($dir eq 'L') {
                $y++;
                $next_facing = 'n';
            } else {
                $y--;
                $next_facing = 's';
            }        
        } elsif ($facing eq 'w') {
            if ($dir eq 'L') {
                $y--;
                $next_facing = 's';
            } else {
                $y++;
                $next_facing = 'n';
            }       
        }
        
        foreach my $coord (0 .. $#xs) {
            if ($x == $xs[$coord] && $y == $ys[$coord]) {
                print "Revisited x=$x y=$y\n";
            }
        }
        
        #add current locations to arrays
        
        push @xs, $x;
        push @ys, $y;

    }

    $facing = $next_facing;
}

print "Part one final location - x:$x y:$y\n";

