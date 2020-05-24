from mathematica.algerba.matrices import add_matrices, sub_matrices


def test_add_matrices():
    a = [[1,2]],
         [3,4]]
    b = [[2,2,],
         [2,2]]


    expected = [[3,4],
                [5,6]]

    assert add_matrices (a,b) == expected

def test_add_matrices():
    a = [[1,2]],
         [3,4]]
    b = [[2,2,],
         [2,2]]


    expected = [[3,4],
                [5,6]]

    assert add_matrices (a,b) == expected