grammar generalGrammar;

main: (stat)* EOF;

stat: 
    print       #StatPrint
  | assigment   #StatAssigment
  ;

print: 'print' string;

assigment: VARNAME ':' string;

string: '"' .+? '"';

ID: [a-zA-Z]+;
VARNAME: ID+ (ID | NUMBER)*;
NUMBER: [0-9]+;
WS: [ \r\n\t]+ -> skip;
COMMENTS: '//' .*? '\n' -> skip;