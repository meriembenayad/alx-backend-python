## 0x01 - Python - Async

![async](async.jpeg)

### Resources

**Read or watch**:

- [Async IO in Python: A Complete Walkthrough](https://realpython.com/async-io-python/ "Async IO in Python: A Complete Walkthrough")
- [asyncio - Asynchronous I/O](https://docs.python.org/3/library/asyncio.html "asyncio - Asynchronous I/O")
- [random.uniform](https://docs.python.org/3/library/random.html#random.uniform "random.uniform")

### Tasks

<details>
<summary>0. The basics of async</summary>

Create an asynchronous coroutine named `wait_random`. This coroutine should accept an integer argument `max_delay` with a default value of 10. The function of `wait_random` is to pause for a random delay between 0 and `max_delay` seconds (inclusive and could be a floating-point number) and then return that delay.

The random module should be utilized for this purpose.

Here's how you can use it:

```python
#!/usr/bin/env python3

import asyncio

wait_random = __import__('0-basic_async_syntax').wait_random

print(asyncio.run(wait_random()))
print(asyncio.run(wait_random(5)))
print(asyncio.run(wait_random(15)))
```

When you run the script, it might produce output like this:

```shell
9.034261504534394
1.6216525464615306
10.634589756751769
```

**File:**

- `0-basic_async_syntax.py`
</details>

<details>
<summary>1. Let's execute multiple coroutines at the same time with async</summary>

From the Python file you've previously written, import the `wait_random` function. Then, write an asynchronous routine named `wait_n` that accepts two integer arguments in this order: `n` and `max_delay`. The routine should call `wait_random` `n` times with the specified `max_delay`.

The `wait_n` routine should return a list of all the delays (as float values). The delays in the list should be in ascending order without using the `sort()` function due to the concurrent nature of the routine.

Here's how you can use it:

```python
#!/usr/bin/env python3
'''
This is a test file for verifying the correct output of the wait_n coroutine
'''
import asyncio

wait_n = __import__('1-concurrent_coroutines').wait_n

print(asyncio.run(wait_n(5, 5)))
print(asyncio.run(wait_n(10, 7)))
print(asyncio.run(wait_n(10, 0)))
```

When you run the script, it might produce output like this:

```shell
[0.9693881173832269, 1.0264573845731002, 1.7992690129519855, 3.641373003434587, 4.500011569340617]
[0.07256214141415429, 1.518551245602588, 3.355762808432721, 3.7032593997182923, 3.7796178143655546, 4.744537840582318, 5.50781365463315, 5.758942587637626, 6.109707751654879, 6.831351588271327]
[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]
```

Please note that your output might vary slightly, which is expected.

**File:**

- `1-concurrent\_coroutines.py`
</details>

<details>
<summary>2. Measure the runtime</summary>

In the file `2-measure_runtime.py`, import the `wait_n` function from the previous Python file you've written.

Define a function called `measure_time` that takes two integer arguments: `n` and `max_delay`. This function should calculate the total time taken to execute `wait_n(n, max_delay)` and then return the average time per operation, which is `total_time / n`. The result should be a floating-point number.

To measure the approximate elapsed time, make use of the `time` module.

Here's how you can use it:

```python
#!/usr/bin/env python3

measure_time = __import__('2-measure_runtime').measure_time

n = 5
max_delay = 9

print(measure_time(n, max_delay))
```

When you run the script, it might produce output like this:

```shell
1.759705400466919
```

**File:**

- `2-measure\_runtime.py`
</details>

<details>
<summary>3. Tasks</summary>

From the `0-basic_async_syntax` file, import the `wait_random` function.

Construct a regular function (not an asynchronous one) named `task_wait_random` that accepts an integer `max_delay` as an argument and returns an `asyncio.Task`.

Here's how you can use it:

```python
#!/usr/bin/env python3

import asyncio

task_wait_random = __import__('3-tasks').task_wait_random

async def test(max_delay: int) -> float:
    task = task_wait_random(max_delay)
    await task
    print(task.__class__)

asyncio.run(test(5))
```

When you run the script, it might produce output like this:

```shell
<class '_asyncio.Task'>
```

**File:**

- `3-tasks.py`
</details>

<details>
<summary>4. Tasks</summary>

Update the code from `wait_n` to create a new function named `task_wait_n`. The code should be almost the same as `wait_n`, with the exception that `task_wait_random` is invoked instead.

Here's how you can use it:

```python
#!/usr/bin/env python3

import asyncio

task_wait_n = __import__('4-tasks').task_wait_n

n = 5
max_delay = 6
print(asyncio.run(task_wait_n(n, max_delay)))
```

When you run the script, it might produce output like this:

```shell
[0.2261658205652346, 1.1942770588220557, 1.8410422186086628, 2.1457353803430523, 4.002505454641153]
```

**File:**

- `4-tasks.py`
</details>
