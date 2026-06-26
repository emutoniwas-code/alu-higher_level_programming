#!/usr/bin/python3
def islower(c):
    """Check for lowercase character"""
    if type(c) is not str or len(c) == 0:
        return False
    return ord("a") <= ord(c) <= ord("z")
