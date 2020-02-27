#!/usr/bin/env python


class NoSolutionException(Exception):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


class InfiniteSolutionException(Exception):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
