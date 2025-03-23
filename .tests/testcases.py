import main

def test_add():
    passed_count = 0
    total = 0

    try:
        assert main.add(2, 3) == 5
        passed_count += 1
    except AssertionError:
        pass
    total += 1

    try:
        assert main.add(-1, 1) == 0
        passed_count += 1
    except AssertionError:
        pass
    total += 1

    try:
        assert main.add(0, 0) == 0
        passed_count += 1
    except AssertionError:
        pass
    total += 1

    # Print the results at the end
    print(f"✅ Passed: {passed_count}/{total}")

    # Force pytest to show the result in case of failure
    assert passed_count == total  # Optional: make pytest fail if not all tests pass
