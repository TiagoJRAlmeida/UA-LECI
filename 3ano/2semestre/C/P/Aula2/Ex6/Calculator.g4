grammar Calculator;
program: stat* EOF;
stat: 
    expr? NEWLINE        #StatExpr
|   assigment? NEWLINE   #StatAssigment
;

assigment: ID '=' expr;

expr:
    op=('+'|'-') expr           #ExprUnary
|   expr  op=('*'|'/'|'%') expr #ExprMultDivMod
|   expr  op=('+'|'-') expr     #ExprAddSub
|   ID                          #ExprId
|   Integer                     #ExprInteger
|   '(' expr ')'                #ExprParent
;


ID: [a-zA-Z_]+;
Integer : [0-9]+;
NEWLINE: '\r'? '\n';
WS: [ \t]+ -> skip ;
COMMENT: '#' .*? '\n' -> skip;