**Trigger:** In the Bash tool (zsh), `git show $REV:cms/packages/...` fails with "ambiguous argument '<sha>ms/packages/...'" — characters right after the colon vanish.

**Rule:** zsh parses `:c`, `:a`, `:h`, `:t`, `:r`, `:e`, `:l`, `:u`, `:s` … after a bare `$VAR` as history-style modifiers and eats them. Always brace the variable in revision:path arguments: `git show "${REV}:cms/packages/..."`, `git ls-tree "${REV}" -- path`. Same for `${REV}^{tree}`-style suffixes.
