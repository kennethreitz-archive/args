args
====

Argument Parsing for Humans.


Usage
-----

Here's an example application::

    import args

    print 'Arguments passed in: ' + str(args.all)
    print 'Flags detected: ' + str(args.flags)
    print 'Files detected: ' + str(args.files)
    print 'NOT files detected: ' + str(args.not_files)
    print 'Grouped Arguments: ' + str(args.grouped)

No arguments::

    $ tool
    Arguments passed in: []
    Flags detected: <args []>
    Files detected: []
    NOT Files detected: <args []>
    Grouped Arguments: {'_': <args []>}

A few arguments::

    $ tool -s this that --import this and that and this and that
    Arguments passed in: ['-s', 'this', 'that', '--import', 'this', 'and', 'that', 'and', 'this', 'and', 'that']
    Flags detected: <args ['-s', '--import'
    Files detected: []
    NOT Files detected: <args ['-s', 'this', 'that', '--import', 'this', 'and', 'that', 'and', 'this', 'and', 'that']>
    Grouped Arguments: {'--import': <args ['this', 'and', 'that', 'and', 'this', 'and', 'that']>, '_': <args []>, '-s': <args ['this', 'that']>}

A few expanded file arguments::

    $ tool *.py
    Arguments passed in: ['args.py', 'setup.py']
    Flags detected: <args []>
    Files detected: ['args.py', 'setup.py']
    NOT Files detected: <args []>
    Grouped Arguments: {'_': <args ['args.py', 'setup.py']>}

A few non-expanded file arguments::

    $ tool '*.py'
    Arguments passed in: ['*.py']
    Flags detected: <args []>
    Files detected: ['args.py', 'setup.py']
    NOT Files detected: <args []>
    Grouped Arguments: {'_': <args ['*.py']>}

A few mixed files/flags/arguments::

    $ tool '*.py' --test test face book -s ~/.ssh
    Arguments passed in: ['*.py', '--test', 'test', 'face', 'book', '-s', '/Users/kreitz/.ssh']
    Flags detected: <args ['--test', '-s']>
    Files detected: ['args.py', 'setup.py', '/Users/kreitz/.ssh/id_rsa', '/Users/kreitz/.ssh/id_rsa.pub', '/Users/kreitz/.ssh/known_hosts']
    NOT Files detected: <args ['--test', 'test', 'face', 'book', '-s']>
    Grouped Arguments: {'--test': <args ['test', 'face', 'book']>, '_': <args ['*.py']>, '-s': <args ['/Users/kreitz/.ssh']>}


Installation
------------

Installation is simple with pip::

    $ pip install args

