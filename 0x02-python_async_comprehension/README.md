## 02. Python - Async Comprehension

### Resources

- [PEP 530 – Asynchronous Comprehensions](https://peps.python.org/pep-0530/ "PEP 530 -- Asynchronous Comprehensions")
- [What’s New in Python: Asynchronous Comprehensions / Generators](https://www.blog.pythonlibrary.org/2017/02/14/whats-new-in-python-asynchronous-comprehensions-generators/ "What’s New in Python: Asynchronous Comprehensions / Generators")
- [Type-hints for generators](https://stackoverflow.com/questions/42531143/how-to-type-hint-a-generator-in-python-3 "Type-hints for generators")

### Tasks

<details>
<summary>0. Async Generator</summary>

Write an asynchronous generator named `async_generator` that doesn't require any parameters.

This generator will execute a loop 10 times. In each iteration, it will wait for 1 second asynchronously and then yield a random number between 0 and 10. Make sure to utilize the `random` module for this.

```sh
bob@dylan:~$ cat 0-main.py
#!/usr/bin/env python3

import asyncio

async_generator = __import__('0-async_generator').async_generator

async def print_yielded_values():
    result = []
    async for i in async_generator():
        result.append(i)
    print(result)

asyncio.run(print_yielded_values())

bob@dylan:~$ ./0-main.py
[4.403136952967102, 6.9092712604587465, 6.293445466782645, 4.549663490048418, 4.1326571686139015, 9.99058525304903, 6.726734105473811, 9.84331704602206, 1.0067279479988345, 1.3783306401737838]
```

**File:**

- `0-async_generator.py`
</details>

<details>
<summary>1. Async Comprehensions</summary>

Import `async_generator` from the preceding task and then write a coroutine named `async_comprehension` that doesn't require any parameters.

This coroutine will gather 10 random numbers by using an asynchronous comprehension over `async_generator`, and then it will return these 10 random numbers.

```sh
bob@dylan:~$ cat 1-main.py
#!/usr/bin/env python3

import asyncio

async_comprehension = __import__('1-async_comprehension').async_comprehension


async def main():
    print(await async_comprehension())

asyncio.run(main())

bob@dylan:~$ ./1-main.py
[9.861842105071727, 8.572355293354995, 1.7467182056248265, 4.0724372912858575, 0.5524750922145316, 8.084266576021555, 8.387128918690468, 1.5486451376520916, 7.713335177885325, 7.673533267041574]

```

**File:**

- `1-async_comprehension.py`
</details>

<details>
<summary>2. Run time for four parallel comprehensions</summary>

Import `async_comprehension` from the previous file and construct a coroutine named `measure_runtime`. This coroutine will run `async_comprehension` four times concurrently using `asyncio.gather`.

`measure_runtime` should calculate the total execution time and return this value.

You'll notice that the total execution time is approximately 10 seconds. This is because `async_comprehension` is designed to run asynchronously, meaning all four instances of it run at the same time, not one after the other. Since each instance of `async_comprehension` takes about 10 seconds to complete, running them concurrently also takes around the same amount of time. This is the power of asynchronous programming! It allows you to run multiple tasks at the same time, thereby potentially reducing the total execution time.

```sh
bob@dylan:~$ cat 2-main.py
#!/usr/bin/env python3

import asyncio


measure_runtime = __import__('2-measure_runtime').measure_runtime


async def main():
    return await(measure_runtime())

print(
    asyncio.run(main())
)

bob@dylan:~$ ./2-main.py
10.021936893463135
```

**File:**

- `2-measure_runtime.py`
</details>
