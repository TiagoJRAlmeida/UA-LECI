@SuppressWarnings("CheckReturnValue")
public class VInterpreter extends SuffixCalculatorBaseVisitor<Double> {
   @Override public Double visitStat(SuffixCalculatorParser.StatContext ctx) {
      Double res = visit(ctx.expr());
      if (res != null){
         System.out.println(String.format("Resultado: %.1f", res));;
      }
      return res;
   }

   @Override public Double visitExprNumber(SuffixCalculatorParser.ExprNumberContext ctx) {
      Double res = Double.parseDouble(ctx.NUMBER().getText());
      return res;
   }

   @Override public Double visitExprSuffix(SuffixCalculatorParser.ExprSuffixContext ctx) {
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
}
