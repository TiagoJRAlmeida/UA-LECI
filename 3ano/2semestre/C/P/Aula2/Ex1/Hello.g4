grammar Hello;
main: (greetings | bye)*;
greetings: 'hello' name;
bye: 'bye' name;
name: word+;
word: ID;
ID: [a-zA-Z]+;
WhiteSpace: [ \t\r\n]+ -> skip;