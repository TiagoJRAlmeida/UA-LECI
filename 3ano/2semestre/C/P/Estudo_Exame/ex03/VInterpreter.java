@SuppressWarnings("CheckReturnValue")
public class VInterpreter extends CalculatorBaseVisitor<Integer> {
   @Override public Integer visitStat(CalculatorParser.StatContext ctx) {
      Integer res = visit(ctx.expr());
      if (res != null){
         System.out.println(String.format("Resutado: %d", res));
      }
      return res;
   }

   @Override public Integer visitExprAddSub(CalculatorParser.ExprAddSubContext ctx) {
      Integer res = null;
      Integer e1 = visit(ctx.expr(0));
      Integer e2 = visit(ctx.expr(1));
      String op = ctx.op.getText();
      
      switch(op){
         case "+":
            res = e1 + e2;
            break;
         case "-":
            res = e1 - e2;
            break;
      }
      
      return res;
   }

   @Override public Integer visitExprParent(CalculatorParser.ExprParentContext ctx) {
      Integer res = visit(ctx.expr());
      return res;
   }

   @Override public Integer visitExprInteger(CalculatorParser.ExprIntegerContext ctx) {
      Integer res = Integer.parseInt(ctx.INTEGER().getText());
      return res;
   }

   @Override public Integer visitExprUnary(CalculatorParser.ExprUnaryContext ctx) {
      Integer res = visit(ctx.expr());
      String op = ctx.op.getText();
      
      if(op.equals("-")){
         res *= -1;
      }

      return res;
   }

   @Override public Integer visitExprMultDivMod(CalculatorParser.ExprMultDivModContext ctx) {
      Integer res = null;
      Integer e1 = visit(ctx.expr(0));
      Integer e2 = visit(ctx.expr(1));
      String op = ctx.op.getText();
      
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
      }
      
      return res;
   }
}
