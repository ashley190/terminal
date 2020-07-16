import textwrap

text = "Pinot Noir is a dry, light-bodied red that has a higher acidity and a soft, smooth, low-tannin finish. It is considered a lighter bodied red that is fruity and floral."

text = textwrap.fill(text, width=70)

print(text)
