# Fuzzbang #
---

Fuzzbang is a Python 3 package providing simple fuzzing support.

## Example ##
    from fuzzbang.alphanumericfuzzer import AlphaNumericFuzzer
    
    N = 10 # number of test cases

    # bounds on length of alphanumeric strings
    MIN_LEN = 0
    MAX_LEN = 8
    
    f = AlphaNumericFuzzer(MIN_LEN, MAX_LEN) # fuzzer object
    
    # generate test cases
    for i in range(N):
        data = f.generate() # generate string
        print("(" + str(len(data)) + ")") # print length of string
        print(data) # print string itself

