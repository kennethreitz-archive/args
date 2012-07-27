#! /usr/bin/env python
# -*- coding: utf-8 -*-

import args
from nose.tools import ok_

def test_args_all():
    arguments = ['install', '--lang', 'python', 'c', 'js']
    arg = args.ArgsList(args = arguments)
    ok_(arg.all == arguments)

def test_flags():
    flags = ['--name', '--email']
    arguments = [flags[0], 'kracekumar', flags[1], 'me@kracekumar']
    arg = args.ArgsList(args = arguments)
    ok_(arg.flags.all == flags)


def test_files():
    files = ['*.py']
    arg = args.ArgsList(args = files)
    #any way current directory will have minimum one file i.e this file
    ok_(len(arg.files) > 1)

def test_not_files():
    flags = ['--name', '--email']
    arguments = [flags[0], 'kracekumar', flags[1], 'me@kracekumar', '*.py']
    arg = args.ArgsList(args = arguments)
    arguments.pop()
    ok_(arg.not_files.all == arguments)

def test_grouped():
    details = {'--language': ['python'], '--creator': ['Guido Van Rossum'], \
               '--foundation': ['psf']
               }
    arguments = []
    for key in details:
        arguments.append(key)
        arguments.append(details[key][0])

    arg = args.ArgsList(args = arguments)
    for item in arg.grouped:
        if item is not '_':
            ok_(arg.grouped[item].all == details[item])

def test_start_with():
    dynamic_lang = ['python', 'perl']
    static_lang = ['c', 'c++']
    arguments = ['--lang']
    arguments.extend(dynamic_lang)
    arguments.extend(static_lang)
    arg = args.ArgsList(args = arguments)
    ok_(arg.start_with('p').all == dynamic_lang)

def test_assignments():
    details = {'--arch': ['x64', 'i386'], 'lang': ['']}
    arguments = []
    for key in details:
        for argument in details[key]:
            arguments.append(key + '=' + argument)

    arg = args.ArgsList(args = arguments)
    for item in arg.assignments:
        ok_(arg.assignments[item].all == details[item])


