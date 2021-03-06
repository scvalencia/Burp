# Missing arguments while processing query
ERROR_MISSING_ARGS = ('Error while parsing %s query, missing arguments. '
	'%s expects at least %d arguments, %d found.')

# The expression does not evaluates to an expresssion
ERROR_EXPRESION_EVAL = ('The given expression, does not evaluates to a relation.')

# Unbound relation
ERROR0_UNBOUND_VAR = ('Unbound variable: %s.')

# Save relation[s] error, due to file handling related error
ERROR_SAVE_FILE = ('Error while saving relation(s) inf the given file: %s.')

# Fetch relations from file
ERROR_FETCH_FILE = ('Error while fetching relations from \'%s\'.')

# Import option error
ERROR_IMPORT_OPT = ('Error while importing relation %s. %s '
	'is not a correct format.')

ERROR_IMPORT_QUERY_OPT = ('Error while importing query. %s '
	'is not a correct format.')

ERROR_IMPORT_QUERY_QUOTE = ('Error while importing query. A quote, must be given as third parameter.')

ERROR_CREATE_TYPE = ('Error while creating relation %s : %s is not a valid type.')

ERROR_CREATE_ARITY_MISMATCH = ('Error while creating relation %s. Arity of types, must be the same as '
					'arity of attributes.')

ERROR_CREATE_ARITY_ZERO = ('Error while creating relation %s : arity must be bigger than zero.')

ERROR_INSERT_MISMATCH = ('Error while inserting tuple into the %s relation. '
			'Relation\'s arity is %d, but receive a %d-tuple.')

ERROR_INSERT_TYPE = ('Error while inserting tuple into the %s relation'
			'\n\tRelation\'s type is: %s.\n\tTuple\'s type is: %s.')

ERROR_PROJECT_ATTRIBUTES = ('Error while projecting the relation, unbound attribute %s.' 
			' in the relation %s')

ERROR_TYPE_COMPATIBLE = 'Error while calculating %s. Not type-compatible relations.'

ERROR_SELECT_ATTRIBUTE = ('Error while selecting the relation. The given name: %s, '
	'is not an attribute of the %s relation.')

ERROR_SELECT_VALUE = ('Error while selecting the relation. The given expression: %s, '
	'is not an attribute of the %s relation, or a valid value.')

ERROR_SELECT_CLAUSE_TYPE1 = ('Error while selecting the relation. The given attribute: %s, '
	'has not the same type as: %s.')

ERROR_SELECT_CLAUSE_TYPE2 = ('Error while selecting the relation. The given attribute: %s, '
	'must has BOOL type')

ERROR_MALFORMED_CONDITION = ('Error while parsing the given condition. '
	'%s, does not form a valid clause.')

ERROR_UNRECOGNIZED_OPERATOR = 'Unrecognized operator or command: %s'