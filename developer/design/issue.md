# Deterministic auto-generated MID field

## Description

<!-- Provide a clear and concise description of the feature you want to request. -->


The MID field paradigm works well _assuming the source requirements document implements MID fields and those fields do not change_.
Our customers have never supplied us with requirements that contain an equivalent of a MID field, so we always need to generate our own MID fields.



The auto-generation capability of strictdoc is such that   




The user guide strongly recommends using MIDs for accurate diffs, but for nodes that already have UIDs it is not clear why using a hash of the UID for the MID is not sufficient for this purpose. The stated advantages from [the docs](https://strictdoc.readthedocs.io/en/stable/stable/docs/strictdoc_01_user_guide.html#6.2.4.1.1-Unique-vs-machine-identifiers-MID-vs-UID):

    Advantages of using machine identifiers:

    1. Machine identifiers provide a robust means of identifying documents, sections, requirements, or custom nodes. An MID can uniquely identify a given node, independent of other fields like UID or TITLE.
    2. MIDs increase the portability of requirements data. Even when UID naming conventions change or nodes are relocated, the MID continues to uniquely identify the original node.
    3. The unique identification of nodes via MIDs allows precise tracking of changes using StrictDoc's Diff/Changelog functionality. It allows the algorithm to accurately match requirements, sections, or document nodes, even if they are moved, renamed, or undergo metadata changes.

For non-requirement fields, I can understand why an MID would be helpful because there is not a guarantee for a unique field.



1. Tracking requirements changes between revisions by UID is reasonable unless the UIDs get renamed (at which point it's still a manual track to sync requirements between different versions)
2. MIDs are not currently determinstically generated, even for the same file 



Use case: Deterministically import requirements spreadsheets (typically a DOORS export) without a MID field to track changes over revisions

When importing a new set of requirements documentation ()

As an experiment, I relocated a requirement to a different location in the spreadsheet. The diff was able to parse




but enforcing that MIDs get added to customer requirements is not typically feasible.



As an extreme example, a customer had a requirements document (not DOORS based) where requirement numbering was auto-generated.
A requirement was added in the middle, which shifted every other requirement below that to a different number.



## Problem

<!-- Describe the problem or gap that this feature aims to address. Why is it needed? -->

1. No option within the import feature to request a MID field be auto-generated
    1. Workaround exists to re-import a previously-generated sdoc file so it generates these fields
2. MID field hashes are not deterministic when using auto-generation of MID values; currently randomly generated using python's built-in uuid4() function
    1. Customers will often send updated spreadsheets with new, removed, or changed requirements
    2. The same file imported multiple times results in unique MID fields for each making linkage between unchanged requirements unrealistic


## Solution

<!-- Suggest a possible solution or feature implementation. -->
1. Generate MID field, if requested, in the import command

## Additional Information

<!-- Add any other relevant details, such as dependencies, related issues, or references to similar features elsewhere. -->


Sorting based on UUID to make git diffs much more stable?

Right now, sdoc files are more like documentation with ordered layouts.
If each field has a LEVEL associated with it, 




Would also be helpful during import to specify that the grammar file be generated as a separate file instead of embedded in the resultant sdoc file. This supports a programmatic method of using an external grammar file that has been vetted instead of re-calculating it each time.

Ideal workflow:

1. User imports requirements file (excel spreadsheet) for the first time. Outputs:
    1. sdoc file, with deterministic MIDs
    2. grammar file
2. User gets updated requirements file with requirements changed, moved, deleted, and added.
3. User imports again, pointing `strictdoc` to the location of the existing grammar file.


I can potentially help writing something for the generation of deterministic MIDs but would need to do a bit of investigation to understand what is available to `MID.create()` when it is called to understand whether this request is currently feasible.

Import issues:

* Enable auto-generation of MIDs on first excel import with a command line flag
* Make auto-generated MID fields deterministic based on the content of the node (e.g. TITLE or UID if either exists, and STATEMENT)
* Add feature to accept an existing grammar file to use for an excel import instead of generating a new one that is embedded in the resultant converted file.
