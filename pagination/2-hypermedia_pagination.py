#!/usr/bin/env python3
"""function that implements a get_hyper method"""

import math
from typing import List, Dict, Any
import csv


class Server:
    """Server class to paginate a dataset"""
    def __init__(self):
        self.__dataset = None

        def dataset(self) -> List[List]:
            """Cached dataset"""
            if self.__dataset is None:
                with open(self.DATA_FILE) as f:
                    reader = csv.reader(f)
                    dataset = [row for row in reader]
                    self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List[Any]]:
        """Returns a paginated dataset"""
        assert isinstance(page, int) and page > 0
        assert isinstance(page_size, int) and page_size > 0

        dataset = self.dataset()
        start_index = (page - 1) * page_size
        end_index = start_index + page_size

        if start_index >= len(dataset):
            return []

        return dataset[start_index:end_index]

    def get_hyper(self, page: int = 1, page_size: int = 10) -> Dict[str, Any]:
        """Returns a dictionary with information pagination"""
        data = self.get_page(page, page_size)
        dataset_length = len(self.dataset())
        total_pages = math.ceil(dataset_length / page_size)

        return {
            'page_size': len(data),
            'page': page,
            'data': data,
            'next_page': page + 1 if page < total_pages else None,
            'prev_page': page - 1 if page > 1 else None,
            'total_pages': total_pages,
        }
