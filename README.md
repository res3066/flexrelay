# flexrelay

Simple tool to relay FlexRadio's UDP discovery protocol packets outside of a
vlan/broadcast domain (to include arbitrary networks across a VPN, etc).

## Requirements

Developed on Python 3.11.  Should work on any python3.  It would potentially be
valuable to make it python2-agnostic as there is some older router software with
embedded python2.7.

## Impetus for writing this code / Principle of Operation

FlexRadios have a simple beaconing protocol consisting of broadcasting
packets on UDP/4992.  Flex does not support connecting across
non-local networks because if they did, no doubt hams would just put
Flex hardware direct on the Internet or poke holes in firewalls and
consider it done.  Fat, drunk and stupid is no way to go through life,
son.

Flex offers a service for finding your radio (or your friend's radio)
remotely, brokering access, and connecting to it.  It's called
Smartlink and probably useful for the vast majority of ham use cases.
But not mine.  I want to run OpenVPN or Wireguard between an ipad or a laptop (or a
remote site) and home, and have things transparently Just Work, without
reliance on Internet connectivity or Flex's service being up.

At present, the FlexRadio 6400 (the only unit upon which I have tested
this) is agnostic about receiving broadcast vs. unicast packets so the
mqtt-based client/server architecture [required by
others](https://github.com/hb9fxq/flex6k-discovery-util-go/) is
unnecessary.  All that is needed is a broadcast listener that sits in
the same broadcast domain with the Flex and then forwards off the
advertisement traffic to a plurality of unicast addresses.

## Usage

At AI4UC QTH we moved the VPN endpoint off of a router to a Raspberry Pi with a hole poked for OpenVPN
to make it through.  We run this script inside of screen because we're lame and haven't gotten around
to writing a systemd wrapper for it.

There's a variable inside that lists all of the targets.  This (and other things) should be a config file.

./flexrelay.py

will print out some debug characters telling when packets are received and then written to the network.

## To Do

Add a configuration file.  .ini is preferred because it is built in, despite it being a crummy format.

Add systemd support.  Yes, systemd sucks.  No, we aren't getting rid of it.

## Dependencies

None and we want to keep it that way!

## License

MIT

## Author Information

rs@seastrom.com AI4UC


