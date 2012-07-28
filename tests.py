#! /usr/bin/env python
# -*- coding: utf-8 -*-

import args
from nose.tools import ok_

def compare_values(a, b):
    ok_(a == b)

def test_args_all():
    arguments = ['test', '--number', 'one', 'two', 'three']
    arg = args.ArgsList(args = arguments)
    ok_(arg.all == arguments)

def test_flags():
    flags = ['--one', '--two']
    arguments = [flags[0], 'a', flags[1], 'b']
    arg = args.ArgsList(args = arguments)
    ok_(arg.flags.all == flags)

def test_files():
    files = ['*.py']
    arg = args.ArgsList(args = files)
    ok_(len(arg.files) > 1)

def test_not_files():
    flags = ['--one', '--two']
    arguments = [flags[0], 'a', flags[1], 'b', '*.py']
    arg = args.ArgsList(args = arguments)
    arguments.pop()
    ok_(arg.not_files.all == arguments)

def test_grouped():
    details = {'--alphabet': ['a', 'b'], '--number': ['one'], '--test': ['']}
    arguments = []
    for key in details:
        for argument in details[key]:
            arguments.append(key)
            arguments.append(argument)

    arg = args.ArgsList(args = arguments)
    yield compare_values, len(arg.grouped) - 1, len(details)
    for item in arg.grouped:
        if item is not '_':
            yield compare_values, arg.grouped[item].all, details[item]

def test_start_with():
    numbers = ['one', 'two', 'three']
    fnumbers = ['four', 'five']
    arguments = ['--number']
    arguments.extend(numbers)
    arguments.extend(fnumbers)
    arg = args.ArgsList(args = arguments)
    ok_(arg.start_with('f').all == fnumbers)

def test_assignments():
    details = {'--number': ['one', 'two'], 'test': ['']}
    arguments = []
    for key in details:
        for argument in details[key]:
            arguments.append(key + '=' + argument)

    arg = args.ArgsList(args = arguments)
    yield compare_values, len(arg.assignments), len(details)
    for item in arg.assignments:
        yield compare_values, arg.assignments[item].all, details[item]
