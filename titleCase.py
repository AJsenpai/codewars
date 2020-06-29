"""
Write a function that will convert a string into title case, given an optional list of exceptions (minor words). 
The list of minor words will be given as a string with each word separated by a space. Your function should ignore the case 
of the minor words string -- it should behave in the same way even if the case of the minor word string is changed.
"""
# my solution
def title_case(title, minor_words=""):
    newtitle = ""
    for index, val in enumerate(title.split()):
        if val.lower() in minor_words.lower().split() and index != 0:
            newtitle += f"{val.lower()} "
        else:
            newtitle += f"{val.title()} "
    return newtitle.strip()




print(title_case(title="First a of in", minor_words="an often into"))
# Expected 'First A Of In' but
# print(title_case("THE WIND IN THE WILLOWS", "The In"))
# Test.assert_equals(title_case('a clash of KINGS', 'a an the of'), 'A Clash of Kings')
# Test.assert_equals(title_case('THE WIND IN THE WILLOWS', 'The In'), 'The Wind in the Willows')
# Test.assert_equals(title_case('the quick brown fox'), 'The Quick Brown Fox')

# codewars solution
def title_case(title, minor_words=""):
    return " ".join(
        c if c in minor_words.lower().split() else c.title()
        for c in title.capitalize().split()
    )