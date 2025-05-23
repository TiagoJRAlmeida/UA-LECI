grammar Calculator;
program: stat* EOF;
stat: 
    expr? NEWLINE        #StatExpr
|   assigment? NEWLINE   #StatAssigment
;

assigment: ID '=' expr;

expr:
    op=('+'|'-') expr           #ExprUnary
|   expr op=('*'|'/'|'%') expr  #ExprMultDivMod
|   expr op=('+'|'-') expr      #ExprAddSub
|   '(' expr ')'                #ExprParent
|   ID                          #ExprId
|   INTEGER                     #ExprInteger
;


ID: [a-zA-Z_]+;
INTEGER: [0-9]+;
NEWLINE: '\r'? '\n';
WS: [ \t]+ -> skip ;
COMMENT: '#' .*? '\n' -> skip;