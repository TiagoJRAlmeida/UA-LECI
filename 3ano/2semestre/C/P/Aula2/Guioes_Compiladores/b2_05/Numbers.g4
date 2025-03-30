grammar Numbers;

file: line* EOF;

line : NUM '-' NAME NEWLINE;
NUM: [0-9]+;
NAME: [a-zA-Z]+;
NEWLINE: '\r'? '\n';
WS: [ \t]+ ->skip;