# Test add, mult, sub, div
from calculator import add, sub

@pytest.mark.suite1
def test_add ():
	assert add(4, 1) == 5

@pytest.mark.suite2
def test_sub():
	assert sub(6, 5) == 1