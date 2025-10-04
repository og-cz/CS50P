# CS50p Week 7

- [Regular expressions](#regular-expressions)
- [re library](#re-library)
- [Regular expression patterns](#regular-expression-patterns)
  - [Logic](#logic)
- [Special sequence](#special-sequence)
- [Matching start and end](#matching-start-and-end)
- [Set of characters](#set-of-characters)
- [Character classes](#character-classes)
- [Flags](#flags)
- [Groups](#groups)
- [Capturing groups](#capturing-groups)
- [Walrus operator](#walrus-operator)
- [re.sub](#re.sub)
- [re.search](#re.search)

### regular expressions

- regexes - its literally just a pattern to match some kind of data, if we typed and email we must validate that we did type and email
- we must create a pattern to match with

### re library

a library for regex with alot of functionalities

famous function in this library
re.search(pattern, string, flags=0)

- pattern = regex
- string actual string

### regular expression patterns

| Pattern | Meaning                          | Example                                              |       |                              |
| ------- | -------------------------------- | ---------------------------------------------------- | ----- | ---------------------------- |
| `.`     | Any character except newline     | `"a.c"` matches `"abc", "a1c"`                       |       |                              |
| `\d`    | Digit `[0-9]`                    | `\d+` matches `"123"`                                |       |                              |
| `\D`    | Non-digit                        | `\D+` matches `"abc"`                                |       |                              |
| `\w`    | Word character `[a-zA-Z0-9_]`    | `\w+` matches `"hello_123"`                          |       |                              |
| `\W`    | Non-word character               | `\W+` matches `"!@#"`                                |       |                              |
| `\s`    | Whitespace (space, tab, newline) | `\s+` matches `" "`                                  |       |                              |
| `\S`    | Non-whitespace                   | `\S+` matches `"hello"`                              |       |                              |
| `^`     | Start of string                  | `^Hello` matches `"Hello world"`                     |       |                              |
| `$`     | End of string                    | `world$` matches `"Hello world"`                     |       |                              |
| `*`     | 0 or more repetitions            | `a*` matches `""`, `"a"`, `"aaa"`                    |       |                              |
| `+`     | 1 or more repetitions            | `a+` matches `"a"`, `"aaa"`                          |       |                              |
| `?`     | 0 or 1 repetition                | `a?` matches `""` or `"a"`                           |       |                              |
| `{n}`   | Exactly n repetitions            | `a{3}` matches `"aaa"`                               |       |                              |
| `{n,m}` | Between n and m repetitions      | `a{2,4}` matches `"aa"`, `"aaa"`, `"aaaa"`           |       |                              |
| `[]`    | Character set                    | `[abc]` matches `"a"` or `"b"` or `"c"`              |       |                              |
| `[^ ]`  | Negated set                      | `[^abc]` matches anything except `"a"`, `"b"`, `"c"` |       |                              |
| \`      | \`                               | OR                                                   | \`cat | dog`matches`"cat"`or`"dog"\` |
| `()`    | Grouping                         | `(abc)+` matches `"abc"`, `"abcabc"`                 |       |                              |

#### logic

- ".+@.+" this is equivalent to ".._@.._" -> because this ( .. ) implies any character and another any charater with 0 or more

this is check using machine like finite machine in automata

### special sequence

- r = makes raw string meaning keep the original form as it is
- \ = backlash makes either escape character or special sequence or it makes you say not to treate the next \ -> as a special symbol

### matching start and end

^ -> matchest literal start of a string

$ -> matches the ned of a string or just before the new line at the end of a string
example:

> pattern = r"^Hello.\*world$"

- ^Hello → starts with "Hello"
- .\* → any characters in between
- world$ → ends with "world"

### set of characters

we can use square brackets inside the pattern
and inside this is one or more characters we want to look for specifically

[ ] -> set of characters
[^] -> complementing the set

- [abc] → matches a single a, b, or c
- [^abc] → the ^ at the start inside brackets means NOT those characters → matches anything except a, b, or c

### character classes

A character class is written inside square brackets [...].
It means: “match ONE character from this set.”

| Shorthand | Meaning                          | Equivalent       |
| --------- | -------------------------------- | ---------------- |
| `\d`      | Digit                            | `[0-9]`          |
| `\D`      | Non-digit                        | `[^0-9]`         |
| `\w`      | Word char (letter, digit, `_`)   | `[A-Za-z0-9_]`   |
| `\W`      | Non-word char                    | `[^A-Za-z0-9_]`  |
| `\s`      | Whitespace (space, tab, newline) | `[ \t\n\r\f\v]`  |
| `\S`      | Non-whitespace                   | `[^ \t\n\r\f\v]` |

### flags

Flags in Python’s re module are options you can pass to re.search(), re.match(), re.findall(), etc. to change how the regex works.
re.search(pattern, string, flags=0)

re.IGNORECASE
re.MULTILINE
re.DOTALL

### groups

A|B -> either A or B
(...) -> a group
(?:...) -> non-capturing version -> not saved in .group()

example:

- (cat|dog) → Match either “cat” or “dog”, and capture which one was matched.
- (?:cat|dog) → Match either “cat” or “dog”, but do not capture it (just for logic).
- (abc)? → the whole "abc" group is optional → matches "" or "abc".

### capturing groups

when u specify a group everything will be return to you as a individual value

```python
name = "malan, david"
matches = re.search(r"^(.+), (.+)$",name)
# captured: (malan) (david)
```

### walrus operator

##### := - symbol

It was added in Python 3.8 and is officially called the assignment expression operator.

- The difference is just that with the walrus, you can assign + test in one line.
  - ✅ So the “logic” of the walrus operator is just:
  - “Assign this value, and immediately use it in place.”

example

```python
if (x := 5) > 3:
    print("yes")
What happens here:

(x := 5) → assigns 5 to x
Now Python checks: 5 > 3 → True
```

### re.sub

sub here is subtitute

re.sub() in Python is a search-and-replace function from the re (regex) module.

re.sub(pattern, repl, string, count=0, flags=0)

- pattern → regex pattern to search for.
- replacement → the text (or function) to replace matches with.
- string → the input text.
- count (optional) → how many matches to replace (default = all).
- flags (optional) → regex flags like re.IGNORECASE.

just take baby steps adding steps 1 at a time that should be our approach

### re.search

we used search because we want to find a certain string and get using group so either whatever is our input we have out own certain timeline of what we are extracting specifically from

(?: ... ) is just a non-capturing group.
It works the same as ( ... ) in terms of grouping for logic, but:

( ... ) → creates a capturing group, which shows up in .groups() or .group(1), .group(2), etc.
(?: ... ) → just groups things together for regex rules but does not capture them.
