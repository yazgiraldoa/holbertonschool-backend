#!/usr/bin/env python3
"""
Pagination helper
"""
from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple[int]:
    """
    Function that return a tuple of size two containing a start
    index and an end index corresponding to the range of indexes
    to return in a list for those particular pagination parameters.
    """
    page_num = page - 1
    start_idx = 0 if page_num == 0 else page_num * page_size
    end_idx = page * page_size
    return (start_idx, end_idx)
