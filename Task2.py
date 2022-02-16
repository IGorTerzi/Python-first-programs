
import re

text= input("Enter IP adress: ")

import ipaddress
 
def check_ip(text):
    try:
        ipaddress.ip_address(text)
    except ValueError:
        return False
    else:
        return True
print(check_ip(text))


replace_values={".": "[.]"}


def replace_SI(text, replace_values):
  for i, j in replace_values.items():
   text = text.replace(i, j)
  return text

replacedText = replace_SI(text, replace_values)

print("Corrupted IP adress: ", replacedText)
