#!/usr/bin/env python
# encoding: utf-8

from expendeeApp import ExpendeeApp

if __name__ == '__main__':
    expendeeApp = ExpendeeApp()
    cancel = False
    while not cancel:
        inp = input()
        print(expendeeApp.runCommand(inp))