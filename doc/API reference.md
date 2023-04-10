## Handler

### Constructor

```python
Handler(symbolObject, expression, handledMode, handledFunction, *handledFunctionParams)
```

| Parameter             | Type                   | Default | Description                                                  |
| --------------------- | ---------------------- | ------- | ------------------------------------------------------------ |
| symbolObject          | `GlobalSymbol`         |         | Synchronize symbols of the domain where `expression` is from. |
| expression            | string                 |         | Python statement.                                            |
| handledMode           | int                    | 0       | Optional. Pattern for handling `expression` cases.           |
| handledFunction       | function pointer       | None    | Optional. If unexpectedness occurs, call this function.      |
| handledFunctionParams | variable argument list |         | Optional. The parameters passed in by `handledFunction`, it should be consistent with the parameter structure designed by the original function. |

### Attributes

<table>
    <tr>
    	<td><code>Handler.value</code></td>
        <td>Return the return value if there is a return value after <code>expression</code> is executed.</td>
    </tr>
    <tr>
    	<td><code>Handler.status</code></td>
        <td>Return <code>False</code> if an error occurs after <code>expression</code> execution.</td>
    </tr>
</table>


## GlobalSymbol

### Constructor

```python
GlobalSymbol(pythonFilePath, globalSymbols)
```

| Parameter      | Type   | Default | Description                                                  |
| -------------- | ------ | ------- | ------------------------------------------------------------ |
| pythonFilePath | string |         | The absolute path of the Python file where `expression` is from in `Handler`. Recommended to directly pass in the Python built-in variable `__file__`. |
| globalSymbols  | list   |         | The global scope symbols of the Python file where the `expression` is from in `Handler`. Recommended to directly pass in the Python built-in function `globals()`. |

### Attributes

<table>
    <tr>
    	<td>GlobalSymbol.path</td>
        <td>Return the absolute path of the Python file.</td>
    </tr>
    <tr>
    	<td>GlobalSymbol.name</td>
        <td>Return the name of the Python file.</td>
    </tr>
    <tr>
    	<td>GlobalSymbol.symbols</td>
        <td>Return the global scope symbols of the Python file.</td>
    </tr>
</table>