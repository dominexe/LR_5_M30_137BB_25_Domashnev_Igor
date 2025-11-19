from all_def_sort import *
import pytest

def test_bubble_sort2(get_list):
    list = get_list
    list1 = get_list
    bubble_sort(list)
    assert list == sorted(list1)

def test_bubble_sort():
    list = [6, 7, 2, 9, 5]
    bubble_sort(list)
    assert list == [2,5,6,7,9]

def test_selection_sort():
    list = [12, 8, 3, 20, 11]
    selection_sort(list)
    assert list == [3,8,11,12,20]

def test_insertion_sort():
    list = [9, 1, 15, 28, 6]
    insertion_sort(list)
    assert list == [1,6,9,15,28]

def test_heap_sort():
    list = [35, 12, 43, 8, 51]
    heap_sort(list)
    assert list == [8,12,35,43,51]

def test_merge_sort():
    list = [120, 45, 68, 250, 176]
    list = merge_sort(list)
    assert list == [45,68,120,176,250]

def test_quick_sort():
    list = [22, 5, 1, 18, 99]
    quick_sort(list)
    assert list == [1,5,18,22,99]



