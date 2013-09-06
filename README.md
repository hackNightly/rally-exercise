```python
import templar

vars = {'name': 'Darrell', 'age': 26, 'occupation': 'javascript ninja'}
template = 'Hi my name is ${name}! I am ${age} years old and I consider myself to be a ${occupation}.'

sentence = templar.parse(vars, template)
print sentence

# >> 'Hi my name is Darrell! I am 26 years old and I consider myself to be a javascript ninja.'
```

Run Test Sute
```
python test.py
```
