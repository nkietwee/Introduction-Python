## **Practical Examples**
### Basic Fucntion in Python
- **🧩 Calculate Rectangle Area**
    Create a function **rectangle_area(width, height)** that returns the area of a rectangle.
    **Input :**
    ```shell
    Enter Width: 5
    Enter Height: 10
    ```
    **Output :**
    ```shell
    50
    ```

- **🧩 Sum Unlimited Numbers**
    Write a function **sum_all(*numbers)** that accepts multiple numbers and returns their total sum.
    **Input :**
    ```shell
    1, 2, 3, 4, 5
    ```
    **Output :**
    ```shell
    15
    ```

- **🧩 Enforce Keyword Arguments**
    Write a function **login(*, username, password)** that only accepts keyword arguments.
    **Input :**
    ```shell
    Enter Username : admin
    Enter Password : 123
    ```
    **Output :**
    ```shell
    Username: admin
    Password: 123
    ```

- **🧩 Check Even Number**
    Create a function **is_even(n)** that returns `True` if the number is even, otherwise `False`.
    **Output :**
    ```shell
    True # even
    False # odd
    ```

- **🧩 Create Profile**
    Write a function `show_profile(**info)` that displays user profile details using key-value pairs.
    **Input :**
    ```shell
    Enter your name: Boat
    age: 22
    city: Bangkok
    ```
    **Output :**
    ```shell
    Name: Boat
    Age: 22
    City: Bangkok
    ```

- **🧩 Recursive Factorial**
    Write a recursive function **factorial(n)** that returns the factorial of `n`. 
    **Input :**
    ```shell
    Enter your number: 5
    ```
    **Output :**
    ```shell
    120
    ```

- **🧩 Simple Number Guessing Game**  
    Write a Python script that implements the following game using a `while` loop.

    **Setup**  
    1. Import the standard `random` module.  
        ```python
        import random
        ```
    2. Define the maximum number:
        ```python
        max_num = 30
        ```
    3. Choose a secret number between 1 and 30:
        ```python
        target = random.randint(1, max_num)
        ```
    4. Initialize an attempt counter:
        ```python
        attempts = 0
        ```

    **Gameplay Loop**  
    Use a `while True` loop with these steps:
    1. Prompt the user (showing the current round):
        ```plaintext
        Round 1 – Guess Your Number:
        ```
    2. Read input and validate:
        - If input is not all digits, print:
        ```plaintext
        ❌ Please enter a number!
        ```
        and **continue** (do **not** increment `attempts`).
    3. Convert valid input to an integer and increment the counter:
        ```python
        guess = int(user_input)
        attempts += 1
        ```
    4. Compare `guess` to `target`:
        - **Correct**:  
        ```plaintext
        🎉 Congratulations! You guessed it in X attempts.
        ```  
        then **break** out of the loop.
        - **Too low**:  
        ```plaintext
        ⬆️ Higher!
        ```
        - **Too high**:  
        ```plaintext
        ⬇️ Lower!
        ```

    **End of Game**  
    After breaking out of the loop, print:
    ```plaintext
    Thanks for playing! 😊
    ```

