#!/usr/bin/env python3
"""Hypermedia pagination"""
import csv
import math
from typing import List, Dict


class Server:
    """Server class to paginate a database of popular baby names"""
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
        """Retrieves a page of data from the dataset"""
        assert isinstance(
            page, int) and isinstance(
            page_size, int), "Must be int"
        assert page > 0 and page_size > 0, "The page and page_size must be > 0"
        list = []
        with open(self.DATA_FILE) as f:
            read = csv.reader(f)
            idxx = index_range(page, page_size)
            for num, line in enumerate(read):
                if num in range(idxx[0], idxx[1]):
                    list.append(line)
        return list

    def get_hyper(self, page: int = 1, page_size: int = 10) -> Dict:
        """Returns a dictionary with pagination metadata"""
        dict = {}
        idxx = index_range(page, page_size)
        if (idxx[0] + 1) > len(self.dataset()):
            dict["page_size"] = 0
        else:
            dict["page_size"] = idxx[1] - idxx[0]
        dict["page"] = page
        dict["data"] = self.get_page(page, page_size)
        total_pages = math.ceil(len(self.dataset()) / page_size)
        dict["next_page"] = page + 1 if page < total_pages else None
        dict["prev_page"] = page - 1 if page > 1 else None
        dict["total_pages"] = total_pages
        return dict


def index_range(page, page_size):
    """Calculate the start and end indices for a dataset page"""
    start = (page - 1) * page_size
    end = page * page_size
    return tuple([start, end])
