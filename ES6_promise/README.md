# Promises

## What is a Promise?
- A Promise is a JavaScript object that represents a task that will finish later.
- It is like a promise from a friend: "I will give you the answer soon."
- In code, it helps us work with asynchronous actions like API calls, reading files, or waiting for a timer.

## Why do we use Promises?
- Because some tasks take time and do not finish immediately.
- Promises let us wait for results without blocking the whole program.
- Useful for real-world things like:
  - talking to an API
  - reading files
  - fetching from a database
  - waiting for a timer

## The 3 states of a Promise
- `pending`: the task is still running.
- `fulfilled`: the task finished successfully.
- `rejected`: the task failed.

## How to create a Promise
- Use `new Promise((resolve, reject) => {})`.
- `resolve()` means success.
- `reject()` means failure.

```js
const myPromise = new Promise((resolve, reject) => {
  const success = true;

  if (success) {
    resolve('Done!');
  } else {
    reject('Oops, failed.');
  }
});
```

## Simple examples

### `resolve()` example
```js
const promise = new Promise((resolve) => {
  resolve('🎉 Great!');
});

promise.then((value) => {
  console.log(value);
});
```

### `reject()` example
```js
const promise = new Promise((resolve, reject) => {
  reject('❌ Something went wrong');
});

promise.catch((error) => {
  console.error(error);
});
```

## `.then()`, `.catch()`, and `.finally()`
- `.then()` runs when the promise is fulfilled.
- `.catch()` runs when the promise is rejected.
- `.finally()` runs no matter what, after success or failure.

```js
const promise = new Promise((resolve, reject) => {
  const data = { id: 1 };

  if (data) {
    resolve(data);
  } else {
    reject('No data found');
  }
});

promise
  .then((result) => {
    console.log('Success:', result);
  })
  .catch((error) => {
    console.error('Error:', error);
  })
  .finally(() => {
    console.log('Done waiting.');
  });
```

## `Promise.all()` vs `Promise.allSettled()`
- `Promise.all()` waits for every promise to succeed.
  - If one fails, the whole thing fails.
- `Promise.allSettled()` waits for every promise to finish.
  - It gives results for both success and failure.

```js
const p1 = Promise.resolve('A');
const p2 = Promise.resolve('B');
const p3 = Promise.reject('C failed');

Promise.all([p1, p2])
  .then((values) => console.log(values));

Promise.allSettled([p1, p2, p3])
  .then((results) => console.log(results));
```

## Mental model
- Think of a Promise like a package on the way.
- First it is `pending` while the delivery is happening.
- Then it becomes either:
  - `fulfilled` if it arrives safely
  - `rejected` if it gets lost

Flow:
- pending → fulfilled (success)
- pending → rejected (failure)

## Common beginner mistakes
- Forgetting to return or use the promise value.
- Not using `.catch()` for errors.
- Mixing callbacks and promises in a confusing way.
- Assuming a promise is finished before `.then()` runs.

## What each file teaches
- `0-promise.js`: creates a simple Promise and shows how `new Promise((resolve, reject) => {})` works.
- `1-promise.js`: shows a Promise that resolves on success or rejects on failure.
- `2-then.js`: teaches using `.then()` and how promise success can return data.
- `3-all.js`: teaches `Promise.all()` with two async tasks and how one error makes the whole result fail.
- `4-user-promise.js`: shows `Promise.resolve()` to return a quick successful value.
- `5-photo-reject.js`: shows `Promise.reject()` to return a quick error.
- `6-final-user.js`: uses `.then()`, `.catch()`, and `.finally()` together.
- `7-load_balancer.js`: uses `Promise.race()` so the fastest result wins.
- `8-try.js`: shows throwing errors before a promise or async logic.
- `9-try.js`: shows `try...catch...finally` for safe code and cleanup.

## Key Takeaways
- A Promise is a tool for handling tasks that finish later.
- Use `resolve()` for success and `reject()` for failure.
- Use `.then()` for results, `.catch()` for errors, and `.finally()` for cleanup.
- `Promise.all()` needs every promise to succeed.
- `Promise.allSettled()` reports every result, even failures.
