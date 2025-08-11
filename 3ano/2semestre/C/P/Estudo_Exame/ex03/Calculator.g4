grammar Calculator;

main: stat* EOF;

stat: expr? NEWLINE;

expr:
    op=('+' | '-') expr             #ExprUnary
  | expr op=('*' | '/' | '%') expr  #ExprMultDivMod
  | expr op=('+' | '-') expr        #ExprAddSub
  | INTEGER                         #ExprInteger
  | '(' expr ')'                    #ExprParent
  ;

INTEGER: [0-9]+;
NEWLINE: '\r'? '\n';
WS: [ \t]+ -> skip;
COMMENT: '#' .*? '\n' -> skip;