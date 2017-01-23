
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

The top function is also called "this" and the top execution offset is also called "fptr" (read: eff-pointer, function pointer)

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
