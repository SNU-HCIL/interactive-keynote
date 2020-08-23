class: left, middle

# Interactive keynote

#### SNU HCIL 

---

#### Overview
# Hello World

Hello?

1. a
2. b

---

# Class Example

```python
class Counter:
    def __init__(self):
        self._count = 0
    def incr(self):
        self._count += 1
    def decr(self):
        self._count -= 1
    @property
    def count(self):
        return self._count

counter = Counter()
counter.incr()
counter.incr()
counter.decr()
counter.incr()
print(counter.count)
```

---

# Class Example

```python
class Counter:
    def __init__(self):
        self._count = 0
    def incr(self):
        self._count += 1
    def decr(self):
        self._count -= 1
    @property
    def count(self):
        return self._count

counter = Counter()
counter.incr()
print(counter.count)
```

---

# Class Example

```python
class Counter:
    def __init__(self):
        self._count = 0
    def incr(self):
        self._count += 1
    def decr(self):
        self._count -= 1
    @property
    def count(self):
        return self._count

counter = Counter()
print(counter.count)
```