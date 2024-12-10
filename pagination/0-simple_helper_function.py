#!/usr/bin/env python3
"""function that returns a tuple"""


def index_range(page, page_size):
    """This function calculates the start and end index,
    for a given page number and page size."""
    start = (page - 1) * page_size
    end = page * page_size
    return tuple([start, end])
