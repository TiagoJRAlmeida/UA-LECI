grammar Calculator;

main: stat* EOF;

stat: 
    expr? NEWLINE       #StatExpr
  | assigment? NEWLINE  #StatAssigment
  ;

assigment: ID '=' e=expr;

expr:
    op=('+' | '-') e=expr                 #ExprUnary
  | e1=expr op=('*' | '/' | '%') e2=expr  #ExprMultDivMod
  | e1=expr op=('+' | '-') e2=expr        #ExprAddSub
  | INTEGER                               #ExprInteger
  | ID                                    #ExprId
  | '(' e=expr ')'                        #ExprParent
  ;

ID: [a-zA-Z_]+;
INTEGER: [0-9]+;
NEWLINE: '\r'? '\n';
WS: [ \t]+ -> skip;
COMMENT: '#' .*? '\n' -> skip;