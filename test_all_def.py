from all_def import *
import pytest


# def test_find_delitels():
#     assert find_delitels(25) == [1,5,25]
#
# def test_perevod():
#     assert perevod(42,2) == 101010
#
# def test_find_all_sogl():
#     assert find_all_sogl('hello, my name is anton') == 10
#
# def test_find_all_glas():
#     assert find_all_glas('no one dares to order me around') == 12
#
# def test_find_del_matrix():
#     assert find_del_matrix(2,3,4,5) == -2


# # Параметризм
# @pytest.mark.parametrize("x11,x12,x21,x22,answer",[
#     (2,3,4,5,-2),
#     (1,1,1,1,0),
#     (5,6,7,8,0)
# ])
# def test_find_del_matrix2(x11,x12,x21,x22,answer):
#     assert find_del_matrix(x11,x12,x21,x22) == answer

#Фикстуры
def test_find_all_sogl2(get_sp):
    k = get_sp
    assert find_all_sogl(k) in [x for x in range(5,10)]

def test_find_all_glas2(get_sp):
    k = get_sp
    assert find_all_glas(k) in [x for x in range(2,10)]