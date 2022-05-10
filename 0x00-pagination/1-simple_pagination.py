#!/usr/bin/env python3
"""
Simple pagination
"""
import csv
import math
from typing import List, Tuple


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


class Server:
    """
    Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """
        Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """
        Method to find the correct indexes to paginate the dataset correctly
        and return the appropriate page of the dataset
        """
        assert isinstance(page, int)
        assert page > 0
        assert isinstance(page_size, int)
        assert page_size > 0

        pag = index_range(page, page_size)
        self.dataset()
        return self.__dataset[pag[0]: pag[1]]
