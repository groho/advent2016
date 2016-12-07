#!/usr/bin/perl
use strict;
use warnings;
use Digest::MD5 qw(md5_hex);
use List::Util qw(sum0);

my $input = 'ugkcyxxp';

my $counter = 0;
my $chars_found = 0;
my @password;

while ($chars_found < 8) {

    my $digest = md5_hex($input . $counter);

    # Parse out 6th char for array location and 7th char for actual passcode
    if ($digest =~ m/^[0]{5}([0-9abcdef])([0-9abcdef])[0-9abcdef]*$/) {
        # only allow locations 0-7 and discard duplicates
        if (hex($1) < 8 && !defined $password[hex($1)]) {
            print "Password character $1 = $2\n";
            $password[$1] = $2;
            $chars_found++;
        }
    }

    $counter++;
}

print "Password = @password \n";
