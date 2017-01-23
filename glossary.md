
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
