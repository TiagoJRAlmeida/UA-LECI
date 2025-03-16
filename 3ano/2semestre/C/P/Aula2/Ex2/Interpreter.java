@SuppressWarnings("CheckReturnValue")
public class Interpreter extends SuffixCalculatorBaseVisitor<Double> {

   @Override public Double visitStat(SuffixCalculatorParser.StatContext ctx) {
      Double res = visit(ctx.expr());
      if(res != null){
         System.out.println(res);
      }
      return res;
   }

   @Override public Double visitExprNumber(SuffixCalculatorParser.ExprNumberContext ctx) {
      return Double.parseDouble(ctx.Number().getText());
   }

   @Override public Double visitExprSuffix(SuffixCalculatorParser.ExprSuffixContext ctx) {
      Double res = null;
      Double e1 = visit(ctx.expr(0));
      Double e2 = visit(ctx.expr(1));
      String op = ctx.op.getText();

      if(e1 != null && e2 != null){
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

            default:
               break;
         }
      }

      return res;
   }
}
