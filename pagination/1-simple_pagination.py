#!/usr/bin/env python3
"""Module that provides a helper function to compute pagination."""
from typing import Tuple
import csv
from typing import List


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """Return a page of the dataset based on page number and page size.
        """
        assert isinstance(page, int) and isinstance(page_size, int)
        assert page > 0 and page_size > 0
        dataset = self.dataset()
        start, end = index_range(page, page_size)
        return dataset[start:end]


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """Return a tuple containing start and end indexes for pagination."""
    if page != 0:
        start_index = (page - 1) * page_size
        end_index = start_index + page_size
        return start_index, end_index
    else:
        return "page cannot be zero"
