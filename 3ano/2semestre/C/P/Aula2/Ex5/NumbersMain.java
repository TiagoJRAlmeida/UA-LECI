import java.io.File;
import java.io.FileInputStream;
import java.io.FileNotFoundException;
import java.io.IOException;
import java.io.InputStream;
import java.util.Scanner;

import org.antlr.v4.runtime.*;
import org.antlr.v4.runtime.tree.*;

public class NumbersMain {
   final static Scanner in = new Scanner(System.in);
   public static void main(String[] args) {
      InputStream in_stream = null;
      NumbersL numberTable = new NumbersL();
      try{
         in_stream = new FileInputStream(new File("numbers.txt"));
      }
      catch(FileNotFoundException e){
         System.err.println("ERROR: reading number file!");
         System.exit(1);
      }


      try {
         // create a CharStream that reads from standard input:
         // CharStream input = CharStreams.fromStream(System.in);
         // ^^ Alterar pelo que está a baixo, para o main receber char Streams de um ficheiro, invés de System in
         CharStream input = CharStreams.fromStream(in_stream);
         // create a lexer that feeds off of input CharStream:
         NumbersLexer lexer = new NumbersLexer(input);
         // create a buffer of tokens pulled from the lexer:
         CommonTokenStream tokens = new CommonTokenStream(lexer);
         // create a parser that feeds off the tokens buffer:
         NumbersParser parser = new NumbersParser(tokens);
         // replace error listener:
         //parser.removeErrorListeners(); // remove ConsoleErrorListener
         //parser.addErrorListener(new ErrorHandlingListener());
         // begin parsing at file rule:
         ParseTree tree = parser.file();
         if (parser.getNumberOfSyntaxErrors() == 0) {
            // print LISP-style tree:
            // System.out.println(tree.toStringTree(parser));
            ParseTreeWalker walker = new ParseTreeWalker();
            // NumbersL listener0 = new NumbersL(); <-- Perguntar o motivo de comentar isto
            // walker.walk(listener0, tree);
            // ^^ Trocar pelo que está abaixo
            walker.walk(numberTable, tree);
            }
         }
         catch(IOException e) {
            e.printStackTrace();
            System.exit(1);
         }
         catch(RecognitionException e) {
            e.printStackTrace();
            System.exit(1);
         }

         while(in.hasNextLine()){
            String line = in.nextLine();
            String processedLine = line.replace("-", " ");
            Scanner scline = new Scanner(processedLine);
            boolean first = true;
            while(scline.hasNext()) {
                  String newToken = scline.next();
                  String text = newToken.toLowerCase();
                  if (!first)
                     System.out.print(" ");
                  if (numberTable.exists(text))
                     newToken = numberTable.getValue(text).toString();
                  System.out.print(newToken);
                  first = false;
            }
            scline.close();
         }
      }
}
