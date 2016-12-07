#!/usr/bin/perl
use strict;
use warnings;
use Digest::MD5 qw(md5_hex);

my $input = 'ugkcyxxp';

my $counter = 0;
my $password = '';

while (length($password) < 8) {

    my $digest = md5_hex($input . $counter);

    # parse out 6th character for password
    if ($digest =~ m/^[0]{5}([0-9abcdef])[0-9abcdef]*$/) {
        $password .= $1;
        print "Found password character #" . length($password) . " = $1 \n";
    }
    
    $counter++;
}

print "Password = $password\n";
