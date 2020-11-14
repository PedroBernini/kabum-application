from server import app

@app.template_filter()
def currencyFormat(value):
    value = float(value)
    return "{:,.2f}".format(value)