# Git Sizer Max Blob Size
A script to filter a folder containing repo based git sizer data to list the top 10 largest blobs.

## Example Usage

```bash
❯ python3 gsmbs.py ~/Downloads/git_sizer
2024-11-18 13:10:06,470 - INFO - Getting files in directory: /Users/bastian.rueland/Downloads/git_sizer
2024-11-18 13:10:06,479 - INFO - Filtering for maxBlobSize from git-sizer files
2024-11-18 13:10:10,237 - INFO - 10 biggest, unique sorted blobs (DESC):
2900948792 bytes -> 2900.95 MB
2304723456 bytes -> 2304.72 MB
1325402393 bytes -> 1325.40 MB
957603840 bytes -> 957.60 MB
942058408 bytes -> 942.06 MB
707402128 bytes -> 707.40 MB
643466850 bytes -> 643.47 MB
601816067 bytes -> 601.82 MB
591098560 bytes -> 591.10 MB
536870896 bytes -> 536.87 MB
```