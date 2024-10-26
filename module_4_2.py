def test_function():
    def inner_function():
        values = "Я в области видимости функции test_function"
        print(values)
    inner_function()
    return inner_function()

test_function()






