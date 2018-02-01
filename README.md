CSI Agent
=========
An agent providing Chat Service Integration, read: a bot.

CSI Agent is a chat bot framework that supports easy plugin development
and multiple backends. Initial development will target Slack, but once
the codebase is functional, support for Discord, Mattermost, and good
old IRC is also planned.

Testing
-------
The code will use the [tox] framework for testing.
Both dynamic and static analysis of the code will be performed, using
[nose] and [pylint], respectively.

Documentation
-------------
The public API of the code should be documented thoroughly with
docstrings, including all arguments and exceptions that are raised.

Plugins should also be documented well using docstrings. A built-in
`help` command is planned that will rely on the summary line and body
of plugin docstrings to provide basic help to the user.

Once the project is more fully developed, I plan to use [sphinx] to
generate documentation and publish it on [readthedocs].

Python Compatibility
--------------------
Only Python 3.4 and up will be supported. Most libraries these days seem
to work on both Python 2 and 3, and I feel that the codebase will be
much cleaner and easier to maintain without having to address
compatibility issues between versions.

This isn't a library that will need to be pulled into an existing
Python 2 application, either - it's a new platform, and new code will be
written to integrate into it. I'd much rather have plugins be written
with the expectation of running on Python 3 now than have plugins in
the future that don't work once support for Python 2 is
[finally dropped in 2020][pep-373].


[tox]: https://tox.readthedocs.io/en/latest/
[nose]: https://nose.readthedocs.io/en/latest/
[pylint]: https://pylint.readthedocs.io/en/latest/

[sphinx]: http://www.sphinx-doc.org/en/stable/
[readthedocs]: https://readthedocs.org/

[pep-373]: https://www.python.org/dev/peps/pep-0373/
