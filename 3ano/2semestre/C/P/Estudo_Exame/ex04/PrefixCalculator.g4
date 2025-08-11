grammar PrefixCalculator;

main: stat* EOF;

stat: expr? NEWLINE;

expr:
    op=('*' | '/' | '+' | '-') expr expr    #ExprPrefix
  | NUMBER                                  #ExprNumber
  ;

NUMBER: [0-9]+('.'[0-9]+)?;
NEWLINE: '\r'? '\n';
WS: [ \t]+ -> skip;