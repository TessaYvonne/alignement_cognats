# Design

## Add character before each character in a string

example: 

```
°bíà
```

becomes

```
°b°i°́à
```

and 

```
°b(x)íà
```

becomes

```
°b°(x)°i°́à
```

and 

```
bíà
```

remains

```
bíà
```

algorithm:

1. split text into characters
2. if first character != ° -> exit
3. set in_parens to false
4. set result to ""
5. set pointer to first character
5. if in_parens is false
   6. add ° followed by the character pointed to by pointer to result 
   6. if character = ( -> set in_parens to true
   7. move pointer to next character, go to step 5 
8. else
   9. add the character pointed to by pointer to result
   10. if character = ) -> set in_parens to false
11. return result
