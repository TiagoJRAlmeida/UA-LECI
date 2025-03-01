import java.util.Iterator;

@SuppressWarnings("CheckReturnValue")
public class Execute extends HelloBaseVisitor<String> {
   @Override public String visitGreetings(HelloParser.GreetingsContext ctx) {
      // String res = null;
      String name = visit(ctx.name());
      System.out.println(String.format("Olá " + name));
      return name;
      //return visitChildren(ctx);
      //return res;
   }

   @Override public String visitBye(HelloParser.ByeContext ctx) {
      // String res = null;
      String name = visit(ctx.name());
      System.out.println(String.format("Adeus " + name));
      return name;
      //return visitChildren(ctx);
      //return res;
   }

   @Override public String visitName(HelloParser.NameContext ctx) {
      String res = "";
      Iterator<HelloParser.WordContext> iterator = ctx.word().iterator();

      while(iterator.hasNext()) {
         res += (res.isEmpty() ? "" : " ") + visit(iterator.next());
      }
      // return visitChildren(ctx);
      return res;
   }

   @Override public String visitWord(HelloParser.WordContext ctx) {
      // String res = null;
      // return visitChildren(ctx);
      return ctx.ID().getText();
      //return res;
   }
}
