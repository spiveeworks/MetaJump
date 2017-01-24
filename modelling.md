  
MetaJump Modelling Language (MJML)  
==================================  

This document constructs a system of notating data types in MetaJump.  

Note that given the nature of MetaJump, MJML only explains notations for the stack and for functions, since nothing else exists.  

MJML is primarily designed to demonstrate MJ idiom, so the idiom guide will refer to types using MJML, however the last section of this document, "Advanced Names", is not useful for the idiom guide, as it is specifically intended to extend MJML beyond the basic idiomata.  

Simple Types and Sequences  
==========================  

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

Empty Sequences  
---------------  

An empty sequence can be indicated with `~`.  

Pure, Modellable  
================  

A function is pure if it does not use any IO operations under any circumstances.  
A function is modellable if there is some MDML way of representing the data that it will read/modify in the stack, as well as the data that will be left/replaced after execution.  

Under these circumstances the function's type can be specified by how it will interact with the stack;  
Each of the following sequences of words will be modelled as a word sequence enclosed by parentheses:  
 * Words that it will read but will always remain untouched at the end of execution (the function's 'capture')  
 * Words that it will modify, or remove from the stack (the function's 'arguments')  
 * Words that would be placed if the modified words were thought of as removed (the function's 'return')  

Stated visually, a pure, modellable function is represented by `(CAPTURE)(ARGUMENTS)(RETURN)`  

So for example if a function took two words, let's call them A, and B, and then added A to B without removing A, this would be represented as:  
`(.)(.)(.)` because A will be left, B will be removed as arguments, and A + B will replace the arguments  

Ommissions  
----------  

Various abbreviations are possible, and are generally preferred when possible.  

First, empty parentheses are equivalent to having a tilde in the parentheses, so for example:  
`(..)()(.)` means `(..)(~)(.)`.  

A function that took two arguments and replaced one of them would be modelled as such:  
`()(..)(.)`, but an additional abbreviation is possible, when there is no capture, only two pairs of parentheses are needed:  
`(..)(.)`  

Further still, a function that takes no capture, nor arguments, can be represented by a single pair of parentheses enclosing a sequence.  
When the return values have a fixed quantity, such a function is referred to as a tuple.  
For example, a triple is a function that does not modify the stack other than to add three elements to it, and is modelled as `(...)` which is equivalent to both `()()(...)` and `()(...)`  

A function that takes no arguments, and returns no values, is represented as `()`, which cannot be abbreviated further.  

Basic Names  
===========  

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
i.e. an iterator would be here defined as a function/tuple that returns another iterator and an integer  

There are no restrictions on type recursion, but some types may be difficult to implement in any meaningful way.  

Generic Type  
------------  

Sometimes an unknown type needs to be consistent within a structure, but otherwise unknown.  
For this names can be used without definition within a structure.  

For example, a function's code could read something like:  
  `rcode [0], rcode cpush, rcode [0], rcode cpush, pop [0], pop [0], flush`,   

This takes two arguments and constructs a tuple/duple/pair, and would have type `(a, b)((a, b))`  
Notice how when the symbols are not periods, asterisks, and question marks, sequences become comma separated.  


Algebraic Value  
---------------  

Sometimes the data in a structure specifies information about other parts of that structure.  
For this reason, values themselves can be named, for algebraic constructs in other parts of a structure.  
When a name is used algebraically, it must be an algebraic value, and so the type must be an integer.  
The ways in which a name is used 'algebraically' will come up below.  

Numerals are also defined to be algebraic values, but can only take the decimal value they represent.  
This is because they can be used wherever pronumerals (named algebraic values) can be used.   

Generic and Ambiguous Sequences  
===============================  

Subsequence  
-----------  

Often times, a pattern of data structures needs to be repeated a number of times within the same sequence;  
For this, a subsequence can be wrapped in square brackets `[]` to indicate that the pattern repeats.  

The number of repetitions is specified algebraically after a colon to the right of the subsequence, for example, a basic subsequence of integers would be represented as such:  
`[.]:n`  
In this case `n` is undefined, and so in some situations a subsequence like this may be unworkable.  

Putting a place where `n` can be determined, somewhere to the right of the subsequence, will make this workable, as functions will be able to determine how many elements of the stack are in the way of what they need.  
`[.]:n, n`  
This works out identically to arrays in the Java Virtual Machine, where the first (top) element of an array is the size of that array.  

If no algebraic specifier is given to a subsequence, then the latter structure is implied:  
`[.]` is equivalent to `[.]:n, n`  

Note that a subsequence is not a function, but a notation of a part of a sequence, but may appear within a function's type.  

`list_reference: ([.])`  

Union/Variant  
-------------  

A union or variant can be used to represent multiple possible sequences of data types that could appear within a larger sequence.  
`<a|b>`  

Similar to the subsequence, algebraic values can be used to specify which option is valid:  
`<x=0:a|x=1:b>, x`  

Additionally the notation `<a|b|c|etc>:x` is short hand for `<x=0:a|x=1:b|x=2:c|x=3:etc>`  
This is called variant notation, but note that unlike the abreviation of subsequences, variants still require explicit appearance of a pronumeral.  
`<a|b>:x, x` is **not** equivalent to `<a|b>:x` nor `<a|b>`  

Note that the union `<*|.>` is equivalent to the symbol `?`  
however some fictional union of all possible functions would not be equivalent to `*`, due to the impossibility of using naming schemes described below.  

Advanced Names  
==============  

Postfix Generic Types  
---------------------  

Postfixing an entire structure or part of one with `where name: type` where name is a name and type is a data model for a word or sequence, acts as a hybrid between the 'Type Alias' concept and the 'Generic Type' concept.  
Names specified in this manner have the unique property of being consistent within any instance of the specified data structure, but not between multiple instances.  

For example,  
`[consistent] where consistent: ?`  
will be some example of `[.]` OR `[*]` but not necessarily `[?]`  

The full format is as follows:  
`FULL_STRUCTURE ::= STRUCTURE | STRUCTURE where POSTFIXES`  
`POSTFIXES ::= POSTFIX | POSTFIX; POSTFIXES`  
`POSTFIX ::= NAMES: STRUCTURE`  
`NAMES ::= NAME | NAME, NAME`  

Note that multiple names can be given the same structure, but will be independantly assigned;  
Additionally multiple sets of postfix definitions all follow the same `where `, and are semicolon separated.  

Finally each postfix can specify new names that are clarified in later postfixes.  

Alias Templates  
---------------  

A type alias can be followed by a colon separated list of algerbraic or generic names after the alias.  

Then whenever the alias is used, it must be followed by a colon-separated list of expressions/structures for each name.  

Finally specialized versions of an alias with specific values for the templated names can be defined in the postfix.  

As an example, the following are equivalent:  
`subseq: [.]:x`  
`subseq:x: .subseq:x-1 where: subseq:0: ~`  
