
MetaJump Idiom
==============

This document is a step by step breakdown of using MJ, but is intended to be used alongside the glossary.  
Check terms in the glossary as they come up, the glossary is alphabetic, this guide is ordered by complexity.

This document will construct and use a system called MetaJump Modelling Language, (MJML) which is primarily an abstract way of representing these idiomata.

Simple and Strictly Typed Objects
=================================

Words
-----

In MJ primitve data takes the form of a word.  

In MJML the following are representations of a single word:
 * A period '`.`' represents a numeric word, an integer
 * An asterisk '`*`' represents a function, (in theory this is a word that acts as a reference to a list of operations)
 * A question mark '`?`' represents either of the above, and therefore can't be used as either.

Sequences of Words
------------------

Sections of the stack can be represented as a comma separated list of data structures.  
The elements are presented in order from the lowest in the stack to the highest.  

Commas can be removed on either side of any of the symbols mentioned so far, but as structures get more complicated, or get referred to by names, they will require commas.

Pure, Modellable
----------------

A function is pure if it does not use any IO operations under any circumstances.  
A function is modellable if there is some MDML way of representing the data that it will read/modify in the stack, as well as the data that will be left/replaced after execution.

Under these circumstances the function's type can be specified by how it will interact with the stack;  
Each of the following sequences of words will be modelled as a word sequence enclosed by parentheses:
 * Words that it will read but will always remain untouched at the end of execution (the function's 'capture')
 * Words that it will modify, or remove from the stack (the function's 'arguments')
 * Words that would be placed if the modified words were thought of as removed (the function's 'return')

So for example if a function took two words, let's call them A, and B, and then added A to B without removing A, this would be represented as:
`(.)(.)(.)` because A will be left, B will be removed, and A + B will be replaced

Whereas a function that did remove A would be modelled as such:
`()(..)(.)`

Empty sequences can be omitted from left to right, so the latter example could also be presented as `(..)(.)`  

A tuple is a function that does not take any arguments, and does not read from the stack at all, and will be represented as a single sequence wrapped in parentheses.  
A triple, for example, is a function that does not modify the stack other than to add three elements to it, and is modelled as `(...)` which is equivalent to both `()()(...)` and `()(...)`

A function that takes no arguments, and returns no values, is represented as `()`, which cannot be ommited.

Names
=====

Type Aliases
------------

Types can be aliased for clarity.
For example, the following annotation of a curry function:  
`binary: (..)(.)`  
`unary: (.)(.)`  
`curried_binary: (.)(unary)`  
`binary_curry: (binary)(curried_binary)`  
could also be represented directly as ((..)(.))((.)((.)(.)))

This also opens up the possibility of recursive type definitions, such as the following:  
`iterator: (iterator.)`  
i.e. an iterator in this case is a function that returns another iterator and an integer

There are no restrictions on type recursion, but some types may be difficult to implement in any meaningful way.

Generic Type
------------

Sometimes an unknown type needs to be consistent within a structure, but otherwise unknown.  
For this names can be used without definition within a structure.

For example, a function's code could read something like:
  `rcode [0], rcode cpush, rcode [0], rcode cpush, pop [0], pop [0], flush`, 

This takes two arguments and constructs a tuple/duple/pair, and would have type `(a, b)((a, b))`

Algebraic Value
---------------

Sometimes the data in a structure specifies information about other parts of that structure.  
For this reason, values themselves can be named, for algebraic constructs in other parts of a structure.  
When a name is used algebraically, it must be an algebraic value, and so the type must be an integer.  
The ways in which a name is used 'algebraically' will come up below.  



