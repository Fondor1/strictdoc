## Description
<!-- Provide a clear and concise description of the feature you want to request. -->
Allow users to provide an existing grammar file (e.g., `.sgra`) to be used during Excel import, avoiding automatic generation of a grammar based on Excel headers.

## Problem
<!-- Describe the problem or gap that this feature aims to address. Why is it needed? -->
Currently, importing from Excel attempts to infer a grammar from sheet headers and embeds this into the output `.sdoc` file. This prevents reuse of custom grammars and requires post-import cleanup or manual grammar insertion.

## Solution
<!-- Suggest a possible solution or feature implementation. -->
- Add a flag to the import command, such as `--grammar-file existing.grammar.sgra`.
- Modify import logic:
  - If the flag is provided, skip header-based grammar inference.
  - Load and parse the specified grammar file.
  - Set the document’s grammar to the imported one using the `IMPORT_FROM_FILE: ...` syntax in the `[GRAMMAR]` section.
- Ensure output `.sdoc` reflects the external grammar reference rather than embedding a generated grammar.
- Add tests verifying:
  - Import using `--grammar-file` produces a document that respects the provided grammar.
  - Grammar is referenced via `IMPORT_FROM_FILE`, not duplicated inline.
  - The flag overrides header inference without breaking other import behaviors.

## Additional Information
<!-- Add any other relevant details, such as dependencies, related issues, or references to similar features elsewhere. -->
This leverages existing SDoc support for external grammars (e.g., `[GRAMMAR] IMPORT_FROM_FILE: grammar.sgra`) and simplifies workflows where custom grammar consistency is essential across documents. It also avoids grammar drift during Excel conversions.
