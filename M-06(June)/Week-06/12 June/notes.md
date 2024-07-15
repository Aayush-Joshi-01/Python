# Memory Management In Python
## Garbage Collection is done using the method of reference counting
## Two Problems for not implementing memory management are:
- **Forgetting to Free Up the Memory**
- **Freeing Memory Too Soon**
## Memory Leak Problem:
### Occurs when memory that is no longer needed and is forgotten to be released causes memory leaks, happens when objects are not garbage collected.
## Preventing Memory Leak
1. Properly manage resources/references: Use the concept of context managers(with statements) or make sure to close the db connection, files,network sockets, etc.
2. Avoid Circular references: is a situation similar to deadlock
3. Using Garbage Collection Strategies: we can manually release references using garbage references by importing `gc`and doing `gc.collect()` or let the python automatic gc to work.
### Python uses Automatic Memory management strategies with automatic garbage collection
