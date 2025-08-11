import java.util.HashMap;

@SuppressWarnings("CheckReturnValue")
public class VInterpreter extends CalculatorBaseVisitor<Integer> {
   protected static HashMap<String, Integer> vars = new HashMap<String, Integer>();
   
   @Override public Integer visitStat(CalculatorParser.StatContext ctx) {
      Integer res = null;
      CalculatorParser.AssigmentContext assCtx = ctx.assigment();
      CalculatorParser.ExprContext exprCtx = ctx.expr();

      if (exprCtx != null){
         res = visit(exprCtx);
         System.out.println(String.format("Resultado: %d", res));
      }
      else if (assCtx != null){
         res = visit(assCtx);
      }

      return res;
   }

   @Override public Integer visitAssigment(CalculatorParser.AssigmentContext ctx) {
      Integer res = null;
      String varName = ctx.ID().getText();
      Integer varValue = visit(ctx.expr()); 
      
      if (varValue == null){
         System.err.println("ERROR: Invalid Value");
      }
      else {
         vars.put(varName, varValue);
         System.out.println(String.format("%s --> %d", varName, varValue));
      }
      
      return res;
   }

   @Override public Integer visitExprAddSub(CalculatorParser.ExprAddSubContext ctx) {
      Integer res = null;
      Integer e1 = visit(ctx.expr(0));
      Integer e2 = visit(ctx.expr(1));
      String op = ctx.op.getText();
      
      if (e1 == null || e2 == null){
         return res;
      }

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

   @Override public Integer visitExprUnary(CalculatorParser.ExprUnaryContext ctx) {
      Integer res = visit(ctx.expr());
      String op = ctx.op.getText();
      
      if (res == null){
         return res;
      }

      if(op.equals("-")){
         res *= -1;
      }

      return res;
   }

   @Override public Integer visitExprInteger(CalculatorParser.ExprIntegerContext ctx) {
      Integer res = Integer.parseInt(ctx.INTEGER().getText());
      return res;
   }

   @Override public Integer visitExprId(CalculatorParser.ExprIdContext ctx) {
      Integer res = null;
      String varName = ctx.ID().getText();
      if (!vars.containsKey(varName)){
         System.err.println("ERROR: Variavel <" + varName + "> not defined!");
      }
      else{
         res = vars.get(varName);
      }
      return res;
   }

   @Override public Integer visitExprMultDivMod(CalculatorParser.ExprMultDivModContext ctx) {
      Integer res = null;
      Integer e1 = visit(ctx.expr(0));
      Integer e2 = visit(ctx.expr(1));
      String op = ctx.op.getText();
      
      if (e1 == null || e2 == null){
         return res;
      }

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
