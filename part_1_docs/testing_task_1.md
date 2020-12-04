### Testing task 1:

# Carry out static testing on the code below.
# Comment on any errors that you see below.

Note that we are only looking for errors here.

**Not** any issues with, i.e.: 
Thinking that methods should be renamed or should be class level, or using string interpolation etc. 

These aren't errors but rather standards that vary from developer to developer. 

Only comment on errors that would stop the tests running.
 
```python 

class CardGame: # __init__ missing


  def check_for_ace(self, card):
    if card.value = 1: # double = as opposed to single required for comparison
      return True
    else  #colon missing
      return False
   

  dif highest_card(self, card1 card2): # coma after card1 missing. should be def as opposed to dif before function name
  if card1.value > card2.value: # indentaiton issue
    return card # should be car1 as opposed ot card
  else:
    return card2
  


def cards_total(self, cards): # indentation issue
  total# total shall be initiated with value 0
  for card in cards:
    total += card.value
    return "You have a total of" + total# indentation issue
  
``` # these symbols should not be here
