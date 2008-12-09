# multihook

multihook allows multiplexing of [Git](http://git.or.cz) hooks. 

It is useful if you want to run multiple hooks on a single event.  For
example, you might use multihook on post-receive to send notifications
by e-mail and by XMPP multi-user chat.

## License

This code is copyright (c) 2008 by Jack Moffitt <jack@metajack.im> and
is available under the [GPLv3](http://www.gnu.org/licenses/gpl.html).
See `LICENSE.txt` for details.

## Usage

To use multihook, just copy `multihook.py` to your
repository's `.git/hooks` dir and call it `post-receive`. Be sure to
set it executable with `chmod 755 post-receive` as well.

You'll need to edit the very top of the file where `HOOKS` is
defined.  Each item of this array is a script to run.  Each item is an
array of strings; the first string is the script, and the other
strings are its arguments.
