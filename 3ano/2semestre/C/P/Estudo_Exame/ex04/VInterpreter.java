@SuppressWarnings("CheckReturnValue")
public class VInterpreter extends PrefixCalculatorBaseVisitor<Double> {
   @Override public Double visitStat(PrefixCalculatorParser.StatContext ctx) {
      Double res = visit(ctx.expr());
      if (res != null){
         System.out.println(String.format("Resultado: %.1f", res));;
      }
      return res;
   }

   @Override public Double visitExprPrefix(PrefixCalculatorParser.ExprPrefixContext ctx) {
      Double res = 0.0;
      Double e1 = visit(ctx.expr(0));
      Double e2 = visit(ctx.expr(1));
      String op = ctx.op.getText();
      
      switch(op){
         case "*":
            res = e1 * e2;
            break;
         case "/":
            res = e1 / e2;
            break;
         case "+":
            res = e1 + e2;
            break;
         case "-":
            res = e1 - e2;
            break;
      }
      
      return res;
   }

   @Override public Double visitExprNumber(PrefixCalculatorParser.ExprNumberContext ctx) {
      Double res = Double.parseDouble(ctx.NUMBER().getText());
      return res;
   }
}
