import java.util.HashMap;

@SuppressWarnings("CheckReturnValue")
public class VInterpreter extends generalGrammarBaseVisitor<String> {
   HashMap<String, String> varMap = new HashMap<>();

   @Override public String visitStatPrint(generalGrammarParser.StatPrintContext ctx) {
      String res = visit(ctx.print());
      return res;
   }

   @Override public String visitStatAssigment(generalGrammarParser.StatAssigmentContext ctx) {
      String res = visit(ctx.assigment());
      return res;
   }

   @Override public String visitPrint(generalGrammarParser.PrintContext ctx) {
      String res = visit(ctx.string());
      System.out.println(res);
      return res;
   }

   @Override public String visitAssigment(generalGrammarParser.AssigmentContext ctx) {
      String key = ctx.VARNAME().getText();
      String value = visit(ctx.string());
      
      varMap.put(key, value);
      
      return value;
   }

   @Override public String visitString(generalGrammarParser.StringContext ctx) {
      String res = ctx.ID().getText();
      return res;
   }
}
