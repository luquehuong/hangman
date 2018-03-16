# hangman_lib.py
# A set of library functions for use with your Hangman game
#
#
# The gallows image used by the print_hangman_image(..) function is
# copyrighted! If you use that function, your program MUST appropriately
# give credit to the internet artist sk. Have your program print out 
# something akin to "Art created by sk" at the beginning or end.

def print_hangman_image(mistakes = 6):
  """Prints out a gallows image for hangman. The image printed depends on
the number of mistakes (0-6)."""
  
  if mistakes <= 0:
    return ''' ____________________
| .__________________|
| | / /     
| |/ /  
| | /     
| |/   
| |     
| |   
| |    
| |     
| |    
| |   
| |   
| |    
| |      
| |      
| |       
| |      
""""""""""""""""""""""""|
|"|"""""""""""""""""""|"|
| |                   | |
: :                   : : 
. .                   . .)'''

  elif mistakes == 1:
    return''' ___________.._______
| .__________))______|
| | / /      ||
| |/ /       ||
| | /        ||.-''.
| |/         |/  _  \\
| |          ||  `/,|
| |          (\\\\`_.'
| |        
| |     
| |    
| |   
| |   
| |    
| |      
| |      
| |       
| |      
""""""""""""""""""""""""|
|"|"""""""""""""""""""|"|
| |                   | |
: :                   : : 
. .                   . .'''
  elif mistakes == 2:
    return''' ___________.._______
| .__________))______|
| | / /      ||
| |/ /       ||
| | /        ||.-''.
| |/         |/  _  \\
| |          ||  `/,|
| |          (\\\\`_.'
| |          -`--' 
| |          |. .|  
| |          |   |   
| |          | . |    
| |          |   |     
| |          || ||
| |      
| |      
| |       
| |      
""""""""""""""""""""""""|
|"|"""""""""""""""""""|"|
| |                   | |
: :                   : : 
. .                   . .'''
  elif mistakes == 3:
    return''' ___________.._______
| .__________))______|
| | / /      ||
| |/ /       ||
| | /        ||.-''.
| |/         |/  _  \\
| |          ||  `/,|
| |          (\\\\`_.'
| |         .-`--' 
| |        /Y . .|
| |       // |   |  
| |      //  | . |   
| |     ')   |   |     
| |          || ||
| |      
| |      
| |       
| |      
""""""""""""""""""""""""|
|"|"""""""""""""""""""|"|
| |                   | |
: :                   : : 
. .                   . .'''
  elif mistakes == 4:
    return''' ___________.._______
| .__________))______|
| | / /      ||
| |/ /       ||
| | /        ||.-''.
| |/         |/  _  \\
| |          ||  `/,|
| |          (\\\\`_.'
| |         .-`--'.
| |        /Y . . Y\\
| |       // |   | \\\\
| |      //  | . |  \\\\
| |     ')   |   |   (`
| |          || ||
| |      
| |      
| |       
| |      
""""""""""""""""""""""""|
|"|"""""""""""""""""""|"|
| |                   | |
: :                   : : 
. .                   . .'''
  elif mistakes == 5:
    return''' ___________.._______
| .__________))______|
| | / /      ||
| |/ /       ||
| | /        ||.-''.
| |/         |/  _  \\
| |          ||  `/,|
| |          (\\\\`_.'
| |         .-`--'.
| |        /Y . . Y\\
| |       // |   | \\\\
| |      //  | . |  \\\\
| |     ')   |   |   (`
| |          ||'||
| |          ||   
| |          ||   
| |          ||   
| |         / |  
""""""""""""""""""""""""|
|"|"""""""""""""""""""|"|
| |                   | |
: :                   : : 
. .                   . .'''
  else: #mistakes >= 6
    return''' ___________.._______
| .__________))______|
| | / /      ||
| |/ /       ||
| | /        ||.-''.
| |/         |/  _  \\
| |          ||  `/,|
| |          (\\\\`_.'
| |         .-`--'.
| |        /Y . . Y\\
| |       // |   | \\\\
| |      //  | . |  \\\\
| |     ')   |   |   (`
| |          ||'||
| |          || ||
| |          || ||
| |          || ||
| |         / | | \\
""""""""""|_`-' `-' |"""|
|"|"""""""\ \       '"|"|
| |        \ \        | |
: :         \ \       : : 
. .          `'       . .'''


  
