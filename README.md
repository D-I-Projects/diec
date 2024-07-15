# Diec

A tool that encodes text and give out a key, that you can decode with this program too!

## Installation

```bash
pip install diec
```

# Example

<hr>

## encode()

```python
from diec.encoder import encode

encode("I love python and I love to learn new things here too! <3")
```
### Output

The Key you created : <a href="https://github.com/D-I-Projects/diec/blob/main/diec_example/key.diec">key.diec</a>

The encoded text : <a href="https://github.com/D-I-Projects/diec/blob/main/diec_example/encoded.diec">encoded.diec</a>

**Both of them will apear in your current directory**

<hr>

## decode()

```python
from diec.decoder import decode

decode() #The key.diec and encoded.diec file have to be in the same directory as the file that runs that command.
```
### Output
```bash
I love python and I love to learn new things here too! <3
```
<hr>
