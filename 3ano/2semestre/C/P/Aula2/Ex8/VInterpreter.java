import java.util.HashMap;

@SuppressWarnings("CheckReturnValue")
public class VInterpreter extends CalculatorBaseVisitor<String> {
   private static HashMap<String, String> varMap = new HashMap<String, String>();

   @Override public String visitStatExpr(CalculatorParser.StatExprContext ctx) {
      String res = null;
      res = visit(ctx.expr());
      if (res != null){
         System.out.println(res);
      }
      return res;
   }

   @Override public String visitStatAssigment(CalculatorParser.StatAssigmentContext ctx) {
      String res = null;
      res = visit(ctx.assigment());
      if (res != null){
         System.out.println(res);
      }
      return res;
   }

   @Override public String visitAssigment(CalculatorParser.AssigmentContext ctx) {
      String res = null;
      String e1 = visit(ctx.expr());
      String id = ctx.ID().getText();
      if (e1 != null && id != null){
         res = String.format("%s = %s", id, e1);
         varMap.put(id, e1);
      }
      return res;
   }

   @Override public String visitExprAddSub(CalculatorParser.ExprAddSubContext ctx) {
      String res = null;
      String e1 = visit(ctx.expr(0));
      String e2 = visit(ctx.expr(1));
      if (e1 != null && e2 != null) {
         switch(ctx.op.getText()){
            case "+":
               res = String.format("%s %s +", e1, e2);
               break;
            case "-":
               res = String.format("%s %s -", e1, e2);
         }
      }
      return res;
   }

   @Override public String visitExprParent(CalculatorParser.ExprParentContext ctx) {
      String res = null;
      res = visit(ctx.expr());
      return res;
   }

   @Override public String visitExprUnary(CalculatorParser.ExprUnaryContext ctx) {
      String res = null;
      String e1 = visit(ctx.expr());
      if (e1 != null) {
         switch(ctx.op.getText()){
            case "+":
               res = String.format("%s !+", e1);
               break;
            case "-":
               res = String.format("%s !-", e1);
         }
      }
      return res;
   }

   @Override public String visitExprInteger(CalculatorParser.ExprIntegerContext ctx) {
      String res = null;
      res = ctx.INTEGER().getText();
      return res;
   }

   @Override public String visitExprId(CalculatorParser.ExprIdContext ctx) {
      String res = null;
      String id = ctx.ID().getText();
      if (varMap.containsKey(id)){
         res = varMap.get(id);
      }
      return res;
   }

   @Override public String visitExprMultDivMod(CalculatorParser.ExprMultDivModContext ctx) {
      String res = null;
      String e1 = visit(ctx.expr(0));
      String e2 = visit(ctx.expr(1));
      if (e1 != null && e2 != null) {
         switch(ctx.op.getText()){
            case "*":
               res = String.format("%s %s *", e1, e2);
               break;
            case "/":
               res = String.format("%s %s /", e1, e2);
         }
      }
      return res;
   }
}
