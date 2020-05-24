from matchematica.geometry.figures import square_area, triangle_area


def test_sqaure_area():
    assert square_area(4) == 16
    assert square_area(2) == 4


def test_triangle():
    assert triangle_area(2, 4) == 4
