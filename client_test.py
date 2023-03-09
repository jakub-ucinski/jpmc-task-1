from client import getRatio

TEST_CASES = [
    {"input": {'a': 100, 'b': 100}, "expected": 1},
    {"input": {'a': 0, 'b': 100}, "expected": 0},
    {"input": {'a': 100, 'b': 0}, "expected": None},
    {"input": {'a': 100, 'b': 1}, "expected": 100},
    {"input": {'a': 1, 'b': 100}, "expected": 1/100},
]

RESULTS = {'pass': {'cases': []}, 'fail': {'cases': []}}

for test_case in TEST_CASES:
    inpt = test_case["input"]
    expected = test_case["expected"]
    actual = getRatio(inpt["a"], inpt["b"])

    try:
        assert actual == expected
        RESULTS["pass"]["cases"].append({"input": inpt, "expected": expected, "actual": actual})

    except AssertionError:
        RESULTS["fail"]["cases"].append({"input": inpt, "expected": expected, "actual": actual})

print("Pass : ", len(RESULTS["pass"]["cases"]))
print("Fail : ", len(RESULTS["fail"]["cases"]))
for fail in RESULTS["fail"]["cases"]:
    print("Input : ", fail["input"])
    print("Expected : ", fail["expected"])
    print("Actual : ", fail["actual"])
