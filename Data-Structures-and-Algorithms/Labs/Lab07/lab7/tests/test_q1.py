import pytest
import hashlib
from sys import stderr
from q1 import *

q1_testcases  = [
    # Visible Testcases
    ([5, 9, 2, 1, 6, 3, 0], 0, 6, "[0, 1, 2, 5, 6, 3, 9]\n[0, 1, 3, 5, 2, 6, 9]\n[0, 1, 2, 3, 5, 6, 9]\n[0, 1, 2, 3, 5, 6, 9]", [0, 1, 2, 3, 5, 6, 9], True),
    ([21, 36, 11, 9, 6, 42, 39], 0, 6, "[6, 9, 11, 21, 36, 42, 39]\n[6, 9, 11, 21, 36, 42, 39]\n[6, 9, 11, 21, 36, 42, 39]\n[6, 9, 11, 21, 36, 39, 42]", [6, 9, 11, 21, 36, 39, 42], True),
    ([10, 7, 8, 9, 1, 5], 0, 5, '[1, 7, 5, 8, 9, 10]\n[5, 1, 7, 8, 9, 10]\n[1, 5, 7, 8, 9, 10]\n[1, 5, 7, 8, 9, 10]', [1, 5, 7, 8, 9, 10], True),
    ([54, 26, 93, 17, 77, 31, 44, 55, 20], 0, 8, "[55, 26, 20, 17, 54, 31, 44, 77, 93]\n[17, 26, 20, 55, 54, 31, 44, 77, 93]\n[17, 44, 20, 26, 54, 31, 55, 77, 93]\n[17, 20, 26, 44, 54, 31, 55, 77, 93]\n[17, 20, 26, 31, 44, 54, 55, 77, 93]\n[17, 20, 26, 31, 44, 54, 55, 77, 93]", [17, 20, 26, 31, 44, 54, 55, 77, 93],True), 
    (['Aisha', 'Nadia', 'Waqar', 'Saleha', 'Hasan', 'Shahid', 'Shah Jamal', 'Abdullah', 'Umair', 'Taj'], 0, 9, "['Aisha', 'Abdullah', 'Hasan', 'Saleha', 'Waqar', 'Shahid', 'Shah Jamal', 'Nadia', 'Umair', 'Taj']\n['Abdullah', 'Aisha', 'Hasan', 'Saleha', 'Waqar', 'Shahid', 'Shah Jamal', 'Nadia', 'Umair', 'Taj']\n['Abdullah', 'Aisha', 'Hasan', 'Saleha', 'Nadia', 'Shah Jamal', 'Shahid', 'Waqar', 'Umair', 'Taj']\n['Abdullah', 'Aisha', 'Hasan', 'Nadia', 'Saleha', 'Shah Jamal', 'Shahid', 'Waqar', 'Umair', 'Taj']\n['Abdullah', 'Aisha', 'Hasan', 'Nadia', 'Saleha', 'Shah Jamal', 'Taj', 'Shahid', 'Umair', 'Waqar']\n['Abdullah', 'Aisha', 'Hasan', 'Nadia', 'Saleha', 'Shah Jamal', 'Shahid', 'Taj', 'Umair', 'Waqar']\n['Abdullah', 'Aisha', 'Hasan', 'Nadia', 'Saleha', 'Shah Jamal', 'Shahid', 'Taj', 'Umair', 'Waqar']", ['Abdullah', 'Aisha', 'Hasan', 'Nadia', 'Saleha', 'Shah Jamal', 'Shahid', 'Taj', 'Umair', 'Waqar'], True),
    ([4, 1, 3, 9, 7], 0, 4, '[1, 3, 4, 9, 7]\n[1, 3, 7, 4, 9]\n[1, 3, 4, 7, 9]', [1, 3, 4, 7, 9], True), 
    ([12, 8, -6, 2, 4, 5, 3, 7, 4, 2], 0, 9, '[3, 2, -6, 2, 4, 4, 5, 7, 12, 8]\n[-6, 2, 3, 2, 4, 4, 5, 7, 12, 8]\n[-6, 2, 2, 3, 4, 4, 5, 7, 12, 8]\n[-6, 2, 2, 3, 4, 4, 5, 7, 12, 8]\n[-6, 2, 2, 3, 4, 4, 5, 7, 12, 8]\n[-6, 2, 2, 3, 4, 4, 5, 7, 8, 12]', [-6, 2, 2, 3, 4, 4, 5, 7, 8, 12], True), 
    (['FunForFun', 'Practice.FunForFun', 'FunforFun'], 0, 2, "['FunforFun', 'FunForFun', 'Practice.FunForFun']\n['FunForFun', 'FunforFun', 'Practice.FunForFun']", ['FunForFun', 'FunforFun', 'Practice.FunForFun'], True), 
    
    # Hidden Testcases
    ([37, 23, 0, 17, 12, 72, 31, 46, 100, 88, 54], 0, 10, 'aa53a559af80d8de5898a894f7bf8ee1337fd12abf7fc9348758aa6cdc18ed0d', '1e9c261d574b2ee99aeae7f6de07cbc7a6cc6f487b79e1a80a15443fb300ad04', False), 
    ([5, 2, 7, 10, 3, 5, 2, 1, 8, 9], 0, 9, '1160ba27c042cede757170b7d73c658375b17e9991d42fc7b1f0bf2fcb63c55e', 'b4789af97f8cc5a46eb7c90b3ab321488339a9d3c09731baf7a679b05220c76e', False), 
    ([7, 5, 5, 4, 3, 2, 1], 0, 6, '354faa4b55d32523804d5e98a3d10f9a494282e4a7f2eb3662ee2f7ce9b583e5', 'b518438af1011f2e4f4baf630bc00b80d7b41f384b942815d06f5c99a1ae5ca3', False), 
    ([0, 1, -1], 0, 2, 'd8cd7f541a1774e1a735d5477275a57dba18169a8021d5295ab21657b883f294', 'e512856be455ce3d0249415a73d5c16913698de91538787853bce94b11eaada7', False), 
    ([0, 1, 2, 3, 9, -1], 0, 5, '92d80c63504cb55a239b1e076506aa3aae79bf5474fb194b7db12c3ccdc08e60', 'e4d84adb7f224ec80acbc1fd7de45109c456e80cd4d36326e3a08b8701588e53', False), 
    ([1, 2, 3, 4, 5, 6, 7, 8, 11, 10, 0], 0, 10, '370aed2ccfd0b9beebcf22004051ae1bcf43c7f9028133422f20292e62cd6e70', '8128d5ede96a5d11a114922983789e8de5a27d9b2a07991bfdb22181c70a0a9d', False), 
    ([71, 32, 22, 19, 18, 1, 15, 40], 0, 7, '0f6234b133f33e027f30c2001661616514c691f1958f6f414ce998bead9856b0', '978ab89564586985c5bf115acde16a65d03a44ca61184fe20fde0c56b9863b0a', False)
    ]


def hashcode(n: int) -> str:
    return hashlib.sha256(str(n).encode('utf-8')).hexdigest()

@pytest.mark.parametrize("lst,low,high,result,resultlst,testcase",q1_testcases)
def test_q1(capsys, lst, low, high, result, resultlst, testcase):
    quick_sort(lst, low, high)
    captured, _ = capsys.readouterr()
    print(hashcode(captured[:-1]))
    if testcase == True:
        assert captured[:-1] == result
        assert lst == resultlst
    else:
        assert hashcode(captured[:-1]) == result
        assert hashcode(lst) == resultlst