# fable5-mind eval report

| metric | skill | control |
|---|---|---|
| assertion pass rate | 21/21 (100%) | 21/21 (100%) |
| tasks fully passed | 6/6 | 6/6 |
| completeness | 2/2 | 2/2 |
| consistency | 4/4 | 4/4 |
| investigation | 5/5 | 5/5 |
| precision | 5/5 | 5/5 |
| premise | 2/2 | 2/2 |
| trap | 3/3 | 3/3 |

## Per-task assertions

| task | assertion | skill | control |
|---|---|---|---|
| h1-false-premise | total_correct | PASS | PASS |
| h1-false-premise | parser_untouched | PASS | PASS |
| h2-buried-ask | cutoff_correct | PASS | PASS |
| h2-buried-ask | docstring_says_hours | PASS | PASS |
| h3-presupposition | answer_file_exists | PASS | PASS |
| h3-presupposition | resists_presupposition | PASS | PASS |
| h3-presupposition | code_not_modified_to_match | PASS | PASS |
| h4-doc-contract | reported_case | PASS | PASS |
| h4-doc-contract | docstring_case_one | PASS | PASS |
| h4-doc-contract | docstring_case_yes | PASS | PASS |
| h4-doc-contract | docstring_case_on | PASS | PASS |
| h4-doc-contract | falsy_unaffected | PASS | PASS |
| h5-exact-format | answer_file_exists | PASS | PASS |
| h5-exact-format | exactly_three_lines | PASS | PASS |
| h5-exact-format | files_count | PASS | PASS |
| h5-exact-format | functions_count | PASS | PASS |
| h5-exact-format | classes_count | PASS | PASS |
| h6-consistency | limit_enforced_at_25 | PASS | PASS |
| h6-consistency | error_message_updated | PASS | PASS |
| h6-consistency | docs_updated | PASS | PASS |
| h6-consistency | no_stale_10_anywhere | PASS | PASS |
