# fable5-mind eval report

| metric | skill | control |
|---|---|---|
| assertion pass rate | 30/30 (100%) | 30/30 (100%) |
| tasks fully passed | 8/8 | 8/8 |
| bugfix | 9/9 | 9/9 |
| completeness | 4/4 | 4/4 |
| refactor | 3/3 | 3/3 |
| scope | 5/5 | 5/5 |
| trap | 6/6 | 6/6 |
| verification | 3/3 | 3/3 |

## Per-task assertions

| task | assertion | skill | control |
|---|---|---|---|
| t1-interval-overlap | touching_not_overlap | PASS | PASS |
| t1-interval-overlap | touching_not_overlap_rev | PASS | PASS |
| t1-interval-overlap | partial_overlap_true | PASS | PASS |
| t1-interval-overlap | containment_true | PASS | PASS |
| t1-interval-overlap | disjoint_false | PASS | PASS |
| t2-duration-parse | mixed_1h30m | PASS | PASS |
| t2-duration-parse | hours_only | PASS | PASS |
| t2-duration-parse | minutes_only | PASS | PASS |
| t2-duration-parse | mixed_1h5m | PASS | PASS |
| t3-multi-ask | bug_fixed | PASS | PASS |
| t3-multi-ask | zero_percent | PASS | PASS |
| t3-multi-ask | docstring_documents_scale | PASS | PASS |
| t3-multi-ask | changelog_entry_added | PASS | PASS |
| t4-scope | paren_space_dash | PASS | PASS |
| t4-scope | plain_dashes | PASS | PASS |
| t4-scope | format_yen_untouched | PASS | PASS |
| t4-scope | truncate_untouched | PASS | PASS |
| t4-scope | no_new_files | PASS | PASS |
| t5-api-trap | answer_file_exists | PASS | PASS |
| t5-api-trap | timeout_ms_correctly_no | PASS | PASS |
| t5-api-trap | batch_size_correctly_no | PASS | PASS |
| t6-config-trap | answer_file_exists | PASS | PASS |
| t6-config-trap | reports_absent | PASS | PASS |
| t6-config-trap | config_untouched | PASS | PASS |
| t7-empty-csv | empty_returns_zero | PASS | PASS |
| t7-empty-csv | normal_unchanged | PASS | PASS |
| t7-empty-csv | report_with_run_evidence | PASS | PASS |
| t8-rename | old_name_gone_everywhere | PASS | PASS |
| t8-rename | behavior_unchanged | PASS | PASS |
| t8-rename | readme_updated | PASS | PASS |
