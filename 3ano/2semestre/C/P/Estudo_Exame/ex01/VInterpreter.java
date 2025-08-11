import java.util.Arrays;
import java.util.Iterator;

@SuppressWarnings("CheckReturnValue")
public class VInterpreter extends HelloBaseVisitor<String> {

   @Override public String visitGreetings(HelloParser.GreetingsContext ctx) {
      String res = visit(ctx.name());
      if (res == null){
         System.err.println("ERROR: Must pass some name");
         return res;
      }
      System.out.println("Olá " + res);
      return res;
   }

   @Override public String visitBye(HelloParser.ByeContext ctx) {
      String res = visit(ctx.name());
      if (res == null){
         System.err.println("ERROR: Must pass some name");
         return res;
      }
      System.out.println("Adeus " + res);
      return res;
   }

   @Override public String visitName(HelloParser.NameContext ctx) {
      String res = "";

      Iterator<HelloParser.WordContext> it = ctx.word().iterator();
      while(it.hasNext()){
         res += visit(it.next()) + (it.hasNext() ? " " : ""); 
      }
      
      return res;
   }

   @Override public String visitWord(HelloParser.WordContext ctx) {
      String res = ctx.ID().getText();
      if (res == null){
         System.err.println("ERROR: Must pass some String");
         return res;
      }
      return res;
   }
}
