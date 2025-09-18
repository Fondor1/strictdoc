## Description
<!-- Provide a clear and concise description of the feature you want to request. -->
Enable automatic generation of machine identifiers (MIDs) during the first import from Excel into a `.sdoc` file when a new command-line flag (`--enable-mid-auto-generation`?) is provided.

## Problem
<!-- Describe the problem or gap that this feature aims to address. Why is it needed? -->
MIDs are auto-generated when _exporting_ SDoc files if the `ENABLE_MID: True` option is present in the document’s `[OPTIONS]`.
No mechanism is available to auto-generate MID numbers during Excel _import_.
Imported documents therefore lack MID fields unless manually enabled post-import with a second export cycle.
This limitation makes conversion processes more complicated and cumbersome for users who may not understand why such a "redundant" import step is required.

## Solution
<!-- Suggest a possible solution or feature implementation. -->
- Add a `--enable-mid-on-import` (or similarly named) flag to the CLI `strictdoc import excel` command.
- Modify the import logic to:
  - Detect the flag and, if present, inject `ENABLE_MID: True` into the document’s `[OPTIONS]`.
  - Ensure the grammar used includes MID fields for relevant nodes.
  - Invoke the MID generation routine (likely the same used during `export`) immediately after import, before writing the `.sdoc` file.
- Add unit/integration tests verifying that MIDs are generated only when the flag is used.

## Additional Information
<!-- Add any other relevant details, such as dependencies, related issues, or references to similar features elsewhere. -->
This aligns with how MIDs are handled during export and in the web UI. It would streamline workflows involving Excel imports by eliminating manual steps. Also, consider updating documentation to reflect this new capability.
