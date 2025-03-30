grammar Calculator;
program: stat* EOF;

stat: assignment? NEWLINE #AssignmentStat
|expr? NEWLINE #ExprStat;

assignment: ID '=' expr;

expr: op=('+' | '-') expr #ExperUnary
| expr op=('*' | '/' | '%') expr #ExprMultDivMod 
| expr op=('+' | '-') expr #ExprAddSub
|ID               #ExprID 
| Integer #ExprInteger
| '(' expr ')' #ExprParent
;

ID: [a-zA-Z_]+;
Integer: [0-9];                 
NEWLINE: '\r'? '\n';
WS:[ \t]+ -> skip;
COMMENT:'#' .*? '\n' -> skip;