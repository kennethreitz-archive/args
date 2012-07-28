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

    $ tool -s yes no --number=one --letter a b c --number=two
    Arguments passed in: ['-s', 'yes', 'no', '--number=one', '--letter', 'a', 'b', 'c', '--number=two']
    Flags detected: <args ['-s', '--number=one', '--letter', '--number=two']>
    Files detected: []
    NOT files detected: <args ['-s', 'yes', 'no', '--number=one', '--letter', 'a', 'b', 'c', '--number=two']>
    Grouped Arguments: OrderedDict([('_', <args []>), ('-s', <args ['yes', 'no']>), ('--number=one', <args []>), ('--letter', <args ['a', 'b', 'c']>), ('--number=two', <args []>)])
    Assignments detected: OrderedDict([('--number', <args ['one', 'two']>)])

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

    Arguments passed in: ['*.py', '--letter', 'a', 'b', 'c', '-s', '/home/example/.example', '--number=one', '--number=two']
    Flags detected: <args ['--letter', '-s', '--number=one', '--number=two']>
    Files detected: ['setup.py', 'args.py', 'tool.py', 'tests.py', '/home/example/.example/two', '/home/example/.example/one']
    NOT files detected: <args ['--letter', 'a', 'b', 'c', '-s', '--number=one', '--number=two']>
    Grouped Arguments: OrderedDict([('_', <args ['*.py']>), ('--letter', <args ['a', 'b', 'c']>), ('-s', <args ['/home/example/.example']>), ('--number=one', <args []>), ('--number=two', <args []>)])
    Assignments detected: OrderedDict([('--number', <args ['one', 'two']>)])


Installation
------------

Installation is simple with pip::

    $ pip install args
