# Clean Panda
 An object-oriented program which allows you to clean the pandas dataframe in an intuitive and easy way.
 
#### Installation

```shell
$ pip install clean-panda
```

## Basic Usage

```python
df = {'name': ['Olivia', 'Dean', 'Alex', 'Jon', 'Tom', 'Jane', 'Kate'],
      'age': [32, 23, 45, 35, 20, 28, 55],
      'sex': ['female', 'male', 'male', 'male', 'male', 'female', 'female']}

clean = Cleaner(df)
print(clean.data.frame)

0         name  age     sex
1    0  Olivia   32  female
2    1    Dean   23    male
3    2    Alex   45    male
4    3     Jon   35    male
5    4     Tom   20    male
6    5    Jane   28  female
7    6    Kate   55  female

clean.normalize_text(['name', 'sex'])
print(clean.data.frame)

0         name  age     sex
1   0  OLIVIA   32  FEMALE
2   1    DEAN   23    MALE
3   2    ALEX   45    MALE
4   3     JON   35    MALE
5   4     TOM   20    MALE
6   5    JANE   28  FEMALE
7   6    KATE   55  FEMALE

```

## Structure

├── **cleaner**
    ├── normalize_text
    ├── remove_features
    ├── keep_features
    ├── remove_duplicates
    ├── remove_na
    ├── replace_str
    ├── replace_values
    ├── rename_column
    ├── sort_data
    ├── convert
    ├── apply_row_rule
    ├── apply_rule_out
    ├── apply_rule
    ├── merge_data
    ├── remove_by_condition
    ├── keep_by_condition
    ├── keep_what_is_in
    ├── round_data
    ├── operator_feat
    ├── map_data
    ├── get_cluster_by_label
    ├── remove_by_cluster
    ├── **data**
        ├── get_fetch
        ├── import_csv
        ├── import_json
        ├── duplicate_data
        ├── append_data
        ├── export_to_csv
        ├── export_to_json
        ├── export_to_xlsx
        ├── get_value
        ├── get_rows
        ├── get_filter_by_values
        ├── **frame** 
        │   ├── pd_methods
    
## License

MIT License