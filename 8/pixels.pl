#!/usr/bin/perl
use strict;
use warnings;

sub init_screen;
sub display_screen;
sub rect;
sub rotate_column;
sub rotate_row;

my $filename = 'input.txt';

# 50 x 6 pixels
my @screen;

open(my $fh, "<", $filename)
    or die "Can't open $filename for reading\n";

init_screen();

# parse input file to big character matrix
while (my $line = <$fh>) {
    chomp $line;  

    if ($line =~ m/rect ([0-9]+)x([0-9]+)/) {
        print "rect with $1 $2\n";
        rect($1,$2);
    } elsif ($line =~ m/rotate row y=([0-9]+) by ([0-9]+)/) {
        print "rotate_row with $1 $2\n";
        rotate_row($1,$2);
    } elsif ($line =~ m/rotate column x=([0-9]+) by ([0-9]+)/) {
        print "rotate_column with $1 $2\n";
        rotate_column($1,$2);
    }

    display_screen();
}

# initializes the 50x6 screen to all OFF
sub init_screen{
    for (my $x=0; $x<50; $x++) {
        for (my $y=0; $y<6; $y++) {
            $screen[$x][$y] = 0;
        }
    }
}

# pretty format to print the screen
sub display_screen{
    my $sum = 0;
    for (my $y=0; $y<6; $y++) {
        for (my $x=0; $x<50; $x++) {    
            print "$screen[$x][$y]";
            if ($screen[$x][$y]) {$sum++;}
        }
        print "\n";
    }
    print "Sum of 1's = $sum\n";
}

# takes x and y coords and enables those pixels
sub rect{
    for (my $x=0; $x<$_[0]; $x++) {
        for (my $y=0; $y<$_[1]; $y++) {
            $screen[$x][$y] = 1;
        }
    }
}

# takes column and number of rotations to make, performs rotation
sub rotate_column{
    my $column = $_[0];
    my $num_rot = $_[1];
    for (my $i=0; $i<$num_rot; $i++) {
        my $temp = $screen[$column][5];
        for (my $y=5; $y>0; $y--) {
             $screen[$column][$y] = $screen[$column][$y-1];
        }
        $screen[$column][0] = $temp;
    }
}

# takes row and number of rotations to make, performs rotation
sub rotate_row{
    my $row = $_[0];
    my $num_rot = $_[1];
    for (my $i=0; $i<$num_rot; $i++) {
        my $temp = $screen[49][$row];
        for (my $x=49; $x>0; $x--) {
            $screen[$x][$row] = $screen[$x-1][$row];
        }
        $screen[0][$row] = $temp;
    }
}
