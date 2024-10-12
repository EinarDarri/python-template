# Code rules

For the git repository we have enabled branch protection for the main and staging (development) branches. This means that changes can only be made to them via pull requests and certain rules must be followed in order to merge them from said pull request.

# Note
 * `mypy.ini` must be in the root of the repo (not in any folder)

## Pull requests
 * When a new commit is made to the branch, it automatically updates the pull request with said changes
 * All comments made by reviewers on the code in the pull request must be marked as resolved before it can be merged
 * All workflows must run successfully, such as unit tests, linting and type checking

# Code style

The work flow that is currently set up are a linter and type validator for python. The rules set by the work flows must be followed in order to be able to merge a pull request
 * All Python functions must have a doc string, excluding dunder methods (eg. \_\_init\_\_()) and function overload annotations.
 * The statements **return**, **break**, **continue** and **yield** must be in their corresponding body
 * Indentation must be correct
 * Blank **except** statements (ones who do not specify an exception type that they should "catch") are not allowed
 * Class names must be in PascalCase
 * Functions and variables must be in snake\_case
 * The "exec" function is disallowed

# Type safety
 * Shows a warning when returning a value with type Any from a function declared with a non- Any return type.
 * Shows errors for missing return statements on some execution paths.
 * Shows a warning when encountering any code inferred to be unreachable or redundant after performing type analysis.
 * Disallows defining functions without type annotations or with incomplete type annotations
 * Disallows calling functions without type annotations from functions with type annotations
 * Disallows usage of generic types that do not specify explicit type parameters.
 * Reports an error whenever a function with type annotations is decorated with a decorator without annotations.
 * Disallows subclassing a value of type Any.
 * Prohibit equality checks, identity checks, and container checks between non-overlapping types.
 * Warns about casting an expression to its inferred type.

# VScode Extensions
 this repo has extensions that are recommended to install for programming in this project those extensions see `@recommended` in extensions 
