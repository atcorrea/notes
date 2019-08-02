# Flask Notes

## Creating a Project
1. pip install flask
2. Use the following snippet:
   ```python
   from flask import Flask, redirect, url_for, jsonify, request, render_template
   app = Flask(__name__)

   if __name__ == '__main__':
    app.run(debug=True) 
   ```
3. run in command line:
    ```
    python filename.py
    ```


## Defining Routes:
Use a decorator.

```python
#parameter name closed between <>
@app.route('/hello/<name>') 
def admin_greeting(name):
    return 'hello ' + name
#type restriction => int: defines that the parameter should be an integer
@app.route('/hello/<int:numb>') 
...
# declaring HTTP verbs
@app.route('/hello/', methods = ['GET', 'POST'])
```

## Returning a HTML page:

Jinga2 Framework

The Jinga2 template engine uses the following delimiters for escaping from HTML.

+ {% ... %} for Statements
+ {{ ... }} for Expressions to print to the template output
+ {# ... #} for Comments not included in the template output
+ \# ... ## for Line Statements

**.py File**
```python
from flask import Flask, render_template

@app.route('/result')
def result():
   dict = {'phy':50,'che':60,'maths':70}
   return render_template('result.html', result = dict)
```
**HTML File**
```HTML
<!DOCTYPE html>
<html lang="pt-BR">
<head>
    <title>{{ dynamicAtribbutes }}</title>
</head>
<body>
    <h1>Hello {{ name }}!</h1>
    {% if result[phy] > 50 %}
         <h2> Your result is pass!</h2>
    {% else %}
         <h2>Your result is fail</h2>
    {% endif %}

    <table border = 1>
    {% for key, value in result.iteritems() %}
       <tr>
          <th> {{ key }} </th>
          <td> {{ value }} </td>
       </tr>
    {% endfor %}
    </table>
</body>
</html>
```

## Returning json
use the jsonify method

```python
from flask import Flask, jsonify

@app.route('/hello/<int:numb>') 
def hello_numb(numb):
    return jsonify(numb,numb+1,numb+2)
```

## Redirecting
use the redirect and the url_for methods
```python
from flask import redirect, url_for

@app.route('/hello/<name>')
def hello_world(name):
    if name == 'admin':
        return redirect(url_for('admin_greeting')) #method name in the string
    else:
        return redirect(url_for('user_greeting', name = name)) #param name as second parameter

@app.route('/hello/adminMode')
def admin_greeting():
    return 'Admin Mode'

@app.route('/hello/user/<name>')
def user_greeting(name):
    return "hello " + name
```

## Linking a static file (js, css, etc.)
**static/main.js**
```js
function hello()
{
    alert("hello");
}
```
**hello.html**
```html
<script type="text/javascript" src="{{ url_for('static', filename='main.js')}}"></script>

<!--Button -->
<button onclick="hello()">APERTE</button>
```

