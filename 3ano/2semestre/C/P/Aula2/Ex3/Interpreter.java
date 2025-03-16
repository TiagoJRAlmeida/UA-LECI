@SuppressWarnings("CheckReturnValue")
public class Interpreter extends CalculatorBaseVisitor<Integer> {

   @Override public Integer visitStat(CalculatorParser.StatContext ctx) {
      Integer res = visit(ctx.expr());
      if(res != null){
         System.out.println(res);
      }
      return res;
   }

   @Override public Integer visitExprAddSub(CalculatorParser.ExprAddSubContext ctx) {
      Integer res = null;
      Integer e1 = visit(ctx.expr(0));
      Integer e2 = visit(ctx.expr(1));
      String op = ctx.op.getText();

      if(e1 != null && e2 != null){
         switch(op){
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

   @Override public Integer visitExprParent(CalculatorParser.ExprParentContext ctx) {
      return visit(ctx.expr());
   }

   @Override public Integer visitExprUnary(CalculatorParser.ExprUnaryContext ctx) {
      Integer res = null;
      Integer e1 = visit(ctx.expr());
      String op = ctx.op.getText();

      if(e1 != null){
         switch(op){
            case "+":
               res = e1;
               break;

            case "-":
               res = (-1) * e1;
               break;

            default:
               break;
         }
      }

      return res;
   }

   @Override public Integer visitExprInteger(CalculatorParser.ExprIntegerContext ctx) {
      return Integer.parseInt(ctx.Integer().getText());
   }

   @Override public Integer visitExprMultDivMod(CalculatorParser.ExprMultDivModContext ctx) {
      Integer res = null;
      Integer e1 = visit(ctx.expr(0));
      Integer e2 = visit(ctx.expr(1));
      String op = ctx.op.getText();

      if(e1 != null && e2 != null){
         switch(op){
            case "*":
               res = e1 * e2;
               break;

            case "/":
               res = e1 / e2;
               break;

            case "%":
               res = e1 % e2;
               break;

            default:
               break;
         }
      }

      return res;
   }
}
