import java.util.HashMap;

@SuppressWarnings("CheckReturnValue")
public class Interpreter extends CalculatorBaseVisitor<Integer> {
   protected static HashMap<String, Integer> varMapping = new HashMap<String, Integer>();

   @Override public Integer visitStatExpr(CalculatorParser.StatExprContext ctx) {
      Integer res = visit(ctx.expr());
      if(res != null){
         System.out.println(res);
      }
      return res;
   }

   @Override public Integer visitStatAssigment(CalculatorParser.StatAssigmentContext ctx) {
      return visit(ctx.assigment());
   }

   @Override public Integer visitAssigment(CalculatorParser.AssigmentContext ctx) {
      String id = ctx.ID().getText();
      Integer expr = visit(ctx.expr()); 
      varMapping.put(id, expr);

      System.out.println(String.format("%s --> %d", id, expr));
      return null;
   }

   @Override public Integer visitExprAddSub(CalculatorParser.ExprAddSubContext ctx) {
      Integer res = null;
      Integer expr1 = visit(ctx.expr(0));
      Integer expr2 = visit(ctx.expr(1));
      String op = ctx.op.getText();

      if(expr1 != null && expr2 != null){
         switch(op){
            case "+":
               res = expr1 + expr2;
               break;

            case "-":
               res = expr1 - expr2;
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
      String op = ctx.op.getText();
      Integer expr = visit(ctx.expr());
      
      if(op == "-"){ expr *= -1; }

      return expr;
   }

   @Override public Integer visitExprInteger(CalculatorParser.ExprIntegerContext ctx) {
      return Integer.parseInt(ctx.Integer().getText());
   }

   @Override public Integer visitExprId(CalculatorParser.ExprIdContext ctx) {
      String id = ctx.ID().getText();
      if(varMapping.containsKey(id)) return varMapping.get(id);
      return null;
   }

   @Override public Integer visitExprMultDivMod(CalculatorParser.ExprMultDivModContext ctx) {
      Integer res = null;
      Integer expr1 = visit(ctx.expr(0));
      Integer expr2 = visit(ctx.expr(1));
      String op = ctx.op.getText();

      if(expr1 != null && expr2 != null){
         switch(op){
            case "*":
               res = expr1 * expr2;
               break;

            case "/":
               res = expr1 / expr2;
               break;

            case "%":
               res = expr1 % expr2;
               break;

            default:
               break;
         }
      }

      return res;
   }
}
