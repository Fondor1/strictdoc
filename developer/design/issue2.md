## Description
<!-- Provide a clear and concise description of the feature you want to request. -->
Introduce a deterministic method for auto-generating MIDs based on node content such as TITLE or UID (if available) and STATEMENT so that the same content always yields the same MID number.

## Problem
<!-- Describe the problem or gap that this feature aims to address. Why is it needed? -->
Current MID auto-generation uses random uuid.uuid4()-based values resulting in different MIDs for a given node, even when the content for that node has not changed.
This undermines tracking consistency and version control of requirement nodes across re-generations.
This is commonly encountered when customers send updated requirements as DOORs Excel spreadsheet exports; another conversion step is required to generate and then compare the resultant `.sdoc` file with the previous.

The current workaround is to NOT enable MID auto-generation, counter to the advice given in the documentation, which still appears to track diffs OK provided the UUIDs do not change.



(aside, diffs are an incredible feature and extraordinarily helpful to help identify and manage upstream changes that we have no control over.)

as not using MID numners undermines the ability for the diff compare tool to 

## Solution
<!-- Suggest a possible solution or feature implementation. -->
- Add a configuration option (e.g., `--deterministic-mid` CLI flag or an `OPTIONS: DETERMINISTIC_MID: True` setting) to toggle deterministic MID generation.
- In the MID generation function:
  - If deterministic mode is enabled, compute the MID as a hash (e.g., SHA‑256) of a concatenated string comprised of node content: `(UID or "") + TITLE + STATEMENT`.
  - Otherwise, continue to use UUID-based generation.
- Ensure existing MID generation is refactored into a reusable function callable during imports and exports.
- Add tests confirming that:
  - Identical node content produces the same MID across runs.
  - Different content produces distinct MIDs.
  - Non-deterministic behavior remains optional (disabled by default).

## Additional Information
<!-- Add any other relevant details, such as dependencies, related issues, or references to similar features elsewhere. -->
We should document that changing node content will change the MID in deterministic mode, which may affect tracking if content revisions are unintended. This feature would greatly enhance reproducibility and diff/change tracking fidelity.
