import pytest
import hashlib
import os
import sys

sys.path.append(os.path.join(os.path.dirname(__file__), ".."))

from q12 import *

q12_testcases = [
    # Visible Testcases
    ('0 1 2 3 4 5 6 7 8 9 10 11', [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11], {0: [0, 3, 6, 9], 1: [1, 4, 7, 10], 2: [2, 5, 8, 11]}, True), 
    ('-6 -5 -4 -3 -2 -1 0 1 2 3 4 5', [-6, -5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5], {0: [-6, -3, 0, 3], 1: [-5, -2, 1, 4], 2: [-4, -1, 2, 5]}, True), 
    ('17 20 -16 34 28 47 -49 37 -43 -19 -8 19', [17, 20, -16, 34, 28, 47, -49, 37, -43, -19, -8, 19], {0: [], 1: [34, 28, 37, -8, 19], 2: [17, 20, -16, 47, -49, -43, -19]}, True), 

    # Hidden Testcases
    ('-50 15 29 49 18 -7 42 -46 10 -13 -44 48', [-50, 15, 29, 49, 18, -7, 42, -46, 10, -13, -44, 48], '28a167a6b3109501f102a8818af6b3588d59f717f9ea9fba30fe1a2d807460c5', False), 
    ('', [], '158c42cc3f9f36a1da755e810cbf15688259dacfb5a2adff2b9180e4111beff9', False)
]

def hashcode(n: int) -> str:
    return hashlib.sha256(str(n).encode('utf-8')).hexdigest()

def capture_main_list(monkeypatch, input_str):
    monkeypatch.setattr('builtins.input', lambda: input_str)
    captured_lst = []

    import q12

    def fake_partition_modulo_three(lst):
        captured_lst.append(lst)
        return lst

    monkeypatch.setattr(q12, 'partition_modulo_three', fake_partition_modulo_three)

    q12.main()

    return captured_lst[0]


@pytest.mark.parametrize("s, nums, result, testcase", q12_testcases)
def test_q12_main(monkeypatch, s, nums, result, testcase):
    lst = capture_main_list(monkeypatch, s)
    assert lst == nums

@pytest.mark.parametrize("s, nums, result, testcase", q12_testcases)
def test_q12_mainOutput(monkeypatch, capsys, s, nums, result, testcase):
    
    monkeypatch.setattr('builtins.input', lambda: s)
    main()
    
    captured,_ = capsys.readouterr()
    captured = captured.strip()
    if testcase == True:
        assert eval(captured) == result
    else:
        assert hashcode(eval(captured)) == result

@pytest.mark.parametrize("s, nums, result, testcase", q12_testcases)
def test_q12_partition_modulo_three(s, nums, result, testcase):    
    if testcase == True:
        assert partition_modulo_three(nums) == result
    else:
        assert hashcode(partition_modulo_three(nums)) == result