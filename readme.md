
MetaJump
========

MetaJump is a jump/goto based language centred around metaprogramming.

In MetaJump lots of functionalities typical to higher level languages need to be implemented in strange metaprogrammy ways, for example, a tuple is constructed by writing a function that takes no arguments and returns the desired values.

Structure
---------

Any MetaJump Virtual Machine (MJVM) contains the following internal objects:  
 * Data stack
 * Call stack
   * Function reference
   * Execution offset
 * Function heap
 * Function Buffer
 * Reverse Buffer

###Data stack

Also known as "The stack"

This is a standard stack of words. (word size typically either 8b or 16b)  
The top few entries of the stack are accessible to make life easier (maybe a tarpit version of MJ should be made?)

The stack needs to be able to hold function references as well, which typically means that function references are words, similar to pointers.

### Call stack

This is a stack containing the functions being executed, and their current execution offset.

The top function is also called `this` and the top execution offset is also called `fptr` (read: eff-pointer, function pointer)

The machine repeatedly executes operations from the top function, until the execution offset exceeds the functions actual contents, at which point the stack is popped.

### Function heap

Also known as "The heap"

Heap management is not typically a part of MJ usage, but theoretically the machine requires a heap for dynamically allocated functions.  

If function references are words, then this heap could just be an array whose size is 2^(word size)

### Function Buffer

This is used for metaprogramming operations.  
Words can be written to the buffer in runtime, and then the buffer can be flushed somewhere into the heap, creating a new callable function.

### Reverse Buffer

This second buffer exists to work around the stack reversing data sequences.  

Words can be added to the reverse buffer using similar operations, but instead of flushing into the heap, the reverse buffer is reversed and flushed into the function buffer.

Flushes of the reverse buffer occur in three places:
 * Before any additions to the function buffer
 * Before the function buffer is flushed
 * When the reverse buffer is explicitly flushed in a function (an opcode should exist for this)

Operations
----------

Although operations aren't explicitly defined while the word size is unknown, an MJVM will typically have the following:

### Stack manipulation

The stack can be manipulated using three crucial operations, one derivative operation, and two convenience operations:
 * push operations
   * const-push; get words as literals from the function data, and push them to the stack
   * push; get a word from the stack and push a copy to the top
 * pop; remove an element from the stack. If it is not the top element then subsequent elements will 'fall backwards'
 * pull/pop-push; remove an element from the stack, and replace it at the top
 * bury/insert; opposite of pull, removes the top element and inserts it deeper into the stack.
 * long-push; takes an entry from deeper in the stack and pushes it to the top.  
    Note that this operation may be the same operation as push if push already offers a large depth

### Primitive functions/math operations

These operations pop one or two elements from the stack, and then push the result of some mathematical function.

In a sense the two basic operations are increment and decrement, and theoretically other operations can be implemented in terms of these, but in practice each function is already implemented in the underlying hardware.

A useful set of functionality would be the following:
 * arithmetic
   * plus
   * minus
   * multiply
   * floor-divide
   * modulus
   * 'divmod' which performs floor divide and modulus at the same time
 * bitwise
   * AND
   * OR
   * XOR
   * left-shift
   * right-shift
 * unary
   * increment
   * decrement
   * one's complement (bitwise inverse)
   * two's complement (additive inverse)
   * logical inverse (1 if 0 else 0)

### Control Flow

#### Jump

The four basic jump operations are:
 * `JMP`; change fptr by the offset specified
 * `JEZ`; pop the top element from the stack and then perform a JMP if that element was zero
 * `JGZ`; similar but for greater than zero
 * `JLZ`; similar but for less than zero

4 compound jump operations could also exist:
 * compound comparisons
   * `JGEZ` for greater than or equal to zero
   * `JLEZ` for less than or equal to zero
   * `JNZ`  for not zero
   * `NOP`  to never jump

For completion an additional 8 jump operations can be found by implementing the above with unconventional pop semantics:
 * `JMP` or `NOP` but still pop the top element (mostly redundant, but an interesting opportunity for small optimizations)
 * `JEZ`, `JGZ`, `JLZ`, `JGEZ`, `JLEZ`, `JNZ`, but without popping the top element when it is compared to zero (can be achieved by just running push 0 first, but also an interesting opportunity for optimization)

A special operation could exist to change the execution offset by a number popped from the data stack.

Additionally another special operation should exist which pops the call stack. (return)  
This operation is implicit at the end of every function, so in effect explicit return operations are a `JMP` to the end of the function.

#### Call

The only crucial call operation pushes something from the data stack onto the call stack, but additional call operations are possible:
 * pop-call; pop top element from the data stack and push it to the call stack
 * const-call; copy a reference from the function's code to the call stack (equivalent to const-push followed by pop-call)
 * offset call; perform a call or a pcall but specify the initial execution offset (could open opportunities for more object oriented code structures, but also dramatically changes how the language is used)
 * call this; calls self
 * offset-call this; what you would expect.  
    provides the usefulness of normal subroutines without requiring new functions to be constructed on the heap

### Metaprogrammy

Words can be copied either from the current function code, or from the stack, and to either the code buffer, or the reverse buffer.
(code, ccode, rcode, rccode)

The buffer can also be flushed into a newly allocated function on the heap.  
A reference to this function will be pushed to the top of the stack.

The reverse buffer is flushed before either code, ccode, or flush are executed.  
The reverse buffer can also be manually flushed (rflush)

Finally a special operation called "this" will take the top function on the call stack and append it to the data stack; this is used for recursive systems that span multiple functions, as well as special data structure implementations such as recursive tuples.

### I/O

Words can be taken from input, and sent to output, using three operations:
 * input; takes a specified number of words from input, and pushes them to the stack
 * output; takes words from the function body and sends them to the output
 * pop-output; pops the specified word from the stack and sends it to output
