# DiagnosisExperiments

## Cases
cases package contains scripts that perform experiments for specific cases. Data for experiments should be first
preprocessed with cleaning script and balancing_script in that particular order.

## Data preparing
data_preparing package contains method for handling missing values and balancing the data set. Not preprocessed files
should have the letter 'f' as prefix.

## Model
model package contains classification models, model configuration objects and class sample.
It contains method that can perform k-fold cross-validation and leave-one-out cross-validation for
CART decision tree and MLP ann. Although, 10-fold cross-validation proved to be ineffective for
the specific hepatitis diagnosis problem and leave-one-out cross-validation should be use to that end.

## Tools
io_handlers package contains methods that read and parse data. It also contains methods that print results as text
or plots.

Files containing data of samples should be formatted in a way: each sample is set in a separate line. Samples'
attributes should be separated by commas. The class should be the first attribute. Files containing features names
should have one feature per line. Files containing classed encoding should have only one class encoding per line
and it should consist of the class name, a coma and the class' encoding.

Initial files should be named according to a specific convention:
- data file: <prefix>_<task_name>.data
- names file: <prefix>_<task_name>.names
- classes file: <task_name>.classes
