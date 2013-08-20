** Rally Code Excersize

Hi Rally devs! That was a super fun project, I'm looking forward to chatting more about it. 

I chose project #5, write some code that can be used in a templating engine, because it was the one that I felt I could most relate to having dealt with many different templating engines on the front-end. I chose Python simply for the ease of writing unit tests and running the program.

cd Rally Exercise

```python
import templar

vars 		 = {'name': 'Darrell', 'age': 26, 'occupation': 'javascript ninja'}
template = 'Hi my name is ${name}! I am ${age} years old and I consider myself to be a ${occupation}.'

sentence = templar.parse(vars, template)
print sentence

# >> 'Hi my name is Darrell! I am 26 years old and I consider myself to be a javascript ninja.'
```
