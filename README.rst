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
    print 'Assignments detected: ' + str(args.assignments)

No arguments::

    $ tool
    Arguments passed in: []
    Flags detected: <args []>
    Files detected: []
    NOT files detected: <args []>
    Grouped Arguments: OrderedDict([('_', <args []>)])
    Assignments detected: OrderedDict()

A few arguments::

    $ tool -s this that --arch=x64 --import this and that and this and that --arch=i386
    Arguments passed in: ['-s', 'this', 'that', '--arch=x64', '--import', 'this', 'and', 'that', 'and', 'this', 'and', 'that', '--arch=i386']
    Flags detected: <args ['-s', '--arch=x64', '--import', '--arch=i386']>
    Files detected: []
    NOT files detected: <args ['-s', 'this', 'that', '--arch=x64', '--import', 'this', 'and', 'that', 'and', 'this', 'and', 'that', '--arch=i386']>
    Grouped Arguments: OrderedDict([('_', <args []>), ('-s', <args ['this', 'that']>), ('--arch=x64', <args []>), ('--import', <args ['this', 'and', 'that', 'and', 'this', 'and', 'that']>), ('--arch=i386', <args []>)])
    Assignments detected: OrderedDict([('--arch=', <args ['x64', 'i386']>)])

A few expanded file arguments::

    $ tool *.py
    Arguments passed in: ['args.py', 'setup.py', 'tests.py']
    Flags detected: <args []>
    Files detected: ['args.py', 'setup.py', 'tests.py']
    NOT files detected: <args []>
    Grouped Arguments: OrderedDict([('_', <args ['args.py', 'setup.py', 'tests.py']>)])
    Assignments detected: OrderedDict()

A few non-expanded file arguments::

    $ tool '*.py'
    Arguments passed in: ['*.py']
    Flags detected: <args []>
    Files detected: ['args.py', 'setup.py', 'tests.py']
    NOT files detected: <args []>
    Grouped Arguments: OrderedDict([('_', <args ['*.py']>)])
    Assignments detected: OrderedDict()

A few mixed files/flags/arguments::

    $ tool '*.py' --test test face book -s ~/.ssh --arch=x64
    Arguments passed in: ['*.py', '--test', 'test', 'face', 'book', '-s', '/home/example/.ssh', '--arch=x64']
    Flags detected: <args ['--test', '-s', '--arch=x64']>
    Files detected: ['args.py', 'setup.py', 'tests.py', '/home/example/.ssh/authorized_keys']
    NOT files detected: <args ['--test', 'test', 'face', 'book', '-s', '--arch=x64']>
    Grouped Arguments: OrderedDict([('_', <args ['*.py']>), ('--test', <args ['test', 'face', 'book']>), ('-s', <args ['/home/example/.ssh']>), ('--arch=x64', <args []>)])
    Assignments detected: OrderedDict([('--arch=', <args ['x64']>)])


Installation
------------

Installation is simple with pip::

    $ pip install args

