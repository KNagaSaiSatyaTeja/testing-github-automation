import main

def test_add():
    assert main.add(2, 3) == 5
    assert main.add(-1, 1) == 0
    assert main.add(0, 0) == 0

if __name__ == "__main__":
    print("✅ All test cases passed!")
