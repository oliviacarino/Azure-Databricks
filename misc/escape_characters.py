# A list of examples for all escape characters in Python

backslash = "this is a backslash \\"
single_quote = 'this is a \' single quote'
double_quote = "this is a \" double quote"
ascii_bell = "this is an ASCII Bell \a thing"
ascii_backspace = "this is an ASCII Backspace \b thing"
ascii_formfeed = "this is an ASCII Formfeed \f thing"
ascii_linefeed = "this is an ASCII Linefeed \n thing"     # \n is also just known as a "new line"
char_name_uni = "this is a character named name in the Unicode database \N{BLACK SPADE SUIT}"
carriage_return = "this is a carriage return \r ASCII"
horiz_tab = "this is a horizontal tab \t ASCII"
vert_tab = "this is a vertical tab \v ASCII"
char_unicode16bit = "\uxxxx"
char_unicode32bit = "\Uxxxxxxxx"

print(
    "Test %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s" %
(backslash,
 single_quote,
 double_quote,
 ascii_bell,
 ascii_backspace,
 ascii_formfeed,
 ascii_linefeed,
 char_name_uni,
 carriage_return,
 horiz_tab,
 vert_tab,
 char_unicode16bit,
 char_unicode32bit,
 )
)
