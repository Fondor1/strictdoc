import argparse
import os
import sys

import html5lib
from tidylib import tidy_document

parser = argparse.ArgumentParser(description="HTML Markup validator")
parser.add_argument("input_file", type=str, help="Path to HTML file")
args = parser.parse_args()

input_file = args.input_file
if not os.path.isfile(input_file):
    sys.stdout.flush()
    err = (
        f"error: html_markup_validator: input file does not exist: {input_file}"
    )
    print(err)  # noqa: T201
    exit(1)

with open(input_file, encoding="utf8") as file:
    html_content = file.read()

errors = []
warnings = []

# Validation #1: html5parser
html5parser = html5lib.HTMLParser(strict=True)
try:
    html5parser.parse(html_content)
except Exception as e:
    errors.append(f"Error: {str(e)}")

# Validation #2: tidylib
_, tidylib_messages_string = tidy_document(
    html_content,
    options={
        "new-blocklevel-tags": (
            # HTML 5
            "main, aside, header, footer, section, article, nav, menu, details, summary, "
            # Turbo.js
            "turbo-frame, "
            # SVG
            "svg, path, line, circle, polyline, "
            # StrictDoc
            "sdoc-scope, "
            "sdoc-autogen, "
            "sdoc-anchor, "
            "sdoc-menu, sdoc-menu-handler, sdoc-menu-list, "
            "sdoc-node, "
            "sdoc-node-controls, "
            "sdoc-node-content, "
            "sdoc-node-uid, "
            "sdoc-node-title, "
            "sdoc-node-field, "
            "sdoc-node-field-label, "
            "sdoc-text, "
            "sdoc-section, "
            "sdoc-section-title, sdoc-section-text, "
            "sdoc-main-placeholder, "
            "sdoc-main-legend, "
            "sdoc-meta, sdoc-meta-label, sdoc-meta-field, "
            "sdoc-form, sdoc-form-grid, "
            "sdoc-form-header, sdoc-form-descr, sdoc-form-footer, "
            "sdoc-form-row, sdoc-form-row-main, sdoc-form-row-aside, "
            "sdoc-form-field, sdoc-form-field-group, "
            "sdoc-form-error, "
            "sdoc-contenteditable, "
            "sdoc-autocompletable, "
            "sdoc-tabs, sdoc-tab, sdoc-tab-content, "
            "sdoc-backdrop, sdoc-modal, "
            "sdoc-modal-container, sdoc-modal-message, "
            "sdoc-modal-header, sdoc-modal-content, sdoc-modal-footer, "
            "sdoc-field, sdoc-field-content, sdoc-field-service, "
            "template, "
        ),
        "char-encoding": "utf8",
        "input-encoding": "utf8",
        "output-encoding": "utf8",
        "drop-proprietary-attributes": "no",
        "show-warnings": False,
    },
)

for message in tidylib_messages_string.split("\n"):
    if "Error: " in message:
        errors.append(message)
    elif "Warning: " in message:
        warnings.append(message)

MESSAGE_PREFIX = "HTML markup validation COMPLETED"

if len(errors) > 0 or len(warnings) > 0:
    for message in warnings + errors:
        print(message)  # noqa: T201

    print(  # noqa: T201
        f"{MESSAGE_PREFIX}: "
        f"{input_file}: {len(errors)} errors, {len(warnings)} warnings."
    )

    if len(errors) > 0:
        exit(1)
    else:
        exit(0)
else:
    print(f"{MESSAGE_PREFIX}: {input_file}: 0 errors, 0 warnings.")  # noqa: T201
