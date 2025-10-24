def call_depth(n,max_depth=10):
    if n > max_depth:
        print("Stack overflow risk detected!")
        return
        call_depth(n + 1)

call_depth