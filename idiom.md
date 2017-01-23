
Basic Definitions
=================

Given this language's reliance on functions over classes, some terminology is lifted from Haskell and functional languages.

Arguments
---------

Elements on the top of the stack that are potentially copied, or deleted, during the execution of a function, as well as elements higher on the stack than those.

If long-pull operations occur then the function could have hundreds of arguments and always return most of them identically.

Return Values
-------------

After removing all arguments from the stack, the return values are the entries that are replaced, including ones that are unchanged.

Capture
-------

Arguments that are always returned identically could also be described as captured values, instead of being arguments and return values.

These are alternative notations, and make no mistake, this will cause confusion.

Pure Function
-------------

A function that does not use any IO operations, under any circumstances, will be pure in the usual sense, using the above definition of arguments.

Data Structures
===============

MetaJump is capable of sophisticated data structures, however all of these structures are implemented as functions!

Tuple
-----

In MetaJump a tuple is any function that takes no arguments, (doesn't read the stack below entries it added) and does not use any IO operations.

MetaJump Modelling Notation
===========================

Basics: words, functions, strictly typed pure functions
-------------------------------------------------------

First of all a word is represented by a period. `.`  
Then a generic function reference is represented by an asterisk. `*`  

A pure function with modellable arguments and return values is specified by its arguments in parentheses followed by its return values in parentheses, from the bottom of the stack to the top.

For example a function that applies the plus operation would have the type `(..)(.)`

If a pure function takes no arguments, i.e. the function is a tuple then the first empty pair of parentheses can be excluded.
A triple of words would be represented by `(...)` which is of course equivalent to `()(...)`

Functions of course can be passed or returned, so nesting can occur; e.g.  
`binary_curry: ( (..)(.) )( (.)( (.)(.) ))`  
This example will be repeated later in a notation with more clarity.

Terms in an argument list are technically comma separated, but commas before or after a period or an asterisk are ommited.

Named types, recursive types
----------------------------

Types can be named for clarity.  
For example, the curry definition above could be clarified as follows:  
`binary: (..)(.)`  
`unary: (.)(.)`  
`curried_binary: (.)(unary)`  
`binary_curry: (binary)(curried_binary)`  

This also opens up the possibility of recursive type definitions, including the basic linked list:  
`stack: (stack.)`  
i.e. a stack is a function that returns another stack, as well as a word.


