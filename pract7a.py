#Implementation of Constraints Satisfaction Problem 

#Python Code:
from simpleai.search import CspProblem, backtrack
from simpleai.search.csp import (
    HIGHEST_DEGREE_VARIABLE,
    LEAST_CONSTRAINING_VALUE,
    MOST_CONSTRAINED_VARIABLE,
)

variables = ("WA", "NT", "SA", "Q", "NSW", "V", "T")
domains = dict((v, ["red", "green", "blue"]) for v in variables)

def const_different(variables, values):
    return values[0] != values[1]

constraints = [
    (("WA", "NT"), const_different),
    (("WA", "SA"), const_different),
    (("NT", "SA"), const_different),
    (("NT", "Q"), const_different),
    (("SA", "Q"), const_different),
    (("SA", "NSW"), const_different),
    (("SA", "V"), const_different),
    (("Q", "NSW"), const_different),
    (("NSW", "V"), const_different),
]
my_problem = CspProblem(variables, domains, constraints)

# Execution block (calling backtrack with different heuristics)
print(backtrack(my_problem))
print(backtrack(my_problem, variable_heuristic=MOST_CONSTRAINED_VARIABLE))
print(backtrack(my_problem, variable_heuristic=HIGHEST_DEGREE_VARIABLE, value_heuristic=LEAST_CONSTRAINING_VALUE))
print(backtrack(my_problem, variable_heuristic=MOST_CONSTRAINED_VARIABLE, value_heuristic=LEAST_CONSTRAINING_VALUE))
print(backtrack(my_problem, variable_heuristic=HIGHEST_DEGREE_VARIABLE, value_heuristic=LEAST_CONSTRAINING_VALUE))
print(min_conflicts(my_problem)) # Note: min_conflicts is generally imported separately and often not used with standard backtrack search