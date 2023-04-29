import curses 
import custom_windows as cw
 

#
# editor()
#
# usage:
#   The main goal of this module in general is to create a convenient way to edit text documents and manage user input while using python_curses 
#   module. The editor() function creates an easily customizable text editor window. It accepts arguments in the following order:
#                               1) winy ------------- width of the editor window
#                               2) winx ------------- height of the editor window
#                               3) ygap ------------- gap between the top of the editor window and the screen border
#                               4) xgap ------------- gap between the right side of the editor window and the screen border
#                               5) filename --------- has the value of "None" by default
#                               6) add_header ------- "False" by default, Pass "True" to add a window header
#                               7) header_text ------ messenge to be displayed in the header
#                               8) add_numbers ------ adds numeration, "False" by default
#                               9) add_shaddow ------ adds shaddow to the right side of the editor window, "False" by default
#                              10) text_color ------- accepts values from 0 to 5 
#                              11) border_color ----- accepts values from 0 to 5
#                              12) header_color ----- accepts values from 0 to 5
#                              13) shadow_color ----- accepts values from 0 to 5
#                              14) number_color ----- accepts values from 0 to 5
#
# functionality:
#   The editor supports utf-8 encoding, although I couldn't figure out how to make curses recognise cyrillic characters yet. I'll solve this 
#   problem in the near future. There are two ways to move cursor around the screen: arrow keys and Alt + h\j\k\l key combinations.
#   The latter one is bug free, wheras the arrow keas overload the script, because of the keystroke buffering. There are some 
#   basic editor features available via Alt key combinations:
#                                ~ Alt + s ---------- returns string of characters, as shown in an example below
#                                ~ Alt + q ---------- puts cursor at the top of the document
#                                ~ Alt + w ---------- puts cursor at the bottom of the document
#                                ~ Alt + o ---------- clears the line to the left of the cursor
#                                ~ Alt + p ---------- clears the line to the right of the cursor
#                                ~ Alt + a ---------- puts the cursor at the beginning of the current string
#                                ~ Alt + , ---------- fast scroll left 
#                                ~ Alt + . ---------- fast scroll right
#                                ~ Alt + v ---------- paste from the clipboard
# example:
#   Here's an example of editor() function. If script returns error, making the window smoller might help. If it crushes while scrolling, 
#   that's the keystroke buffering, use Alt key combinations to scroll the text, moving between the lines should still work fine.

text = cw.editor(10, 50, 10, 10, None, True, 'type something, than press Alt + s to save', True, True, 3, 3, 0, 2, 4)
cw.erase()#~~~clearing the screen~~~#

# text()
#
# usage:
#   This function displays a simple scrollable text window, which can be closed by typing 'q'. The function accepts arguments in the following order:
#                               1) winy ------------- width of the editor window
#                               2) winx ------------- height of the editor window
#                               3) ygap ------------- gap between the top of the editor window and the screen border
#                               4) xgap ------------- gap between the right side of the editor window and the screen border
#                               5) text ------------- text to be displayed
#                               6) text_color ------- accepts values from 0 to 5
#                               7) add_shadow ------- adds shaddow to the right side of the editor window, "False" by default
#                               8) shadow_color ----- accepts values from 0 to 5

cw.text(len(text.split()) + 6, len(max(text.split(), key=len)), 5, 50, "Here's the text you just typed:\n\n{}\nPress 'Q' to exit".format(text), 3, True, 2)

# alert()
#
# usage:
#   The alert function shows a sting of text, than returns ether "True" (if "Enter" key is pressed) or "False" (if any other key is pressed).
#   Function accepts arguments in the following order:
#                               1) winy ------------- width of the editor window
#                               2) winx ------------- height of the editor window
#                               3) ygap ------------- gap between the top of the editor window and the screen border
#                               4) xgap ------------- gap between the right side of the editor window and the screen border
#                               5) messenge --------- a question to be displayed
#                               6) add_shadow ------- adds shaddow to the right side of the editor window, "False" by default 
#                               7) shadow_color ----- accepts values from 0 to 5
#                               8) text_color ------- accepts values from 0 to 5

condition = cw.alert(5, 80, 10, 15, 'Press Enter to return to return "True" Any other key will return "False".', True, 2, 3)
cw.erase()
cw.text(7, 60, 5, 10, "You chose:\n\n{}\n\nPress 'Q' to exit".format(condition), 3, True, 2)

# options()
#
# usage:
#   This function accepti a list, displays it on the screen, than returns a relative position of the chosen item in the list. The list is static and not 
#   scrollable, all the dimentions are automatically chosen. Function accepts arguments in the following order:
#                               1) ygap ------------- gap between the top of the editor window and the screen border
#                               2) xgap ------------- gap between the right side of the editor window and the screen border
#                               3) header ----------- messenge to be displayed in the header
#                               4) add_shadow ------- adds shaddow to the right side of the editor window, "False" by default 
#                               5) shadow_color ----- accepts values from 0 to 5
#                               6) text_color1 ------ the default color
#                               7) text_color2 ------ color in the choosing posiyion
#                               8) header_color ----- accepts values from 0 to 5

option1 = cw.options(10, 10, 'chose something:', ['option 1', 'option 2', 'option 3'], True, 2, 3, 5, 3)
cw.erase()
cw.text(7, 60, 5, 10, "The position of the chosen item is:\n\n{}\n\nPress 'Q' to exit".format(option1), 3, True, 2)

# optionsscrl()
#
# usage:
#   Does the same thing as the options() function, except you choose the y-size of the window. The contents of the window can be scrolled using arrow keys:
#   Function has one additional argument in the beginning - the y-size of the window.

option2 = cw.optionsscrl(6, 10, 10, 'chose something:', ['option 1', 'option 2', 'option 3', 'option 4', 'option 5', 'option 6', 'option 7', 'option 8', 'option 9'], True, 2, 3, 5, 3)
cw.erase()
cw.text(7, 60, 5, 10, "The position of the chosen item is:\n\n{}\n\nPress 'Q' to exit".format(option2), 3, True, 2)



