Дан список чисел округлить их до 2 знаков после запятой.

В данном случае list comprehension создастся в памяти, но по факту там будет везде одно и то же значение.  
Но используя итератор `repeat`, можно сэкономить память

```python
import itertools

itertools.repeat(elem, n=float("inf")) 
```
- повторяет `elem` `n` раз.
